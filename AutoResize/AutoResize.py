import os
import sys
import subprocess
import shutil
from collections import Counter

EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}

def get_image_info(file_path):
    """magick"""
    try:
        result = subprocess.check_output(
            ['magick', 'identify', '-format', '%w,%h', file_path],
            stderr=subprocess.STDOUT
        ).decode().strip()
        w, h = map(int, result.split(','))
        return w, h, file_path
    except Exception:
        return None

def analyze_group(group_data, label_name):
    """
    分析图片组，返回该组的主导比例和基准分辨率
    """
    if not group_data:
        print(f"[{label_name}] 无图，跳过。")
        return None

    # 1. 统计该组的主导比例
    ratios = [d['ratio'] for d in group_data]
    most_common = Counter(ratios).most_common(1)
    target_ratio = most_common[0][0]
    count = most_common[0][1]

    # 2. 在主导比例的图片中，找到分辨率最小的作为基准
    valid_imgs = [d for d in group_data if d['ratio'] == target_ratio]
    standard_img = min(valid_imgs, key=lambda x: x['w'] * x['h'])
    
    print(f"[{label_name}] 比例改为 {target_ratio} (共 {count}/{len(group_data)} 张)")
    print(f"[{label_name}] 分辨率改为: {standard_img['w']}x{standard_img['h']} (基于{os.path.basename(standard_img['path'])})")
    
    return {
        'ratio': target_ratio,
        'w': standard_img['w'],
        'h': standard_img['h']
    }

def main():
    if len(sys.argv) < 2:
        print("错误：未接收到文件夹路径。")
        input("按回车退出...")
        return

    target_dir = sys.argv[1]
    print(f"正在分析文件夹: {target_dir}")
    
    # --- 1. 扫描文件 ---
    image_files = []
    for root, dirs, files in os.walk(target_dir):
        if root != target_dir: continue 
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                image_files.append(os.path.join(root, f))

    if not image_files:
        print("未找到图片。")
        return

    # --- 2. 收集数据并按横竖分组 ---
    print(f"正在读取 {len(image_files)} 张图片信息...")
    
    data = []     # 原始顺序数据
    land_data = [] # 横屏组 (宽 >= 高)
    port_data = [] # 竖屏组 (宽 < 高)

    for p in image_files:
        info = get_image_info(p)
        if info:
            w, h, path = info
            ratio = round(w / h, 2)
            item = {'w': w, 'h': h, 'ratio': ratio, 'path': path}
            
            data.append(item)
            if w >= h:
                land_data.append(item)
            else:
                port_data.append(item)

    if not data:
        return

    print("-" * 40)
    # --- 3. 分别分析横竖屏的主流标准 ---
    land_criteria = analyze_group(land_data, "横屏组")
    port_criteria = analyze_group(port_data, "竖屏组")
    print("-" * 40)

    # 定义备份文件夹路径 (暂不创建，只在需要修改文件时创建)
    backup_dir = os.path.join(target_dir, "Original_Backups")

    # --- 4. 执行处理 ---
    modified_count = 0
    
    for img in data:
        filename = os.path.basename(img['path'])
        
        # 判断当前图片属于哪一组
        is_landscape = img['w'] >= img['h']
        criteria = land_criteria if is_landscape else port_criteria
        
        if not criteria:
            continue

        prefix = "[横]" if is_landscape else "[竖]"

        if img['ratio'] == criteria['ratio']:
            # 比例符合 跳过
            print(f"{prefix} 比例符合，跳过: {filename}")
        else:
            # 比例不对 备份覆盖
            target_w = criteria['w']
            target_h = criteria['h']
            
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
                print(f"已创建备份文件夹: {backup_dir}")
            backup_path = os.path.join(backup_dir, filename)
            shutil.copy2(img['path'], backup_path)

            print(f"{prefix} 正在修正: {filename} (备份->覆盖)")
            subprocess.run([
                'magick', img['path'], 
                '-resize', f'{target_w}x{target_h}!', 
                img['path']
            ])
            modified_count += 1

    if modified_count == 0:
        print("\n无需修改。")
    else:
        print(f"\n处理完成！共修改了 {modified_count} 张图片。")
        print(f"被修改图片的原图已备份至: {backup_dir}")

if __name__ == "__main__":
    main()
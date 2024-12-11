from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def convert_filename(file_name):
    # 提取文件名中的数字
    digits = ''.join(filter(str.isdigit, file_name))
    
    # 处理数字部分
    tens_digit = int(digits[0])
    ones_digit = int(digits[-1])
    
    # 十位数字转换中文
    chinese_tens_digit = { '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}
    tens_digit_chinese = chinese_tens_digit[str(tens_digit)]
    
    # 个位数字添加括号
    ones_digit_with_bracket = f"({ones_digit})"
    
    # 构造新文件名
    new_file_name = f"{tens_digit_chinese}{ones_digit_with_bracket}"
    
    return new_file_name

def create_pdf(image_paths, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    pdfmetrics.registerFont(TTFont('simkai', 'simkai.ttf'))
    
    for image_path in image_paths:
        # 获取图片大小
        img = Image.open(image_path)
        img_width, img_height = img.size

        # 设置页面大小
        page_width, page_height = letter
        min_horizontal_margin = 1.27 * 28.35  # 将厘米转换为点
        # 计算缩放比例，确保等比例缩放
        width_ratio = (page_width - 2 * min_horizontal_margin) / img_width
        height_ratio = (page_height - 20) / img_height  # 顶部和底部留白

        # 选择较小的比例，确保图片不超出页面
        scale_ratio = min(width_ratio, height_ratio)

        # 缩放后的图片尺寸
        new_width = img_width * scale_ratio
        new_height = img_height * scale_ratio

        # 居中位置
        x = (page_width - new_width) / 2
        y = (page_height - new_height) / 2

        # 插入图片
        c.drawInlineImage(img, x, y, width=new_width, height=new_height)

        # 添加文件名
        file_name = os.path.basename(image_path)
        processed_file_name = convert_filename(file_name)
        print(processed_file_name)
        c.setFont('simkai', 15)
        
        # 插入文字
        text_x = page_width / 2
        text_y = 10
        c.drawCentredString(text_x, text_y, f"{processed_file_name}班")

        # 新建一页
        c.showPage()

    c.save()

if __name__ == "__main__":
    image_directory = r"C:\Users\Fofu\Desktop\qrcode"
    image_paths = [os.path.join(image_directory, file) for file in os.listdir(image_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    output_pdf = "output.pdf"

    create_pdf(image_paths, output_pdf)
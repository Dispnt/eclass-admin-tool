
# eclass-admin-tool

搬砖用到的小工具



| 序号 | 文件名 | 用处 |
| --- | --- | --- |
| 1 | StudentsQRCodetoPDF.py | 三个助手：将学生登录二维码批量保存为PDF |
| 2 | SeewoYunpin.js | 批量选中希沃云屏栏目媒体 |
| 3 | jspx.js | 教师培训 |
| 4 | setSubjectLeader.js | 三个助手：把所有教师变成学科组长 |
| 5 | 不知道还有没有 | 不知道还有没有 |

## 用法

### StudentsQRCodetoPDF

这个Python脚本用于批量插入学生登陆三个助手的二维码，生成带有班级的PDF文件。

#### 使用说明

1. **需要安装依赖：**
`pip install reportlab Pillow`

2. 将字体文件 `simkai.ttf` 保存在 `Python安装路径\Lib\site-packages\reportlab\fonts`

3. 将图片存在一个文件夹内，文件名可以是 `31.jpeg`、`32.jpeg`、`33.jpeg` ......



***

### SeewoYunpin.js

在[希沃云屏](https://easisee.seewo.com/ping)的节目内容来源的选择框中全选

#### 使用说明

1. 复制文件中的内容

2. 新建书签，把文件里的内容黏贴进去

3. 点一下省半小时

***

### jspx.js

🥶🥶🥶我不好说



***

### setSubjectLeader.js

在三个助手平台的[学科教师管理](https://dolearning.net/school/subjects)里把所有老师设为学科组长，这样他们可以直接上传\修改校本资源。

**这样操作后，他们也可以删掉别人上传的校本内容**

#### 使用说明

1. 在备课助手里随便点一个学科进去，点击左上角的田字形

2. 点击`运维管理->学科管理`

3. 选择学科最右边的`管理学科教师`

4. 会发现这几百号人都是普通教师：他们只能先上传个人资源，再转换成**不能删除的**校本资源。
复制脚本并运行，所有人在三秒后都是组长，普渡众生


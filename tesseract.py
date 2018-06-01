from PIL import Image
import pytesseract
from pytesseract import *

rep={'O':'0',                           #替换列表
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    };

def initTable(threshold=140):           # 二值化函数
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table
#--------------------------------------------------------------------------------------
im = Image.open('C:\\Users\win7\Downloads\GetVerifyCode.do.gif')     #1.打开图片
im = im.convert('L')                                        #2.将彩色图像转化为灰度图
binaryImage = im.point(initTable(), '1')                    #3.降噪，图片二值化
# binaryImage.show()

vcode = image_to_string(binaryImage, config='-psm 7')

#4.对于识别结果，常进行一些替换操作
for r in rep:
    vcode = vcode.replace(r,rep[r])

#5.打印识别结果
print(vcode)

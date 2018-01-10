import os
import re
import urllib.request

import pytesseract
from PIL import Image

'''
tesseract识别验证码
'''
if __name__ == '__main__':
    img_src = 'https://proxy.mimvp.com/common/ygrcode.php'
    for i in range(1, 10):
        tempDir = "d:/temp/"
        fileSuffix = ".png"
        if not os.path.exists(tempDir):
            os.mkdir(tempDir)
        fileUrl = tempDir + str(i) + fileSuffix
        # 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
        urllib.request.urlretrieve(img_src, fileUrl)
        image = Image.open(fileUrl)
        # 灰度化
        image = image.convert('L')
        # 识别图片
        code = pytesseract.image_to_string(image)
        # 过滤掉非数字字母字符
        code = re.sub(r"[^1-9a-zA-Z]", "", code)
        # 重命名文件
        os.rename(fileUrl, tempDir + code + fileSuffix)

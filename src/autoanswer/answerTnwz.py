# -*- coding: utf-8 -*-

import io

from PIL import Image

from autoanswer.answer import Answer

'''
头脑王者
'''


class AnswerTnwz(Answer):
    def __init__(self):
        self.name = 'tnwz'

    '''
    处理图片
    '''

    def processImg(self, screen):
        tmp = io.BytesIO(screen)
        with Image.open(tmp) as f:
            # 切割图片，拼接问题和选项
            imageQuestion = f.crop((0, 500, f.size[0], 900))
            imageOptions = f.crop((0, 960, f.size[0], 1700))
            newImg = Image.new("RGB", (f.size[0], 1140))
            newImg.paste(imageQuestion, (0, 0))
            newImg.paste(imageOptions, (0, 400))
            newImg.save("screen.png")

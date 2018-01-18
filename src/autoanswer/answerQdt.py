# -*- coding: utf-8 -*-

import io

from PIL import Image

from autoanswer.answer import Answer

'''
趣答题
'''


class AnswerQdt(Answer):
    def __init__(self):
        self.name = 'qdt'

    '''
    处理图片
    '''

    def processImg(self, screen):
        tmp = io.BytesIO(screen)
        with Image.open(tmp) as f:
            # 切割图片，拼接问题和选项
            newImg = f.crop((0, 600, f.size[0], 1660))
            newImg.save("screen.png")

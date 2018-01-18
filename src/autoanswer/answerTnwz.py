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
        self.optionsNum = 4

    '''
    过滤数据
    '''

    def filterData(self, data):
        return data

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

    '''
    解析答案
    '''

    def parseOptions(self, content, options):
        map = {}
        # 得到每个答案的出现次数
        for option in options:
            map[option] = content.text.count(option)
        print('match:', map)
        # 按出现次数排序，出现次数最多则为答案
        option = sorted(map, key=lambda k: map[k])[-1]
        print('result:', option)
        return option

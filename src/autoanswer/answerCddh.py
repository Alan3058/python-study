# -*- coding: utf-8 -*-

import io

from PIL import Image

from autoanswer.answer import Answer

'''
冲顶大会
'''


class AnswerCddh(Answer):
    def __init__(self):
        self.name = 'cddh'
        self.optionsNum = 3

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
            newImg = f.crop((0, 400, f.size[0], 1500))
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

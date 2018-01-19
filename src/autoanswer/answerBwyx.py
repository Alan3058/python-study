# -*- coding: utf-8 -*-

import io
import re

from PIL import Image

from autoanswer.answer import Answer

'''
百万英雄
'''


class AnswerBwyx(Answer):
    def __init__(self):
        self.name = 'bwyx'
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
            newImg = f.crop((0, 300, f.size[0], 1300))
            newImg.save("screen.png")

    '''
    解析答案
    '''

    def parseOptions(self, content, options):
        seqs = r"(A|B|C|D)(、|.)"
        map = {}
        # 得到每个答案的出现次数
        for option in options:
            map[option] = content.text.count(re.sub(seqs, '', option))
        print('match:', map)
        # 按出现次数排序，出现次数最多则为答案
        option = sorted(map, key=lambda k: map[k])[-1]
        print('result:', option)
        return option

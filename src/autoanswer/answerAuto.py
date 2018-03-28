# -*- coding: utf-8 -*-
import logging

from autoanswer.answerBwyx import AnswerBwyx
from autoanswer.answerCddh import AnswerCddh
from autoanswer.answerQdt import AnswerQdt
from autoanswer.answerTnwz import AnswerTnwz

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

if __name__ == '__main__':
    applicationNum = input("please select application(0:头脑王者，1:趣答题，2:冲顶大会，3:百万英雄，default:头脑王者):")
    if applicationNum == '0':
        # 头脑王者
        AnswerTnwz().run()
    elif applicationNum == '1':
        # 趣答题
        AnswerQdt().run()
    elif applicationNum == '2':
        # 冲顶大会
        AnswerCddh().run()
    elif applicationNum == '3':
        # 百万英雄
        AnswerBwyx().run()
    else:
        # 默认头脑王者
        AnswerTnwz().run()

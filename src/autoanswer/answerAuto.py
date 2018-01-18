# -*- coding: utf-8 -*-
from autoanswer.answerCddh import AnswerCddh
from autoanswer.answerQdt import AnswerQdt
from autoanswer.answerTnwz import AnswerTnwz

if __name__ == '__main__':
    applicationNum = input("please select application(0:头脑王者，1:趣答题，2:冲顶大会，default:头脑王者):")
    if applicationNum == '0':
        # 头脑王者
        AnswerTnwz().run()
    elif applicationNum == '1':
        # 趣答题
        AnswerQdt().run()
    elif applicationNum == '2':
        # 冲顶大会
        AnswerCddh().run()
    else:
        # 默认头脑王者
        AnswerTnwz().run()

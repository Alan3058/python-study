# -*- coding: utf-8 -*-
import logging
import os
import random
import subprocess
from abc import abstractmethod
from urllib import request, parse

from aip import AipOcr
from bs4 import BeautifulSoup

from autoanswer.config import APP_ID, API_KEY, SECRET_KEY, CONFIG


class Answer(object):
    def __init__(self, name, optionsNum=4):
        # 名称
        self.name = name
        # 选项数量
        self.optionsNum = optionsNum

    '''
    获取屏幕截屏图片信息
    '''

    def getScreen(self):
        process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        screen = process.stdout.read()
        if not screen:
            logging.error('connect phone failed!---------')
        screen = screen.replace(b'\r\n', b'\n')
        return screen

    '''
    处理图片
    '''

    @abstractmethod
    def processImg(self, screen):
        pass

    '''
    解析图片，得到问题和选项
    '''

    def parseImg(self):
        # 未传图片，直接从本地获取，便于调试
        with open('screen.png', 'rb') as f:
            img = f.read()
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        data = client.basicGeneral(img)
        data = [v['words'] for v in (data['words_result'])]
        print('data:', data)
        data = self.filterData(data)
        # 提取问题
        question = ''.join(data[:-1 * self.optionsNum])
        # 提取选项
        options = data[-1 * self.optionsNum:]
        return question, options

    '''
    过滤数据
    '''

    @abstractmethod
    def filterData(self, data):
        pass

    '''
    获取答案
    '''

    def getAnswer(self, question, options):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip',
            'Connection': 'close',
            'Referer': None  # 如果依然不能抓取的话，这里可以设置抓取网站的host
        }
        url = 'http://www.baidu.com/s?ie=utf-8&wd=' + parse.quote(question)
        print('question：', question)
        print('options', options)
        opener = request.build_opener()
        opener.addheaders = [headers]
        with request.urlopen(url) as f:
            html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        # 获取网页内容
        content = soup.select('#content_left')
        content = content[0] if content else soup
        # 去除script和style
        for tag in content.find_all('script'):
            tag.decompose()
        for tag in content.find_all('style'):
            tag.decompose()
        return self.parseOptions(content, options)

    '''
    解析答案
    '''

    @abstractmethod
    def parseOptions(self, content, options):
        pass

    '''
    模拟点击函数
    '''

    def click(self, path):
        fmx = random.randint(path['x'], path['x'] + path['offsetx'])
        fmy = random.randint(path['y'], path['y'] + path['offsety'])
        cmd = 'adb shell input tap %s %s' % (fmx, fmy)
        os.system(cmd)

    '''
    运行入口
    '''

    def run(self):
        while True:
            command = input("please input enter key(input q , then exit):")
            if command.lower() == 'q':
                exit()
            screen = self.getScreen()
            self.processImg(screen)
            question, options = self.parseImg()
            # 获取答案
            option = self.getAnswer(question, options)
            # 点击对应答案
            self.click(CONFIG[self.name][options.index(option)])

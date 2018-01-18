# -*- coding: utf-8 -*-

import io
import os
import random
import subprocess
from urllib import request, parse

from PIL import Image
from aip import AipOcr
from bs4 import BeautifulSoup

CONFIG = [{'x': 250, 'y': 970, 'offsetx': 580, 'offsety': 140},
          {'x': 250, 'y': 1160, 'offsetx': 580, 'offsety': 140},
          {'x': 250, 'y': 1350, 'offsetx': 580, 'offsety': 140},
          {'x': 250, 'y': 1540, 'offsetx': 580, 'offsety': 140}]

APP_ID = '107047421'
API_KEY = 'xwxcfbWLQEF0GWUDcNwM4wECa'
SECRET_KEY = 'a6qFgZpAXGX84gaSbM1dne4XydnvqDcga'

'''
获取屏幕截屏图片信息
'''


def getScreen():
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screen = process.stdout.read()
    screen = screen.replace(b'\r\n', b'\n')
    return screen


'''
处理图片
'''


def processImg(screen):
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
解析图片，得到问题和选项
'''


def parseImg():
    # 未传图片，直接从本地获取，便于调试
    with open('screen.png', 'rb') as f:
        img = f.read()
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    data = client.basicGeneral(img)
    data = [v['words'] for v in (data['words_result'])]
    print('data:', data)
    # 提取问题
    question = ''.join(data[:-4])
    # 提取选项
    options = data[-4:]
    return question, options


'''
获取答案
'''


def getAnswer(question, options):
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
    map = {}
    # 得到每个答案的出现次数
    for option in options:
        map[option] = content.text.count(option)
    print('match:', map)
    # 按出现次数排序，出现次数最多则为答案
    option = sorted(map, key=lambda k: map[k])[-1]
    print('result:', option)
    return option


'''
模拟点击函数
'''


def click(path):
    fmx = random.randint(path['x'], path['x'] + path['offsetx'])
    fmy = random.randint(path['y'], path['y'] + path['offsety'])
    cmd = 'adb shell input tap %s %s' % (fmx, fmy)
    os.system(cmd)


'''
运行入口
'''


def run():
    while True:
        command = input("please input enter key(input q , then exit):")
        if command.lower() == 'q':
            exit()
        screen = getScreen()
        processImg(screen)
        question, options = parseImg()
        # 获取答案
        option = getAnswer(question, options)
        # 点击对应答案
        # click(CONFIG[options.index(option)])


if __name__ == '__main__':
    run()

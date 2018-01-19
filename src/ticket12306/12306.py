import json
from urllib import request

import re
from bs4 import BeautifulSoup

queryStationUrl = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9046'
queryTicketUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
with request.urlopen(queryStationUrl) as f:
    content = f.read()
content = content.decode('utf-8')
contents = content.split('@')
stationMap = {}
for value in contents[1:]:
    values = value.split('|')
    stationMap[values[1]] = values[2]


def queryTicket(fmStationName, toStationName, date):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=654CC35C5E57A3E0599E152B422AE64F; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1624834314.64545.0000; RAIL_EXPIRATION=1516699251616; RAIL_DEVICEID=plIEoz8Y21BXFMNj0O4N4onsSGPGUWYroMTYbpRxN-sL0pdMVPLOYBg30YDe42_lXELnG-zERcv0Oeq6eeGc09Ga27Ayz-Jd3mATTLee_WImyF3RvYPgdUUyd0JHw0yDckYaz7Vjkm3xj9xvJfwQfqjUKT3erWXu; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2018-01-19; _jc_save_toDate=2018-01-19; _jc_save_wfdc_flag=dc',
        'Host': 'kyfw.12306.cn',
        'If-Modified-Since': 0,
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400',
        'X-Requested-With': 'XMLHttpRequest'
    }
    opener = request.build_opener()
    opener.addheaders = [headers]
    url = queryTicketUrl.format(date, stationMap[fmStationName], stationMap[toStationName])
    print('url:', url)
    with request.urlopen(url) as conn:
        jsonstr = conn.read()
    jsonstr = jsonstr.decode('utf-8')
    jsondata = json.loads(jsonstr)
    map = jsondata['data']['map']
    result = jsondata['data']['result']
    print('车次', '出发地', '到达地', '开始时间', '结束时间', '商务座', '一等', '二等', '高级软卧', '软卧', '动卧', '硬卧', '软座', '硬座', '无座')
    for v in result:
        values = v.split('|')
        print(values[3], values[4], values[5], values[8], values[9], values[-5], values[-6], values[-7], values[-16],
              values[-14], values[-4],
              values[-9], values[-13], values[-8],
              values[-11])


if __name__ == '__main__':
    while True:
        data = input('please input fmstation to station and date（北京 上海 2018-02-09）：')
        if data.lower() == 'q':
            exit()
        datas = re.split(r'\s+', data.strip())
        queryTicket(datas[0], datas[1], datas[2])

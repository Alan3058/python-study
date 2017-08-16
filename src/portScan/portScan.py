'''
Created on 2017年8月12日
端口扫描器
@author: liliangang
'''
import socket
import threading
import time
import argparse


class PortScan:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.availablePort = []
    
    # 扫描端口
    def scan(self, host="", port=0):
        # 默认主机名和端口
        host = host if host != "" else self.host
        port = port if port > 0 else self.port
        
        # 建立socket连接
        s = socket.socket()
        errono = s.connect_ex((host, port))
        s.close()
        if errono == 0 :
            self.availablePort.append(port)
            print("host {} port {} enabled.".format(host, port))
        else:
            print("host {} port {} disabled, errno is {}.".format(host, port, errono))
    # 开启线程扫描
    def quickScan(self, host, port):
        t = threading.Thread(target=self.scan, args=(host, port))
        t.start()

# 获取命令行参数
def getArgs():
    hostHelp = 'host  default localhost.'
    portHelp = '''port default 1000,will scan scope from 0 to 999; 
                if the value is 1..100 , then scan scope from 1 to 99; 
                if the value is 80 88 90,then scan scope is 80 88 90.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='host', default='localhost', help=hostHelp)
    parser.add_argument('-p', dest='port', default=['1000'], nargs='+', help=portHelp)
    args = parser.parse_args()
    host = args.host 
    port = args.port
    ports = []
    if len(port) >= 2:
        ports = list(map(int, port))
    else :
        p = port[0].split(sep='..')
        if len(p) == 1:
            ports = range(int(p[0]))
        else:
            ports = range(int(p[0]), int(p[1]))
    return {'host':host, 'port':ports}
if __name__ == '__main__':
    arg = getArgs()
    host = arg['host'] 
    port = arg['port']
    portScan = PortScan();
    for port in port:
        portScan.quickScan(host, port)
    time.sleep(5)
    print('host {} port {} is enabled.'.format(host, portScan.availablePort))
        

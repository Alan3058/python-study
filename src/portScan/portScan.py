'''
Created on 2017年8月12日
端口扫描器
@author: liliangang
'''
import socket
import threading
import time


class PortScan:
    def __init__(self, hostName="", port=0):
        self.hostName = hostName
        self.port = port
        self.availablePort = []
    
    def scan(self, hostName="", port=0):
        # 默认主机名和端口
        hostName = hostName if hostName != "" else self.hostName
        port = port if port > 0 else self.port
        
        # 建立socket连接
        s = socket.socket()
        errono = s.connect_ex((hostName, port))
        s.close()
        if errono == 0 :
            self.availablePort.append(port)
            print("hostName {} port {} 可用".format(hostName, port))
        else:
            print("hostName {} port {} 不可用，errno is {}".format(hostName, port, errono))
    def quickScan(self, hostName, port):
        t = threading.Thread(target=self.scan, args=(hostName, port))
        t.start()
if __name__ == '__main__':
    portScan = PortScan();
    for port in range(1000):
        portScan.quickScan("localhost", port)
    time.sleep(5)
    print(portScan.availablePort)
        

'''
Created on 2017年8月16日
随机密码生产
@author: liliangang
'''
import random

class RandomPassword:
    def __init__(self, length=8):
        self.factor = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+=-'
        self.length = length
    def next(self, length=0):
        length = length if length > 0 else self.length
        array = []
        for i in range(length) :
            array.append(self.factor[random.randint(0, len(self.factor) - 1)])
        return ''.join(array)
if __name__ == '__main__':
    for i in range(10) :
        print(RandomPassword().next());
        

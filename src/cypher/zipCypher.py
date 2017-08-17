'''
Created on 2017年8月16日
zip文件密码破解例子
@author: liliangang
'''
import zipfile
import argparse

def zipDecrption(zipFileName, fileName):
    file = zipfile.ZipFile(zipFileName)
    passwordFile = open(fileName)
    for password in passwordFile.readlines():
        password = password.strip()
        try:
            file.extractall(path='tmp', pwd=password.encode('utf-8'))
            print("password was found -> '{}'".format(password))
            break
        except Exception as e:
            print(e)
    file.close()
if __name__ == '__main__':
    argparser = argparse.ArgumentParser('zip decrption.')
    argparser.add_argument('-f', dest='zipFileName', help='zip fileName')
    argparser.add_argument('-p', dest='fileName', help='password fileName')
    args = argparser.parse_args()
    zipFileName = args.zipFileName
    fileName = args.fileName
    zipDecrption(zipFileName, fileName)
    # zipDecrption('C:\\Users\\dell\\Desktop\\src.zip', 'C:\\Users\\dell\\Desktop\\password.txt')

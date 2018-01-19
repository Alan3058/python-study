# autoanswer/answerAuto.py:自动答题
## 注意事项
1. 如果没有安装adb驱动，需要安装（http://dl.adbdriver.com/upload/adbdriver.zip）
2. 下载adb工具包（http://dl-t1.wmzhe.com/39/39913/platform-tools-latest-windows.zip）
3. 将adb加入到环境变量中，否则无法找到命令(可能需要重启idea工具，以便能加载新的环境变量)
4. adb shell测试是否可以连接
5. 允许debug调试模式，并需要开启模拟点击功能

## 总结
1. 需要在网速良好的情况下去运行，效果更好。
2. 使用了两次网络调用，解析图片和解析答案，因此答题速度很难快起来。
3. 由于没有题库，会降低答题的准确性，最好可以建立题库，以提高答题效率。
4. 只能赢取文盲（比如像我这种），除非答题不分快慢，呵呵。。。

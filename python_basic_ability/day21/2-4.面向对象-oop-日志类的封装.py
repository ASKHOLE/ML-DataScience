# 日志类的封装


'''
日志类
    class  Mylog
    功能：
        能够随时写入一个日志信息

分析：
    日志文件在什么地方？ 默认在当前目录
    日志的文件名是什么？ 当前日期 2019-09-20.log
    日志的格式是什么样的？ 2019-09-20 12:12:12 错误信息。。。

    属性：成员属性的作用就是存储信息，供成员方法来使用的
        fileurl 日志文件的地址
        filename 日志文件的名称
        fileobj 打开的文件对象


    方法：具体完成的一个功能的过程
        __init__()  ==> 初始化方法，完成对象的初始化，并打开文件
        log()      ==> 负责接受用给的日志信息，并写入到日志文件中
        __del__()   ==> 析构方法，在对象被销毁时，关闭打开的文件
'''

import time
class Mylog():
    # 属性
    fileurl = './'
    filename = str(time.strftime('%Y-%m-%d'))+'.log'
    fileobj = None

    # 方法
    def __init__(self):
        # 打开文件
        self.fileobj = open(self.fileurl+self.filename,'a+',encoding='utf-8')

    def log(self,s):
        # 准备数据，开始写入
        # 2019-09-20 12:12:12 错误信息。。。
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = date+' '+s+'\n'
        # 写入
        self.fileobj.write(msg)

    def __del__(self):
        # 关闭打开的文件
        self.fileobj.close()


# 实例化对象
w = Mylog()
# 调用方法 写日志
w.log('今天天气不太好，而且楼市在装修。。。。')
w.log('楼上装修能理解，但是说话不算数，很讨厌。。。。')




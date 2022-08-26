# 析构方法 __del__

'''
__del__ 析构方法
    触发机制：析构方法会在对象被销毁时自动触发
    作用：关闭一些开发的资源
    注意：是对象被销毁时触发了析构方法，而不是析构方法销毁了对象

对象会在哪些情况下被销毁？
    1。 当程序执行完毕，内存中所有的资源都会被销毁释放
    2。 使用 del 删除时
    3。 对象没有被引用时，会自动销毁
'''

'''
定义一个类，完成一个日志的记录
    调用这个对象的时候，传递一个日志信息
    这个对象会创建一个文件，开始写入，并在最后关闭这个文件
'''

import time

class writeLog():
    # 成员属性
    # 文件的路径
    fileurl = './'
    # 日志文件的名称
    filename = '2019-09-19'

    # 初识化  打开文件
    def __init__(self):
        #完成文件的打开
        print('初始化方法触发类。完成文件的打开')
        self.fileobj = open(self.fileurl+self.filename,'a+',encoding='utf-8')

    # 写日志的方法
    def log(self,s):
        print(f'把日志：{s} 写入文件中')

    # 析构方法
    def __del__(self):
        print('析构方法触发了，关闭打开的文件')
        # 在对象被销毁时，关闭在初始化方法中打开的文件对象
        self.fileobj.close()

#实例化对象
# l = writeLog()
# l.log('今天天气还不错哦。。')

# 使用del手动删除
# del l

# 当对象没有被引用时
# writeLog()

# print('....')



# 思考一个问题？
class Cart():
    brand = ''

    def __init__(self,b):
        self.brand = b
        print(f'初始化方法被触发:创建{self.brand}汽车')

    def __del__(self):
        print(f'析构方法被触发:{self.brand}汽车已经销毁了')


# 问题1。请写出下面程序的执行结果
bm = Cart('宝马')
bc = Cart('奔驰')
fll = Cart('法拉利')

'''
1 宝马创建
2 奔驰创建
3 法拉利创建
4 宝马被销毁
5 奔驰被销毁
6 法拉利被销毁
'''

# 问题2。请写出下面程序的执行结果
# Cart('宝马')
# Cart('奔驰')
# Cart('法拉利')
'''
1 宝马创建
2 宝马销毁
3 奔驰创建
4 奔驰销毁
5 法拉利创建
6 法拉利销毁
'''



#  多态 普通版本
# 对于同一个方法，由于调用的对象不同（或者传入的对象不同），最终实现了不同的结果

# 定义电脑类
class Computer():
    # 在电脑类中定义一个 sub 的规范的接口 方法
    def usb(self,obj):
        obj.start()

# 定义鼠标类
class Mouse():
    def start(self):
        print('鼠标启动成功，可以双击单击嗨起来。。。')

# 定义键盘类
class KeyBord():
    def start(self):
        print('键盘启动成功了，赶紧双击666。。。')

# 定义 U盘 类
class Udisk():
    def start(self):
        print('U盘启动了，赶紧检查一下我的种子还在不在。。。')

# 实例化对象
c = Computer()  # 电脑对象
m = Mouse()     # 鼠标对象
k = KeyBord()   # 键盘对象
u = Udisk()     # u盘对象


# 把不同的设备插入到电脑的usb的接口中
c.usb(m)
c.usb(k)
c.usb(u)








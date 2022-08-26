# 。面向对象 oop 基本实现

'''

类名的书写规范，建议使用驼峰命名法
    大驼峰：MyCar XiaoMi
    小驼峰：myCar xiaoMi

一个类有特征和功能两个内容组成：
    特征就是一个描述：颜色：白色，品牌：奥迪，排量：2.4 。。。
    功能就是一个能力：拉货，带美女兜风。。。。

    特征在编程中就是一个变量，在类中称为 属性
    功能在编程中就是一个函数，在类中称为 方法

类中属性一般定义在前面，方法定义在后面
'''

# 定义一个汽车的类
class Cart():
    # 属性 ==> 特征 ==> 变量
    color = '白色'  # 表示颜色属性
    brand = '奥迪'  # 表示品牌属性
    pailiang = 2.4 # 表示排列属性

    # 方法 ==> 功能 ==> 函数
    def luohuo(self):
        print('小汽车能拉货')

    def doufeng(self):
        print('小汽车能兜风')

    def bamei(self):
        print('带妹子去嗨。。。')


# 如何去使用这个类？
# 通过类实例化一个对象
aodiobj =  Cart()

# print(aodiobj,type(aodiobj))
# <__main__.Cart object at 0x106f08550> <class '__main__.Cart'>

# 调用对象的方法
aodiobj.bamei()

# 获取对象的属性
print(aodiobj.brand)




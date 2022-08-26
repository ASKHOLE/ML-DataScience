# 面向对象 三大特性  - 继承

'''
当子类继承父类后，就可以去使用父类中的成员属性和方法 （除了私有成员）
子类可以有自己独立的成员，也可以没有
子类继承父类后，重新定义了父类中的方法，这种情况称为对父类方法的重写
在子类中可以去直接调用父类中定义的方法 super().父类方法名()
子类继承父类后，定义类父类中没有的方法，这种情况称为 对父类的 扩展
一个父类可以被多个子类继承
子类调用父类的方法时，如果该方法有参数要求，也需要传递参数
'''

# 猫科动物
class maoke():
    # 属性
    maose = '猫纹'
    sex = 'm'

    # 方法
    def pao(self):
        print('走猫步')

    def pa(self):
        print('能上树')

# 定义猫类  去继承 猫科 类
class mao(maoke):

    # 继承父类后，重新定义了父类中的方法
    def pa(self):
        # 在子类中可以使用super直接调用父类的方法
        super().pa()
        print('很快的就能上树了')

    def zhua(self):
        print('喜欢抓老鼠')

# 通过猫类 实例化对象
h = mao()
# print(h)
# print(h.__dict__)  # {}

# 可以获取对象的属性 猫对象自己的属性 ==> 猫类的属性，===> 继承的父类
# print(h.maose)
# 调用对象的方法
# h.pao()
# h.pa()
# h.zhua()


class bao(maoke):
    pass

b = bao()
print(b)
b.pa()

res = 100/3
print(res)
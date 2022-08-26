#  菱形继承
'''
    HuMan
 F       M
     C
'''

# 祖先类
class HuMan():
    num = 444
    def eat(self):
        print(self.num)
        print('顿顿都是小烧烤。。。')

# 父亲类
class F(HuMan):
    num = 333
    def eat(self):
        super().eat()
        print(super().num)
        print('大口喝酒，大口吃肉。。。')

# 母亲类
class M(HuMan):
    num = 222
    def eat(self):
        super().eat()
        print(super().num)
        print('动作优雅，浅尝即止')

# 孩子类
class C(F,M):
    num = 111
    def eat(self):
        super().eat()
        print(super().num)
        print('吃也哭，不吃也哭。。。')

# 实例化对象
c = C()
c.eat()

'''
继承的关系：C->F->M->HuMan

111
顿顿都是小烧烤。。。
444
动作优雅，浅尝即止
222
大口喝酒，大口吃肉。。。
333
吃也哭，不吃也哭。。。

'''
# mro() 获取MRO列表，就是类的继承关系
print(C.mro())
# [<class '__main__.C'>, <class '__main__.F'>, <class '__main__.M'>, <class '__main__.HuMan'>, <class 'object'>]

'''
super()
    使用super去调用父级的方法时，实际上是在用super调用MRO列表中的上一级中的方法，
    使用super去访问父级的属性时，实际上是在用super访问MRO列表中的上一级中的属性。
super()本身调用父级方法时，传递的self对象，就是这个方法中的那个self对象自己
    
'''
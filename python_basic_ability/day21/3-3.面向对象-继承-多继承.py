#  多继承

# 多继承和多继承中的父类方法的调用

# 父亲类
class F():
    def eat(self):
        print('大口喝酒，大口吃肉。。。')

# 母亲类
class M():
    def eat(self):
        print('动作优雅，浅尝即止')

# 孩子类
class C(F,M):
    def eat(self):
        super().eat() # 多继承和多继承中的父类方法的调用
        print('吃也哭，不吃也哭。。。')

# 实例化对象
c = C()
c.eat()


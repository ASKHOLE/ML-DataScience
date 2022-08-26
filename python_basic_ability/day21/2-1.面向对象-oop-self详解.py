# 。self

# 定义人类
class Person():
    # 成员属性
    name = '名字'
    age = '年龄'
    sex = '性别'

    # 成员方法
    def sing(self):
        print('会唱。。。')

    def dance(self):
        print('会跳。。。')

    def rap(self):
        print(f'我是{self.name}我会rap。。。')

    def func(self):
        # # 测试，在类的内部是否可以像类的外部一样，去访问和操作成员
        # print(self)
        # print(self.name)  # 访问对象的属性
        # self.name = '张三三' # 修改对象的属性
        # self.sanwei = '80 80 80' #添加对象的属性
        # print(self.sanwei)
        self.rap()  # 调用对象的方法
        # 只要是对象能干的事，self都可以代表对象去完成
        # 比如：成员的所有操作（添加，删除，更新，访问，调用。。）
    # def func2(a):

    # 定义不含self的方法  绑定类方法 （不接受对象参数的方法，只能使用类去访问）
    def func2():
        print('我是一个没有self的方法')


# 实例化对象
zs = Person()
# zs.name = '张三'
# 通过类实例化的对象，可以在类的外部去访问成员属性和成员方法  对象.成员
# print(zs)
# zs.func()
# zs.rap()
'''
self 单词本身的意思  自己
self 在类的方法中 代表 当前这个对象
self 代表调用这个方法的对象,谁调用了这个方法，self就代表谁
self 就可以在类的内部代替对象进行各种操作

如果在类中定义的方法不含self这个形参时，（self形参，包括其它的代替都不可以）
那么这个方法就不能使用对象去调用
不含self形参的方法，只能使用类去调用，
这种不接受对象作为形参的方法，叫做绑定类方法
'''

# zs.func2()
Person.func2()






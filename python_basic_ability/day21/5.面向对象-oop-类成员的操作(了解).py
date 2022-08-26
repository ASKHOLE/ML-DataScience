#  类成员的操作
# 定义一个汽车的类
class Cart():
    # 属性 ==> 特征 ==> 变量
    color = '白色'  # 表示颜色属性
    brand = '奥迪'  # 表示品牌属性
    pailiang = 2.4 # 表示排列属性

    # 方法 ==> 功能 ==> 函数
    def lahuo(self):
        print('小汽车能拉货')

    def doufeng(self):
        print('小汽车能兜风')

    def bamei(self):
        print('带妹子去嗨。。。')


# 在类的外部，可以直接通过类对成员进行操作
a = Cart()

# 一，类成员属性的操作
# 访问类成员属性
# print(Cart.brand)
# 修改类成员属性
Cart.brand = '宝马'
# print(Cart.brand)

# 思考：如果通过类把属性进行类修改，那么再通过这个类实例化的对象，它的属性是什么呢？那之前创建的对象呢？
b = Cart()

# print(b.brand)# 是修改后的结果
# print(a.brand) # 在类属性修改前创建的对象的属性也被修改

# 给类添加成员属性
Cart.name = 'A6'
# print(Cart.name)

# 思考：通过类创建的对象是否也有这个属性呢？之前创建的对象和之后创建的对象都会有这个新的属性
# print(b.name)
# c = Cart()
# print(c.name)

# 删除类的成员: 在之前和之后创建的对象，都不在有这个属性了
del Cart.brand
# print(a.brand)

# 二 类成员方法的操作，



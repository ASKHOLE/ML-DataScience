#  继承关系检测

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

# 获取类的 MRO列表

# print(A.mro())


# 检测一个类是否是另一个类的子类
res = issubclass(D,B) # True 检测D类是不是B类的子类
res = issubclass(D,C) # True 检测D类是不是C类的子类
res = issubclass(D,A) # True 检测D类是不是A类的子类
res = issubclass(A,D) # False 检测A类是不是D类的子类

print(res)

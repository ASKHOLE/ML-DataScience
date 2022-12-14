# 自定义模块

# 定义类
class MyException():
    pass

# 定义函数
def func():
    print('我是一个模块中的func函数')

love = 'iloveyou'

# 特殊的变量 __name__
# __name__ 这个变量，在当前脚本作为模块被别的程序导入是 __name__的值 是当前这个模块的名称
#在当前脚本被作为主程序直接由python解析运行时，__name__的值 是 '__main__'
name = __name__
print(name)

# 自定义模块中，通常只是去定义类或函数，变量，等，并不调用
# 如果在自定义模块中，想要写一些测试代码，在当前模块作为主程序使用时执行，
# 而作为模块被别的程序导入时不执行，那么可以把测试代码写到 下面代码块中
if __name__ == '__main__':
    print('这个位置写的代码只有当前脚本被直接运行时触发')




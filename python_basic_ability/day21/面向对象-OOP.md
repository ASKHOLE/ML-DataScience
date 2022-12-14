# 面向对象-OOP

> 面向对象编程——Object Oriented Programming，简称`OOP`，是一种**以对象为中心**的程序设计思想。
>
> 面向过程编程——Procedure Oriented Programming，简称`POP`，是一种**以过程为中心**的程序设计思想。



## 理解面向过程与面向对象思想

大家先思考一个问题：把大象装进冰箱，需要几步？

小品给出的答案：三步

第一步：打开冰箱门

第二步：把大象装进去

第三步：关上冰箱门



##### 用面向过程去理解

> 上面给出的答案就是面向过程的，遇到问题后，分析解决问题的步骤，然后一步步去实现

##### 用面向对象去理解

> 是通过分析问题中需要的抽象模型，然后更具需要的功能分别去创建模型对象，最终由模型对象来完成程序

首先面向对象要解决这个问题，需要先建立出抽象模型，比如：打开冰箱门和关闭冰箱门，这都属于一个冰箱的功能，大象走进去，这就是大象的功能。到此时我们就出现了两个抽象模型，一个是冰箱，一个是大象。

冰箱具有 打开和关闭的功能，大象具有走路的能力。

分析到这里，就是面向对象的思想，具体完成的话，就是去创建冰箱和大象这两个对象，最终完成这个程序

冰箱对象-开门，大象对象-走进冰箱，冰箱对象-关门



再思考一个问题，想吃清蒸鱼怎么办？

面向过程：

	1. 买鱼，买料
 	2. 杀鱼和清理，并且腌制
 	3. 放锅烧水
 	4. 把鱼放进去，开始蒸
 	5. 十分钟后开盖，把鱼端出来，浇汁

面向过程中想完成这个愿望，需要一步一步的去执行。

面向对象：

​	需要一个对象：大厨

​	告诉大厨，我想吃清蒸鱼

面向对象就是调用对象去解决问题，具体的对象如何去解决呢？

大厨这个对象肯定也是一步步完成。但是对于我来说，就是调用了对象。而对象去完成这个过程。

当然了最终面向对象中是有面向过程的体现的。





### 面向过程和面向对象的区别和优缺点？



#### 一，面向过程

>  面向过程的核心是过程，过程就是指解决问题的步骤。

优缺点：

+ 优点： 将负责的问题流程化，进而实现简答化
+ 缺点：扩展性差（更新，维护，迭代）

总结：在去完成一些简单的程序时，可以使用面向过程去解决。但是如果有复杂的程序或任务，而且需要不断的进行迭代和维护，那么肯定是优先选择面向对象的编程思想



#### 二，面向对象

> 面向对象的核心是对象，是一个特征和功能的综合体

优缺点：

+ 优点：可扩展性高
+ 缺点：编程复杂度相对面向过程高一些。指的是计算机在执行面向对象的程序时的性能表现



### 后面如何去学习面向对象编程？

1. 理解面向对象编程的思想
2. 学习面向对象编程的语法



### 认识类与对象

类：类是对象的一个抽象的概念

对象（实例）：对象就是由类的创建的实例

类和对象的关系就是 模具与铸件的关系

1. 类是由对象总结而来的，总结的这个过程叫做抽象
2. 对象是由类具体实施出来的，这个过程叫做实例化

如果你现在有点迷糊，那你想一想，

+ 水果是一个对象还是一个类？
+ 汽车是一个对象还是一个类？
+ 手机是一个对象还是一个类？

再来想一个问题，我现在给大家上课，用的是一个笔记本电脑，

请问我当前正在使用的这个笔记本电脑是一个对象还是一个类？

笔记本电脑特征：金属外壳，优美的外观

笔记本电脑功能：给大家制作课程，编辑代码，听音乐。。。



## 面向对象编程的基本实现

> 如果需要实例一个对象，那么需要先抽象一个类

例如需要创建一个汽车对象

首先需要抽象一个汽车类：汽车类就相当于一个设计图纸一样。

由这个设计图纸去创建(实例)出来的真实汽车就是一个对象



如何创建一个类，通过class关键字来定义一个类

示例：

```python
# 定义一个汽车的类
class Cart():
    pass
    
'''
类名的书写规范，建议使用驼峰命名法
    大驼峰：MyCar XiaoMi
    小驼峰：myCar xiaoMi
'''
```

类中需要声明什么内容？

```
一个类有特征和功能两个内容组成：
    特征就是一个描述：颜色：白色，品牌：奥迪，排量：2.4 。。。
    功能就是一个能力：拉货，带美女兜风。。。。

    特征在编程中就是一个变量，在类中称为 属性
    功能在编程中就是一个函数，在类中称为 方法

类中属性一般定义在前面，方法定义在后面
```

示例：

```python
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
```

如何通过类实例化对象并使用？

```python
# 如何去使用这个类？
# 通过类实例化一个对象
aodiobj =  Cart()

# print(aodiobj,type(aodiobj))
# <__main__.Cart object at 0x106f08550> <class '__main__.Cart'>

# 调用对象的方法
aodiobj.bamei()

# 获取对象的属性
print(aodiobj.brand)
```

---



### 成员属性和成员方法的操作

#### 对象操作成员

```
成员属性：
  访问：  对象.成员属性名
  修改：  对象.成员属性名法 = 新值。（此时等于给这个对象创建了一个自己的属性）
  添加：  对象.新成员属性 = 值 (此时是给这个对象自己新建了一个属性)
  删除：  del 对象.成员属性 (注意：只能删除这个对象自己的属性)
  
成员方法：
  访问：  对象.成员方法名()
  修改：  对象.成员方法名 = func（此时等于给这个对象创建了一个自己的方法）
  添加：  对象.方法名 = func (此时是给这个对象自己新建了一个方法)
  删除：  del 对象.方法名 (注意：只能删除这个对象自己的方法)
```

#### 类操作成员（不推荐）

```
成员属性：
  访问：  类名.成员属性名
  修改：  类名.成员属性名法 = 新值。（此时通过这个类创建的对象都具有这个属性）
  添加：  类名.新成员属性 = 值 (此时通过这个类创建的对象都具有这个属性)
  删除：  del 类名.成员属性 (注意：删除这个类的属性后，这个类创建的对象也没有这几个属性了)
  
成员方法：
  访问：  类名.成员方法名()
  修改：  类名.成员方法名 = func（此时通过类创建的对象都被修改）
  添加：  类名.方法名 = func (此时通过类创建的对象都被修改)
  删除：  del 类名.方法名 (注意：此时通过类创建的对象都被修改)
```

#### 总结

+ 一个类可以实例化出多个对象，每个对象在内存中都独立存在的
+ 当通过类实例化对象时，并不会把类中的成员复制一份给对象，而去给对象了一个引用
+ 访问对象成员的时候，如果对象自己没有这个成员，对象会向实例化它的类去查找
+ 对象成员的添加和修改，都只会影响当前对象自己，不会影响类和其它对象
+ 删除对象的成员时，必须是该对象自己具备的成员才可以，不能删除类中引用的成员
+ 对类的成员操作，会影响通过这个类创建的对象，包括之前创建的。

----



### 成员方法中的self

+ self在方法中只是一个形参，并不是关键字
+ self 单词本身的意思  自己
+ self 在类的方法中 代表 当前这个对象
+ self 代表调用这个方法的对象,谁调用了这个方法，self就代表谁
+ self 就可以在类的内部代替对象进行各种操作

### 方法的分类

+ 含有self或者可以接受对象作为参数的方法： 非绑定类方法
+ 不含self或者不能接受对象作为参数的方法：绑定类方法

非绑定类方法，可以使用对象去访问

绑定类方法，只能通过类去访问

----

### 魔术方法

> 魔术方法也和普通方法一样都是类中定义的成员方法
> 魔术方法不需要去手动调用的，魔术方法会在某种情况下，自动触发（自动执行）
> 魔术方法还有一个比较特殊的地方：就是多数的魔术方法 前后都有两个连续的下划线
> 魔术方法不是我们自己定义的，而是系统定义好的，我们来使用

#### `__init__`初始化方法

```
__init__ 初始化方法
    触发机制：在通过类实例化对象后，自动触发的一个方法
    作用：   可以在对象实例化后完成对象的初始化（属性的赋值，方法的调用。。）
    应用场景： 文件的打开，数据的获取。。。干活前的一些准备功能。。。
```



#### `__del__`析构方法

```
__del__ 析构方法
    触发机制：析构方法会在对象被销毁时自动触发
    作用：关闭一些开发的资源
    注意：是对象被销毁时触发了析构方法，而不是析构方法销毁了对象

对象会在哪些情况下被销毁？
    1。 当程序执行完毕，内存中所有的资源都会被销毁释放
    2。 使用 del 删除时
    3。 对象没有被引用时，会自动销毁
```

示例：

> 定义一个类，完成一个日志的记录
>     调用这个对象的时候，传递一个日志信息
>     这个对象会创建一个文件，开始写入，并在最后关闭这个文件

```python
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
```
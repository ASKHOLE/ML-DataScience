# 单入口程序

# 单入口文件是作为程序直接被运行的唯一文件，其它都是作为模块或包，被导入单入口中去执行
'''
ATM/
|---- main.py  # 当前程序的主入口文件，单入口文件,唯一直接运行的文件
|---- package/ # 主要程序模块包
|---- |----- __init__.py  # 包的初始化文件
|---- |----- View.py      # 视图函数模块
|---- |----- Controller.py# 控制器模块
|---- |----- Card.py      # 银行卡模块
|---- |----- User.py      # 用户模块
|---- databases/ # 数据存储文件夹
|---- |---- user.txt
|---- |---- user_id_card.txt

main是程序的主入口文件，会被直接作为主程序运行，所以main.py文件中必须使用 绝对导入 方式
'''





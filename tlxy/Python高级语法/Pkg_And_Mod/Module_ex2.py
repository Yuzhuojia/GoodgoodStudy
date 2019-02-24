import Module_ex1

stu = Module_ex1.Student("xiaojing", 19)

stu.say()

Module_ex1.sayHello()

'''
借助于importlib可以导入名称以数字开头的模块

import importlib
# 导入一个名称叫01的模块并把导入模块赋值给tuling
tuling = importlib.import_module("01)

'''
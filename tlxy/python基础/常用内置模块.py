# 数学模块
import math
import keyword

'''
# 查看关键字
print(keyword.kwlist)

# math.ceil() 向上取整
print(math.ceil(5.1))

# math.floor() 向下取整
print(math.floor(5.9))

# math.sqrt() 开平方,返回float
print(math.sqrt(100))

# math.pow() 幂运算,返回浮点数
print(math.pow(4,5))
print(4**5)

# math.fabs() 求绝对值,返回浮点数
print(math.fabs(-1))
# abs() Python内置函数,获取绝对值
print(abs(-8.0))

# round() 四舍五入,Python内置函数
print(round(4.1))
print(round(5.5))

# math.fsum() 求和,返回浮点数
# sum() Python内置函数
print(math.fsum([1,2,3,4]))
print(sum([1,2,3,4]))

# math.modf() 将一个浮点数拆分为整数部分和小数部分,返回一个元组
print(math.modf(4.5))
print(math.modf(0))
print(math.modf(3))

# math.copysign() 将第二个数的符合传递给第一个数,返回第一个数的浮点数类型
print(math.copysign(1, -2))
'''

# 随机数模块
import random

# for i in range(10):
    # random() 获取0-1之间的随机小数,[0,1)
    # print(random.random())
    # randint(a,b) 随机获取a-b之间的整数值,[a,b]
    # print(random.randint(1,8))
    # uniform() 随机获取指定范围内的浮点值
    # print(random.uniform(1, 9))
    # random.randrange(a,b,[c]) 获取a-b之间步距为c的随机值
    # print(random.randrange(1,9))

'''
# choice() 随机获取列表中的值
l = [4, 7, 68, 909, 8]
print(random.choice(l))

# shuffle() 随机打乱序列,返回值是None
random.shuffle(l)
print(l)

# 字符转换为unicode编码
print(ord('A'))
# 编码转换为字符
print(chr(97))
'''

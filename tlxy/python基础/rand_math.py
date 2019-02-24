import random
import math

'''
输入一个三位数,与程序随机数比较大小
如果大于程序的随机数,分别输出这个三位数的个位,十位,百位
如果等于程序随机数,则提示中奖,记100分
否则,将120个字符输入到列表(每一个字符串的长度为12,前4个是字母,后8个是数字)
'''

# 先定义生成文本的函数
def autoPrnt():
    # 定义一个空字符串,用于拼接字符
    str_num = ''
    # 生成前4个随机字母,用随机值生成ASCII码
    for i in range(4):
        letter = random.randrange(97, 123)
        str_num = str_num + chr(letter)

    # 随机生成后面8个数字
    for i in range(8):
        number = random.randrange(0, 10)
        str_num = str_num + str(number)

    return str_num

num = input("请输入一个三位数:")
r_num = random.randrange(100, 1000)
# 检测输入是否为纯数字并且是一个三位数
if num.isdigit() and 100 <= int(num) <= 999:
    num = int(num)
    if num > r_num:
        hun = num//100
        dec = num%100//10
        unit = num%10
        print("这个数的百位是{},十位是{},个位是{}.".format(hun, dec, unit))
    elif num == r_num:
        print("Good Luck!")
    else:
        lst = []
        # 生成10行
        for i in range(10):
            line = autoPrnt()
            # 执行文件存入操作
            lst.append(line)
        print(lst)
else:
    print("请按规定输入")

# 程序入口
if __name__ == '__main__':  # 调试代码
    # 在本身模块中,__name__ == __main__ ,当第三方导入时,__name__ == 模块本身(文件名字)
    print(__name__)
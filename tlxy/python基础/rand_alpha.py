# 打印字母A
def A():
    # 控制行
    for i in range(5):
        for k in range(5-i):
            print(' ', end='')
        # 控制列
        for j in range(i+1):
            if i == 0 or i == 3 or j == 0 or j == i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# 打印字母B
for i in range(5):
    for k in range(5-i):
        print(' ', end='')
    # 控制列
    for j in range(i+1):
        if i == 0 or i == 3 or j == 0 or j == i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

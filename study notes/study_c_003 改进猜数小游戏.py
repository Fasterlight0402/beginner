"""
改进猜数小游戏，增加功能
1、猜错给提示，大了还是小了
2、多给几次机会
3、每次运行程序，答案应该是随机的
"""


import random                         # 导入随机数模块
answer=random.randint(1,10)      # 生成1-10之间的一个随机整数
count = 3
while count>=0:
    temp2 = input('本关考验你猜整数的能力,输入一个整数:')
    guess = int(temp2)
    if guess == answer:
        print('\t你过关！\n一阵响亮的bgm。\n')
        count = 0
        break                                          # break  语句 跳出循环
    else:
        if guess > answer:                                 # 嵌套型结构的 if  else  后面记得加:     并且注意缩进
            print(f'回答偏大，该罚！\n石头砸中了你的脑袋。\n你还剩{count-1}次机会\n')
        else:
            print(f'回答偏小，该罚！\n石头砸中了你的脑袋。\n你还剩{count-1}次机会\n')
    count -= 1
if count == 0:
    print('就这么结束了么……\n')
else:
    print('你的脑袋无法承受更多石头，就这么结束了么……\n')


'''
循环结构学习
① while 循环语句
  while 1<2:          1<2 为 True，循环会一直持续下去
      print('xxxx')  

② break 语句
    跳出一层的循环语句
'''

'''
模块可用 用 import 

random.random()                         0-1之间的一个小数
random.randint(1,10)                   1-10之间的一个整数
random.uniform(1,10)                   1-10之间的一个小数
random.choice(1,2,3,4,5,6,7,8,9,10)    列表中随机选择一个
random.sample(range(1,10),3)           列表中随即选择3个
random.shuffle(列表)                    打乱列表

'''
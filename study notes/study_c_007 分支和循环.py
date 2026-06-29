#分支和循环   branch and loop

# 分支结构
"""
① 判断一个条件，如果成立就执行某条语句或者某个代码块

if 3<5:
    print('212')  # 缩进决定了从属关系

print('121')


② 判断成立则执行一，判断条件不成立则执行二

if 3<5:
    print('212')
else:
    print('121')

③ 判断多个条件，如果一个不成立则判断第二个，如果第二个不成立，则判断第三个……
if 3<5:
    print('212')
elif 3<5:
    print('212')
elif:
    print('121')  # 最后一个条件也可以改成 else，或者不成立的方式用else来表示

"""

"""
④  条件成立时执行 if 条件condition else 条件不成立时执行
传统形式
age=16
if age<18:
    print('抱歉')
else
    print('欢迎')

用④的形式

print('抱歉') if age<18 else print('欢迎')

small= a if a<b else b

math=66
level = ('D' if 0<= math < 60 else
         'C' if 60<= math < 80 else
         'B' if 80<= math < 90 else
         'A' if 90<= math < 100 else
         'S' if math=100 else
         '请输入0~100之间的分数^_^' )
print(level)
"""

"""
⑤ 分支结构的嵌套
age = 18
isMale = True 
if age <= 18:
    print('抱歉，未满十八岁禁止访问。')
else
    if isMale:
        print('请随意')
    else
        print('抱歉，仅供男士。')

"""

"""
循环语句 while 循环

while 条件：
    执行程序

love = 'yes'
while love == 'yes':
    love = input('今天你还爱我么？')

死循环，开始就不会结束  可以被操控
break 

"""
while True:
    answer= input('可以停下来了么？')
    if answer == 'yes':
        break                 # 循环体遇到break会直接打破，回到while的同一缩进处的下一段
    print('受不了啦!')

"""
continue  

i=0
while i<10:
    i+=1
    if i%2==0:
        continue   # 跳出本次循环，再会回到while的开头
    print(i)

"""
i=0
while i <10:
    i +=1
    if i %2==0:
        continue   # 跳出本次循环，再会回到while的开头  也就是i为奇数则print  ； i为偶数则 不print 直接返回开头
    print(i)

'''
day = 1
while day<=7:
    answer = input('今天有没有好好起飞？')
    if answer ！= 'yes':     
        break
    day += 1
else
    print('Bravo！')

'''

"""
循环嵌套
"""

s: int=1
while s<=9:
    j = 1
    k = j * s
    while j<=s:                        # 当j开始大于i时，才跳出二层while，去到一层while
        print(f'{s}*{j}={k}',end=' ')  # end= 代表本循环内的下一次打印不换行，
        j += 1
        
    print()
    s+=1

"""
for 变量 in 可迭代对象：  # 迭代就大概是遍历一遍的意思
    执行程序

"""
for each in '114514':
    print(each)

nu=0
while nu<len('114514'):  #len() 用于获取一个对象的长度，'114514'有6个数字，长度为6
    print('114514'[nu])  #依次访问并打印每个字符中的一个
    nu+=1

# 用for循环计算等差数列求和
# 长长用到的好兄弟，range（），帮助形成一个数字序列，数列形成玩意儿
# range（末），从0开始到的整数数列，到末这个数字结束，但不会生成末
# range（首，末），   不包含末
# range（首，末，公差）

nu01=0
for nu02 in range(1,101,1):
    nu01+=nu02
print(nu01)

# 找素数程序
for nu04 in range(2,31,1):
    for nu05 in range(2,nu04,1):
        if nu04 % nu05==0:
            print(f'{nu04}不是素数')
            break
    else:
        print(f'{nu04}是素数',end='')

oo=2%2
print(oo)

# 找2-50之间的所有素数程序的改进版
su,zhi=[],[]
for i in range(2,51,1):
    for j in range(2,i,1):
        if i%j==0:
            zhi.append(i)
            break
    else:
        su.append(i)
print('2-50之间所有的素数是：',su,'\n','所有的质数是：',zhi)

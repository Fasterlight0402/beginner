# 字符串(1) 作业
#1
"-520".zfill(10) # 用0填充-520的左侧，负号放最左边，一共10个字符宽度

#2
# 请问 "-520".zfill(10) 和 "-520".rjust(10, "0") 的执行结果一样吗？
# 不一样,zfill(10)会自动识别负号，rjust()不会,负号还在520旁边

print("-520".zfill(10),"-520".rjust(10, "0"))

#3
# 请问下面代码执行的结果是？
# >>> "-520".center(6, "0").zfill(10)
# 00000-5200

print("-520".center(6, "0").zfill(10))

#4
# 请问下面代码执行的结果是？
# >>> "I love FishC".swapcase()[::-1]

print("I love FishC".swapcase()[::-1])
# 大小写反转 .swapcase()  倒顺序输出[::-1]

#5
# 请使用一行代码来检测列表中的每个元素是否为回文数，并返回一个结果为回文数构成的列表。
# 提供的列表：["123", "33211", "12321", "13531", "112233"]
# 返回的结果：['12321', '13531']

q=["123", "33211", "12321", "13531", "112233"]
w=[i for i in q if i==i[::-1]]
print(w)

#动动手0
# 请按照以下规则整理一个给定的字符串 s
# 一个整理好的字符串中，两个相邻字符 s[j] 和 s[j+1]，其中 0 <= j <= s.length - 2，要满足如下条件：
# 若 s[j] 是小写字符，则 s[j+1] 不可以是相同的大写字符
# 若 s[j] 是大写字符，则 s[j+1] 不可以是相同的小写字符
# 如果 s[j] 和 s[j+1] 满足以上两个条件，则将它们一并删除
# 例如"FishCcCode" -> "FishCode"
#    "AbBaACc" -> "AaACc" -> "AaA" -> "A"
#    "AABaAbCc" -> "AABbCc" -> "AACc" -> "AA"

e="FishCcCode"
r=[j for i in e
     for j in i]  # 提取

t=[]
for i in range(len(r)-1):
    if r[i].isupper():
        if r[i+1].upper()!=r[i]:  #若大写，则后一个的大写不等于自己
            t.extend(r[i])

    else:
        if r[i+1].lower()!=r[i]:  #其他就是小写，则后一个的小写不等于自己
            t.extend(r[i])
t.extend(r[-1])                   #最后一个字母必有

y=''.join(t)   # 列表中元素全部加入成一个字符串
print(y)

"""
参考答案
s = input("请输入一个字符串：")
    
res = []
for each in s:
    if res and res[-1].lower() == each.lower() and res[-1] != each:
        res.pop()
    else:
        res.append(each)
    
for each in res:
    print(each, end='')

"""


#动动手1
# 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母，奇数下标为正整数
# 编写代码，将奇数下标的数字转换为相对于上一个字母偏移后的字母
# 比如 s = "a1b2c3" 转换后的结果是 "abbdcf"（a1 -> ab，b2 -> bd，c3 -> cf）
# s = "x7y8z9" 转换后的结果是 "xeygzi"（遇到最后字母 z ，则从 a 继续计算偏移）

letter=['a','b','c','d','e',
        'f','g','h','i','j',
        'k','l','m','n','o',
        'p','q','r','s','t',
        'u','v','w','x','y','z']

s = "x7y8z9"
list_1= [j for i in s
          for j in i]

list_2=[letter.index(list_1[i]) for i in range(len(list_1)) if i%2==0]  # 找出s列表中字母对应的字母表中的序号数

num=[]
for i in range(len(list_1)):
    if i%2==0:
        num.extend(list_1[i])           # list_1的字母都在偶数序号，不用动
    else:
        l=int((i-1)/2)                  # list_1 的1 对应 list_2 的0， 3对应1，5对应2
        k=(int(list_1[i])+list_2[l])%26 # 两数相加后取余在letter中的序号
        num.extend(letter[k])
kl=''.join(num)
print(kl)

"""
s = input("请按规则输入一个字符串：")
    
length = len(s)
# 获取字母 a 的编码值
base = ord('a')
    
# 从第一个元素开始，每次迭代跳过一个元素
for i in range(0, length, 2):
    # ord(s[i]) - base 操作得到一个字母的偏移值，比如 b 就是 1
    # 跟 26 求余数的作用是防止溢出，循环计算偏移
    shift = chr((ord(s[i]) - base + int(s[i+1])) % 26 + base)
    print(s[i]+shift, end="")

"""
'//////////////////////////////////////////////////////////////////////////////////////'
# ord('a') 意思是得到a的计算机编码值
# chr(97)  意思是得到计算机编码为97的负号，就是a，整数只能在0到1114111中


# 字符串2 (2) 作业
# 0. 请问下面代码打印的结果是什么？
# >>> str1 = "xxxxx"
# >>> str1.count("xx")
# 2,5个x  xx出现了2次
str1 = "xxxxx"
print(str1.count("xx"))

# 1. 字符串的 find() 方法和 index() 方法同样是返回查找对象的下标值，那么它们之间的区别是
# find()找不到会返回-1，只适用字符串    index()找不到会报错，可以适用列表或字符串

# 2. 请问下面代码返回的值是什么？
# >>> x = "上海自来水来自海上"
# >>> x.rindex("来水来")
# 3

x = "上海自来水来自海上"
print(x.rindex("来水来"))  # 不能倒过来看需要查找的字符串


# 3. 请问下面代码执行的结果是 A 还是 B 抑或是 C 呢（为了你可以更容易地计数，下面使用 * 表示空格）？
# print(x)
# print(x.expandtabs(2))
# print(x.expandtabs(5))
# print(x.expandtabs(10))

'''
A
Hello****FishC
Hello**ishC
Hello*****FishC
Hello**********FishC

B
Hello***FishC
Hello*FishC
Hello*****FishC
Hello*****FishC

C
Hello***FishC
Hello*FishC
Hello*****FishC
Hello**********FishC
'''

# 4. 请问下面代码打印的结果是什么？
# >>> "I love FishC.com".translate(str.maketrans("ABCDEFG", "12345678"))
# 报错，定义的maketrans左右长度不一样

# 5. 请问下面代码打印的结果是什么？
# >>> "I love FishC.com".translate(str.maketrans("love", "1234", "love"))
# 忽略love 变成 I  FishC.cm

# 动动手：
# 0. 用户输入两个版本号 v1 和 v2，请编写代码比较它们，找出较新的版本。

# 科普：
# 版本号是由一个或多个修订号组成，各个修订号之间由点号（.）连接，
# 每个修订号由多位数字组成，例如 1.2.33 和 0.0.11 都是有效的版本号。
# 从左到右的顺序依次比较它们的修订号，点号（.）左侧的值要比右侧的权重大，即 0.1 要比 0.0.99 大。

v1=input('请输入第一个版本号，v1=')
v2=input('请输入第二个版本号，v2=')

sp_v1,sp_v2=v1.split('.'),v2.split('.')
zhang_v1=[j for i in sp_v1 for j in i]
zhang_v2=[j for i in sp_v2 for j in i]

cha=len(zhang_v1)-len(zhang_v2)

def math():
    num_1, num_2 = ''.join(zhang_v1), ''.join(zhang_v2)
    if num_1 > num_2:
        print('v1')
    elif num_1 == num_2:
        print('v1=v2')
    else:
        print('v2')

if cha==0:
    math()

elif cha>0:
    for i in range(abs(cha)):
        zhang_v2.append('0')
    math()

else:
    for i in range(abs(cha)):
        zhang_v1.append('0')
    math()


# 1. 编写一个加密程序，其实现原理是通过替换指定的字符进行加密，附加要求是实现密文逆向检测。
'''
参考答案
plain = input("请输入需要加密的明文：")
x = input("请输入需要替换的字符：")
y = input("请输入将要替换的字符：")
    
# 加密的代码
if len(x) != len(y):
    print("需要替换的字符数量必须跟将要替换的字符数量一致！")
else:
    cipher = plain.translate(str.maketrans(x, y))       # 这里目前都能看懂
    print("加密后的密文是：" + cipher)
    
# 检测冲突的代码
# flag 变量标志是否退出检测（只要找到一个冲突，就可以直接退出）
flag = 0
    
# 如果 x 中存在相同的字符，那么 y 对应下标的字符也应该是相同的
for each in x:
    if x.count(each) > 1 and flag == 0:
        i = x.find(each)
        last = y[i]
        while i != -1:
            if last != y[i]:
                print("由于替换字符出现冲突，该密文无法解密！")
                flag = -1
                break
    
            i = x.find(each, i+1)
    
# 如果 y 中存在相同的字符，那么 x 对应下标的字符也应该是相同的
for each in y:
    if y.count(each) > 1 and flag == 0:
        i = y.find(each)
        last = x[i]
        while i != -1:
            if last != x[i]:
                print("由于替换字符出现冲突，该密文无法解密！")
                flag = -1
                break
    
            i = y.find(each, i+1)

'''





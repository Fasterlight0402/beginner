#1
# 0. 请至少说出使用函数的两个显著优势？
#
# 省代码，方便阅读检查


# 1. 如果定义的函数不需要接收任何参数，可以不写小括号吗（像下面代码这样）？
# >>> def myfunc:
# ...     pass
# ...
# 不可以

# 2. 请问下面代码中，实参是什么？形参是什么？
# >>> def myfunc(x, y):
# ...     print(x + y)
# ...
# >>> a = 3
# >>> b = 5
# >>> myfunc(a, b)
# 8
#
# 实参a,b  形参 x,y


# 3. 如果在函数的定义中没有出现 return 语句，是否说明该函数没有返回值？
#
# 有返回值，None

# 4. 一个函数能够在同时返回多个值吗？
#
#   只能return一次

# 5. 请问下面代码，通过调用 funA() 函数，是否能够间接地调用到 funB() 函数，
# 从而打印出 "Hi~" 呢（注意它们定义的顺序，在定义 funA() 函数的时候，funB() 函数仍未定义）？
def funa():
    funb()
# ...
def funb():
    print("Hi~")
# ...
funa()
# # 这里是否会报错呢？
#
#  没报错，可以间接调用

# 6. 我们说函数是一个相对封闭的个体，那么函数是如何与外部通信的呢？
#
# 通过改变需要的实参


# 动动手：
# 0. 请编写一个实现【注册】和【登陆】功能的代码，这次要求将不同的功能封装成独立的函数。
# 程序要求如下：
# 编写 4 个函数分别用于获取用户指令（get_int()）、注册（register()）、登陆（login()）、MD5加密（encrypt()）
# 使用一个 Python 的字典作为数据库。
# 注册时需验证用户名是否已存在于数据库
# 登陆时需验证用户名和密码是否匹配
# 密码保存需使用 MD5 加密
# 题目要求：请先分别画出程序主结构、注册函数和登陆函数的流程图，再编写实现代码。


import hashlib
lib=dict()

# 获取用户指令
def get_int(com):
    if com=='1':register()
    else:login()

# 注册
def register():
    name=input('请输入用户名：')
    l=input('请输入密码：')
    lib[name]=encrypt(l)
    print('恭喜，注册成功~\n=====================')

# MD5加密
def encrypt(mm):
    mm_b=bytes(str(mm), "utf-8")
    mm_jm=hashlib.md5(mm_b).hexdigest()
    return str(mm_jm)

# 登录
def login():
    log_name=input('请输入用户名：')
    i=1
    while i==1:
        if log_name not in lib.keys():
            log_name=input('该用户不存在。\n请重新输入用户名：')
        else:
            log_mm=input('请输入密码：')
            while i==1:
                if encrypt(log_mm) not in lib.values():
                    log_mm=input('密码错误！\n请重新输入密码：')
                else:
                    print('恭喜，登录成功~\n=====================')
                    i=2
                    break

print('欢迎来到鱼C论坛~\n=====================')
go=True
while go:
    print('1.注册\n2.登录\n3.退出')
    k = input('请输入指令：')
    if k in ('1','2'):get_int(k)
    elif k =='3':
        print("=====================")
        break
    else:print('指令错误，请重新输入。')

'''
参考答案中的片段：
# 功能：模拟论坛登录
def login():
    name = input("请输入用户名：")
    while not(fishc_db.get(name)):          # 更简便的一种小循环写法，需要记住
        print("该用户名不存在。")
        name = input("请重新输入用户名：")

    passwd = input("请输入密码：")
    while fishc_db.get(name) != encrypt(passwd):
        print("密码错误！")
        passwd = input("请重新输入密码：")

    print("恭喜，登录成功~")

'''

#2
# 0. 如果一个函数要求传递位置参数，那么颠倒实参的顺序，肯定会报错，是吗？
#
#  也不一定。比如 min() 或者 max() 函数，参数顺序没有要求。


# 1. 默认参数跟关键字参数有啥区别？
#
#   默认参数在前面，关键词参数有=

# 2. 任何支持传递位置参数的函数，都可以使用关键字参数吗？
#
# 不是，只有/右边的可以支持关键词参数


# 3. 请问下面代码是否会报错，为什么？
# >>> def abc(a, /, b, c):
# ...     print(a, b, c)
# ...
# >>> abc(a=3, b=2, c=1)
# # 请问这里会报错吗？
#
# 会报错，参数a不支持关键词参数


# 4. 请问下面代码是否会报错，为什么？
def abc(a, *, b, c):
    print(a, b, c)

abc(c=3, b=2, a=1)
# # 请问这里会报错吗？
#
# 不会

# 5. 请问下面代码会打印什么内容，为什么？
# def myfunc(s, vt, o):
#    return "".join((o, vt, s))
#
# myfunc(o="我", "清蒸", "小甲鱼")
# # 请问这里会打印什么内容？
#
# 会error

# 动动手
# 0. 检测输入的中文字符串是否符合回文的语法，这个前面大家已经做过练习了，
# 不过这一次我们将要放宽，只要该字的拼音一样，字不相同没有关系，比如 “前任只认钱” 可以符合要求。
# 提示一：放宽要求后，只要文字的发音构成前后回文，即认定为符合要求。
# 提示二：将汉字转换为对应拼音的方法 -> https://fishc.com.cn/thread-213439-1-1.html
# 提示三：请将各个独立的功能封装为函数。

from xpinyin import Pinyin
p = Pinyin()

def pyh(u):
    pinyin = p.get_pinyin(u)
    pinyin_sp=pinyin.split('-')
    if pinyin_sp==pinyin_sp[::-1]:
        print(f'[{u}]是回文。')
    else:
        print(f'[{u}]不是回文。')

def words_much(l):
    length=len(l)
    while length<3:
        l=input('字数太少，请重新输入：')
        length=len(l)
    pyh(l)

words=input('请输入一段话：')
words_much(words)
'''
参考答案：
from xpinyin import Pinyin
    
def get_input():
    s = input("请输入一段话：")
    while len(s) == 1:
         s = input("字数太少，请重新输入：")
    return s
    
def get_py(s):
    p = Pinyin()
    s = p.get_pinyin(s)
    return s
    
def check_pd(s):
    l = s.split("-")    
    for i in range(len(l) // 2):
        if(l[i] != l[-i-1]):
            return False
    else:
        return True
    
s = get_input()
w = get_py(s)
if check_pd(w):
    print(f"[{s}]是回文。")
else:
    print(f"[{s}]不是回文。")
'''

# 1. 利用函数模拟创建【栈】的数据结构操作。
# 知识解读：
# 什么是栈呢？
# 栈是一种具有 FILO 特性的数据结构，即先放入的数据反而后取出。
# 比如有依次放入数据 250、251、255 到栈中，那么它们在栈中的存储结构如下：
# 255
# 251
# 250

# 此时，执行取出命令（pop），应该将最后压入栈的 255 优先取出，取出后栈中内容如下：
# 251
# 250

# 同样道理，如果我们执行压栈命令（push），将数据 520 压入栈中，那么执行后，栈中内容如下：
# 520
# 251
# 250

# 题目要求：将压栈命令（push）、取出命令（pop）和打印栈的功能分别封装为独立的函数。
# 程序实现如下：

zhan=list()
def push(x):
    zhan.append(x)
    print_zhan(zhan)

def pop():
    length=len(zhan)
    if length>0:
        print(f'{zhan[-1]}')
        zhan.pop()
        print_zhan(zhan)
    else:
        print('栈已空~')

def print_zhan(y):
    length=len(y)
    print('栈:')
    for i in range(length):
        print(str(y[length-i-1]))

run=True
while run:
    com=input('请输入指令(push/pop/top/exit):')
    if com=='push':
        j=input('请输入将要压入栈的值：')
        push(j)
    elif com=='pop':pop()
    elif com=='top':print(zhan[-1])
    else:run=False


'''
参考答案：
def print_s(s):
    print("栈：")
    for each in s[::-1]:
        print(each)

def push_s(s, v):
    s.append(v)

def pop_s(s):
    if len(s) == 0:
        return 0
    else:
        return s.pop()

s = []
ins = ""

while ins != "exit":                                   # 又学到一种循环语句
    ins = input("请输入指令（push/pop/top/exit）：")
    if ins == "push":
        v = input("请输入将要压入栈中的值：")
        push_s(s, v)
        print_s(s)
    if ins == "pop":
        v = pop_s(s)
        if v == 0:
            print("栈已空~")
        else:
            print(v)
            print_s(s)
    if ins == "top":
        if len(s) == 0:
            print("栈已空~")
        else:
            print(s[-1])

'''

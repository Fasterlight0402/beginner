#1
#   创建和调用函数
def myfunc():
    pass      # 函数体,很多时候先用pass占坑，然后再填充细节

myfunc()      # 在这调用函数

def myfunc():
    for i in range(3):
        print('i love functions')
myfunc()

#   函数的参数
#   通过函数的参数来进行功能的定制

def myfunc(name):           # ()里面添加了参数
    for i in range(3):
        print(f'i love {name}')
myfunc('python')            # ()里加啥，就打印啥


def myfunc(name,times):           # ()里面添加了多个参数
    for i in range(times):        # times用来改变次数
        print(f'i love {name}')
myfunc('python',5)


#   参数还分为   形式参数|实际参数
#       形参：函数定义时写的参数的名字，比如上面的 name  times
#       实参：是在调用函数的时候传递进去的值  比如上面'python' 和 5


#   函数的返回值
#   return语句  让自定义的函数实现返回

def div(x,y):
    if y==0:return '被除数不能为0！'
    # 只要执行return语句，函数就会立刻返回值，不会再执行其他语句
    else:return x/y
print(div(9,0))

#       如果函数没有return语句，函数会自己返回一个None值

#2
#   参数
#       位置参数
def yourfunc(s,vt,o):
    return ''.join((o,vt,s))
#   将传入的 s vt  o  顺序颠倒，并组成元组返回
#   在定义参数的时候，就已经把参数的位置定义下来了

print(yourfunc('狗','吃','肉'))

#       关键字参数，解决位置参数过多的情况
#       只要知道参数的名字就可以了

print(yourfunc(o='苹果',s='马',vt='咬了'))
# 参数的名字被定义了，func就不会按照固有顺序输出了

#       同时使用位置参数和关键词参数，需要注意位置参数必须在关键词参数之前
print(yourfunc('太子','狸猫',o='换'))


#       如果没有指定参数，函数则会使用默认参数
def hisfunc(s,vt,o='什么？'):
    return ''.join((o,vt,s))
print(hisfunc('今天','吃'))
#       由于o给了指定参数'什么？',所有调用函数没写 o时，就会给默认值，如果 o 写了，就会覆盖默认值
print(hisfunc('你','怎么','说'))
#       默认参数也是要放到位置参数的后面才行

#       python自带的函数，用help()可以查看功能  (x,/y)，/的左边只能写位置参数


#       可以利用 * 来只能使用关键词参数

def abc(a,*,b,c):
    print(a,b,c)
#   *左边既可以是位置参数，又可以是关键词参数
#   *右边只能是关键词参数

abc(1,b=2,c=3)


#3
#   参数
#       收集参数
#       有些函数并不确定参数的个数，比如print()
#       这种形参就叫做收集参数

#       用*args 可以表示有未知个数的参数，也就是收集参数

def herfunc(*args):
    print(args)
    print(f'有{len(args)}个参数')
    print(f'第二个参数是:{args[1]}')

#       实际上是把所有输入的 args 按照输入顺序，组成了一个元组
herfunc(1,1,4,5,1,4)


def itsfunc(*i,x,y):
    print(i,x,y)

itsfunc(1,1,4,5,x=1,y=4)  #  函数最后的x，y 必须赋予 关键词参数

#   可以用**构建能返回字典的函数
def minefunc(**i):
    print(i)

minefunc(a=1,b=2,c=3)

#   综合练习,位置参数+收集参数+字典形式参数
def ifunc(a,*b,**c):
    print(a,b,c)

ifunc(1,2,3,4,h=5)


#   解包参数
args=(1,2,3,4)
def yfunc(a,b,c,d):
    print(a,b,c,d)

yfunc(*args)  # 利用 * 进行元组tuple的解包，相当于 a=1,b=2,c=3,d=4

kwargs={'a':5,'b':6,'c':7,'d':8}
yfunc(**kwargs)    #     利用**可以将字典dict进行解包,注意数量要和函数的参数数量相同
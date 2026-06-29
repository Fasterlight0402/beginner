# 整数 int   长度不受限制

# 浮点数  float  0.1+0.2=0.3000000004  由于用二进制换算，并不百分百精确，
# 由于float不精确，所以需要用 decimal 模块
# decimal.Decimal('0.1')

# formatted_xxxx = format(xxxx,'.1e')
# 代表xxxx转为保留1位小数点的科学计数法形式

# 1+2j 代表复数 1为实部，2为虚部
# 可用complex（real，imag）构造复数   complex（3，4）=3+4j
# (1+2j).real 输出实部 1.0
# (1+2j).imga 输出虚部 2.0  输出的都是float

# 复数支持 共轭计算 .conjugate()      模 abs()


import decimal              #十进制小数
a=decimal.Decimal('0.1')
b=decimal.Decimal('0.2')
print(a+b)
c=decimal.Decimal('0.3')

number=10000000000
formatted_number=format(number,'.1e') #保留一位小数的
print(formatted_number)


# x+y       加法
# x-y       减法
# x*y       乘法
# x/y       除法
# x//y      整除，
# 舍去余数   如果是负数求，则按高斯函数，求比结果更小的整数

# x%y       求余数
# x=（x//y）*y+（x%y）  余数的符号与被除数想同， -3%2=1
# -x        相反数
# +x        x本身
# abs(x)        x的绝对值，也可求复数模长
# int(x)        将x转换为整数，整数字符转为整数，浮点数截掉小数输出整数
# int（9.99）=9     int（'100'）=100

# float(x)      将x转换为浮点数
# float('3.14')=3.14      float(10)=10.0     科学计数法   float('+1E3')=1000.0

# complex(real,imag)        构造复数

# (x+yj).conjugate()        返回x+yj的共轭复数  输出 x-yj

# divmod(x,y)       返回组（x//y,x%y） 组为（整除，求余数）

# pow(x,y)      计算x的y次方
# pow(x,y,z)        计算 （x**y）%5

# x**y       计算x的y次方

nu01=float('+1E3')
print(nu01)

# nu02=complex('1 + 2j') 加号中间不能加空格，不能转字符串类型
# print(nu02)

nu03=complex('1+2j')  # 不加空格就能正常使用
print(nu03)

nu04=pow(2,4,5)     #  先算2**4 = 16  ，再算16%5 = 1
print(nu04)


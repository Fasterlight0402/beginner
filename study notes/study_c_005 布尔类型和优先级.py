# 布尔类型
# bool()  用于返回一个布尔类型的值（True 或者 False）
#   bool 是 int 的子类，它不能够被进一步继承。
#       True==1  False==0
#   bool 的实例化对象只有 True 和 False 两个
#   bool('')空字符串的结果为 False   其他都为 True    bool（'假'）=True

# bool中定义为False的对象：
#   None和False,值为0的数字类型（0，0.0，Decimal（0）
#   Fraction(0,1)）Fraction(0,1)代表分子为0分母为1的有理数
#   空序列和空集 '',(),{},[],set(),range(0)


# 逻辑运算符
#   and     左右任意为True，结果是True
#       3 and 4 = 4，'123' and '456'='456'   在and中，同为真则输出后面一个


#   or      左右存在为True，结果是True
#       3 or 4 = 4     在or中，同为真 或 者左真右假 则输出左，  左假右真 或 同为假 则输出右

#   not     右边逻辑的否定
#       python中任何对象都能进行真值测试

nu01='123'and'456'
print(nu01)

# 短路逻辑和运算符优先级
#   （not 1）or(0 and 1)or(3 and 4)or(5 and 6 or 7)==4
#       直到第三个括号才第一次为真，第三个括号内为and，and两边为真则输出右边，or的后面就不看了，所以最后结果为4

#    and 和 or 都遵循短路逻辑
#        0 and 3==0 ； 0 or 3==3 ；3 or 4==3 ； 3 and 4==4
#       not 1 or 0 and 1 or 3 and 4 or 5 and 6 and 7 ==4


'''
                python 中的逻辑优先级 从低到高
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
lambda                                Lamb  表达式
if  else                              条件表达式
or                                    布尔 或
and                                   布尔 且
not x                                 布尔 非
in,not in,is,is not,<,<=,>,>=,!=,==      成员测试，同一性测试，比较
|                                      按位或
^                                      按位异或
&                                      按位与
<<,>>                                  位移
+,-                                    加法，减法
*,@,/,//,%                             乘法，矩阵乘法，除法，整除，取余数
+x,-x,~x                               正号，负号，按位翻转
**                                     指数
await x                                Await 表达式

x[index],x[index.index]                下标，切片
,x(arguments...),x attribute           函数调用，属性引用

(expressions...),[expressions...],     绑定或元组显示，列表显示
{key.value},{expressions...}           字典显示，集合显示
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''
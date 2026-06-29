# 流程图  Flowchart
#   表示算法或代码的流程框图组合，不同框代表不同的类型，每两个步骤间用箭头连接起来

"""
"""
'''
                Flowchart
            
→           连接          用于连接不同部分的代码
圆角矩形框    开始/结束      表示开始和结束
方角矩形框    过程          表示程序的过程
菱形狂       条件判断       表示条件判断，根据条件判断决定下一步走向
斜平行四边形    输入/输出     表示程序的输入/输出
----[         注释        用来补充某个步骤的额外信息
⟦⟧            函数        表示一个已在其他地方定义的程序（函数）
'''

nu01 = 1
nu02 = 0
while nu01 <= 20:
    nu02 += nu01
    nu01 += 1
print(nu02)  # 1-20 等差数列求和；效率不高；不如用等差数列求和公式


#   function 函数
#   摄氏度转化为华氏度函数和转化为开尔文温度

def tp_conversion(c ):
    f: float = float(c * 1.8 + 32)
    return f

def kr_conversion(c ):
    krw:float = float(c + 273.15)
    return krw

c = float(input('请输入摄氏度(℃)：'))
f = tp_conversion(c)
krw = kr_conversion(c)
f1 = round(f, 4)                    # round(f,4)保留f的2位小数，四舍五入
f2 = round(krw, 4)
print(f'转换的华氏度是：{f1}℉\n转换的开尔文温度是：{f2}k')

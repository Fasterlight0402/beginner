#  https://fishc.com.cn/thread-38339-1-1.html

# 0. 设计密码程序，有三次机会，若文本包含*则不算用掉机会
mm='FishC.com'
ct=3
while ct>0:
    sr = input('请输入秘密：*****')
    if sr==mm:
         print('密码准正确，进入程序······')
         break
    elif '*' in sr:
        print('密码中不能含有"*"号！您还有3次机会！请输入密码：')
        ct+=1        # 改成 continue
    else:
        print(f'密码输入错误！您还有{ct-1}次机会！')
    ct-=1

print()

#  求100~999之间所有的水仙数
#  如果一个3位数等于它各个位数的立方和，则被称为水仙花数

print('100~999之间的水仙数为：',end='')
for nu01 in range(100,1000,1):
    x = nu01 // 100
    b = (nu01-x*100)//10
    c = nu01%10
    if nu01 == x**3 + b**3 + c**3:
        print(nu01,end=' ')
print()
print()

# 三色球问题  3红  3黄  6绿  共12个球  从中摸出8个，求各种颜色搭配方式
for q in range(3,0,-1):
    for w in range(3,0,-1):
        for e in range(2,7,1):
            if q+w+e==8:
                print(f'{q}个红球，{w}个黄球，{e}个绿球')

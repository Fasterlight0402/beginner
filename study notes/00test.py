phone_book = {}

print("欢迎进入鱼C电话簿")
while True:
    ins = input("请输入命令（I:录入 / C:查询 / D:删除 / P:打印 / E:退出）：")

    if ins == 'I':
        print("\n-- 录入模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                print("该姓名已录入，手机号码是：", phone_book[name])
                if input("请问是否修改(Y/N)：") == 'Y':
                    phone = input("请输入新的手机号码：")
                    while not phone.isnumeric() or len(phone) != 11:
                        phone = input("输入不合法，请重新输入：")
                else:
                    phone = phone_book[name]
            else:
                phone = input("请输入手机号码：")                       # 这里input 了 phone
                while not phone.isnumeric() or len(phone) != 11:        # 进行判断，phone不合法就循环
                    phone = input("输入不合法，请重新输入：")   # 这里再次 input 了 phone，phone又被定义了一遍，实现小循环
            phone_book[name] = phone
            if input("是否继续录入(Y/N)：") != 'Y':    # 原来 input 和 if 可以放一句中，以后Y/N 就这样写
                print()
                break

    elif ins == 'C':
        print("\n-- 查询模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                print(name, phone_book[name], sep="：")  # sep=':'意思是print()中的多个要素，用： 分开
            if input("是否继续查询(Y/N)：") != 'Y':  # 这里直接不回答Y就是退出小循环，回到大循环，省去continue了
                print()
                break

    elif ins == 'D':
        print("\n-- 删除模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                phone_book.pop(name)
            if input("是否继续删除(Y/N)：") != 'Y':
                print()
                break

    elif ins == 'P':
        print("\n-- 打印模式 --")
        for each in phone_book:
            print(each, phone_book[each], sep="：")
        print()

    elif ins == 'E':
        break
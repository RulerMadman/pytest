"""
    模拟银行管理系统
    功能菜单
        1. 开户
        2. 存款
        3. 取款
        4. 转账
        5. 查询
        6. 退出
"""
import getpass
MENU = {
    "create_account":"开户",
    "save_money":"存款",
    "withdraw_money":"取款",
    "transfer_money":"转账",
    "query_account":"查询",
    "exit_system":"退出"
    }
CARDIDS = "6666"
CARDNUM = "11111"
CARDIDE = "0000"
CARD = []
STATUS = {"001":"非法访问","002":"密码错误","003":"卡号不存在","004":"余额不足","005":"撤销操作"}

def menu(*args,**kwargs):
    i = 1
    str = f"请选择功能：\n"
    for key,value in MENU.items():
        str += f"{i}.{value}\n"
        i += 1
    return str

def create_account(*args,**kwargs):
    global CARDNUM
    name = input("请输入您的姓名：")
    password = getpass.getpass("请输入您的密码：")
    money = float(input("请输入您的存款金额："))
    ID = CARDIDS + CARDNUM + CARDIDE
    CARD.append({"id":ID,"name":name,"password":password,"money":money})
    CARDNUM = str(int(CARDNUM) + 1)
    return True

def update_money(*args,**kwargs):
    if args[0] == 1:
        k = "存"
    elif args[0] == 0:
        k = "取"
    else:
        return STATUS["001"]    #001错误代码表示非法访问
    index = check_account()
    if index != "":
        price = float(input(f"请输入您要{k}款的金额："))
        if args[0] == 1:
            index["money"] += price
        elif args[0] == 0:
            if index["money"] >= price:
                index["money"] -= price
            else:
                return STATUS["004"]    #004错误代码表示余额不足
            index["money"] -= price
        else:
            return STATUS["001"]    #001错误代码表示非法访问
        return price
    
def transfer_money(*args,**kwargs):
    index = check_account()
    if index != "":
        otherid = input("请输入您要转账的卡号：")
        index2 = check_account(otherid)
        if index2 != "":
            price = float(input("请输入您要转账的金额："))
            print(f"核对对方信息与转账金额：{index2['name']}的卡号{index2['id']}，您要转账{price}元")
            reok = input(f"请确认转账信息是否正确（Y/N）：")
            if reok.upper() == "Y":
                if index["money"] >= price:
                    index["money"] -= price
                    index2["money"] += price
                    return True
                else:
                    return STATUS["004"]    #004错误代码表示余额不足
            else:
                return STATUS["005"]    #005错误代码表示撤销操作

def check_account(*args,**kwargs):
    if args[0] == "":
        cardid = input("请输入您的卡号：")
    else:
        cardid = args[0]
    for _ in CARD:
        if _["id"] == cardid:
            if args[0] == "":
                password = getpass.getpass("请输入您的密码：")
                if _["password"] == password:
                    return _
                return STATUS["002"]    #002错误代码表示密码错误
            return _
        return STATUS["003"]    #003错误代码表示卡号不存在

#主函数
if __name__ == '__main__':
    while True:
        print(menu())
        choice = input("请输入您的选择：")
        if choice == "1":
            "开户成功" if create_account() else "开户失败"
        elif choice == "2":
            re = update_money(1)
            print(f"存款成功，您存入的金额为{re}元") if type(re)!= str else print(re)
        elif choice == "3":
            re = update_money(0)
            print(f"取款成功，您取款的金额为{re}元") if type(re)!= str else print(re)
        elif choice == "4":
            re = transfer_money()
            print("转账成功") if type(re)!= str else print(re)
        elif choice == "5":
            print(check_account())
        elif choice == "6":
            exit()
        else:
            print(STATUS["001"])    #001错误代码表示非法访问
    else:
        print(STATUS["001"])    #001错误代码表示非法访问
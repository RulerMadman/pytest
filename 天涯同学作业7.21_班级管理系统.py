MENU = {'check_results' : '查询成绩','Modify_grades' : '修改成绩','Query_ranking':'查询排名','Add_grades':'添加成绩','register':'注册账号','q':'退出'}
i = 1
Account_library = []
Guess = [{'小明':{'数学':90,'语文':80,'英语':100},'小红':{'数学':88,'语文':100,'英语':90}}]

class Login_Verification(user,passwrod):  #类111111
    def __init__(self):
        self.user = user
        self.password = passwrod
    def user_operate(self):  #账号密码存储
        self.user_list = [{'小明': {'账号':'qwerty','密码':'password'},'小红': {'账号':'qwertt','密码':'123456'},'王老师': {'账号':'adminasd','密码':'000password'}}]
    def login(self):    #登录系统
        for i in Account_library:
            if self.user in i.keys():
                if self.password ==i.values():
                    if self.user[:5] == admin:
                        return 'admin_user'
                    else:
                        print('这是学生账号')
                else:print('密码不正确')
            else:
                judge = input('账号不存在，是否需要新注册，是/Y，退出/q:').upper()
                if judge == 'Y':
                    return self.register()
                elif judge == 'Q':
                    break
                else:
                    print('输入错误，程序结束')
                    break
    def guess(self,*args,**kwargs):    #查询成绩
        for i in Guess:
            print(f'{args}同学的成绩是{i[args]}')
    def register(self,*args,**kwargs):               #注册账号
        self.register_user = input('请输入你的名字:')
        self.register_qwerty = input('请输入你要注册的账号:')
        self.register_password = input('请输入你要注册的密码:')
        for i in self.user_list:
            for c in i.values():
                if register_user in c:
                    self.register(self)
                else:
                    self.user_list[self.register_user] = {'qwerty':self.register_qwerty,'password':self.register_password}
                    return self.login()

    def average(self, *args, **kwargs):  #查询平均分
        mathematics = []
        chinese = []
        english = []
        for i in Guess:
            print(f'{args}同学的成绩是{i[args]}')
            a = [mathematics.append(c['数学']) for c in i.values()]
            b = [chinese.append(c['语文']) for c in i.values()]
            c = [english.append(c['英语']) for c in i.values()]
        self.mathematics = mathematics = sum(mathematics) / len(mathematics)
        self.chinese = chinese = sum(chinese) / len(chinese)
        self.english = english = sum(english) / len(english)
    def operate(self,*args,**kwargs):    #执行菜单操作
        if args[0] == '1':
            if self.user == 'admin_user':
                class_mate = input('请输入你要查询成绩的同学姓名:')
                self.guess(class_mate)
            else:
                for i in user_list:
                    for x,y in i.items():
                        if y['账号'] == self.user:
                            return self.guess(x)
        elif args[0] == '2':
            if self.user == 'admin_user':
                self.mod_guess()
            else:print('对不起，你没有修改权限')
        elif args[0] == '3':
            self.lst_ranking()
        elif args[0] == '4':
            if self.user == 'admin_user':
                self.add_guess()
            else:print('对不起，你没有添加权限')
        elif args[0] == '5':
            self.register()
        elif args[0] == '6' or args[0] == 'Q':
            break
    def lst_ranking(self,*args,**kwargs):    #查询排名
        a = 1
        for i in Guess:
            for c, d in i.items():
                print(f'第{a}名同学的成绩是{c},他的名字叫{d.values()}')
    def add_guess(self,*args,**kwargs): #添加成绩
        global Guess
        add_name = input('请输入你要添加成绩的同学姓名:')
        add_object = input('请输入你要添加成绩的科目:')
        add_mark = input('请输入你要添加的成绩:')
        Guess[add_name] = {add_object:add_mark}
    def mod_guess(self,*args,**kwargs): #修改成绩
        global Guess
        mod_name = input('请输入你要修改成绩的同学姓名:')
        mod_object = input('请输入你要修改成绩的科目:')
        mod_mark = input('请输入你要修改的成绩:')
        Guess[mod_name] = {mod_object: mod_mark}
while True:
    user = input('请输入账号:')
    password = input('请输入密码:')
    Login_Verification(user,password)
    Login_Verification.login(self)
    for key, value in MENU.items():
        print(f'{i}.{value}')
        i += 1
    str = f'请输入你要进行的操作:'
    if str == '1':
        Login_Verification.operate('1')
    elif str == '2':
        Login_Verification.operate('2')
    elif str == '3':
        Login_Verification.operate('3')
    elif str == '4':
        Login_Verification.operate('4')
    elif str == '5':
        Login_Verification.operate('5')
    elif str == 'q':
        break
    else:print('非法输入')

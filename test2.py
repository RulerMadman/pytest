class Card():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__password = 0
    def get_user(self):      #打印用户信息(name和age)
        print(f'当前用户是{self.name}年龄是{self.age}')

    def __set_password(self,new_password):   # 修改密码使用
        self.__password = new_password
        print(f'新密码是:{self.__password}')

    def setpassword(self, aa_name,aa_password):          #验证用户名，如果用户名正确，则修改密码
        if aa_name == self.name:
            self.__set_password(aa_password)
            return True
        else:
            return False

use = Card('bingbing',18)
while True:
    aa_name = input('请输入用户名:')
    aa_password = input('请输入密码:')
    if use.setpassword(aa_name,aa_password):
        print('密码修改成功')
        break
    else:
        print('用户名错误')


import hashlib
import pymysql
import getpass

class DatabaseManager:
    def __init__(self, config):
        # 在传递给pymysql.connect（）的参数中排除“salt”
        self.config = {key: value for key, value in config.items() if key != 'salt'}
        self.connection = None
        self.salt = config.get('salt')  # 盐分开存放

    def connect(self):
        self.connection = pymysql.connect(**self.config)

    def _hash_password(self, password):
        # 使用存储的盐来哈希密码
        combined = f"{password}{self.salt}".encode('utf-8')
        hashed = hashlib.md5(combined).hexdigest()
        return hashed
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def _hash_password(self, password, salt):
        # 将密码和盐结合起来，然后用 MD5 哈希
        combined = f"{password}{salt}".encode('utf-8')
        hashed = hashlib.md5(combined).hexdigest()
        return hashed

    def check_password(self, username, password):
        if not self.connection:
            raise RuntimeError("未建立数据库连接.")
        
        hashed_password = self._hash_password(password, self.salt)
        
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM user WHERE name=%s AND password=%s"
            cursor.execute(query, (username, hashed_password))
            result = cursor.fetchone()
            return result  # 直接返回查询结果


class UserAuthenticator:
    def __init__(self, db_config):
        # 创建 DatabaseManager 实例时确保包含“salt”
        self.db_manager = DatabaseManager(db_config)
        self.connected = False

    def connect(self):
        self.db_manager.connect()
        self.connected = True

    def disconnect(self):
        self.db_manager.disconnect()
        self.connected = False

    def authenticate(self, username, password):
        if not self.connected:
            raise RuntimeError("未建立数据库连接.")
        
        return self.db_manager.check_password(username, password)

    def login_loop(self):
        while True:
            username = input("请输入用户名: ")
            password = getpass.getpass("请输入密码: ")
            
            res = self.authenticate(username, password)
            if res:
                print("登录成功.")
                return res  # 在认证成功时返回结果对象
            else:
                print("登录失败，请重试.")
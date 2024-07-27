from auth_db import UserAuthenticator

DB_CONFIG = {
    'host': 'lg36520fe35.vicp.fun',
    'port': 18445,
    'user': 'root',
    'password': '',
    'database': 'xfztest',
    'charset': 'utf8mb4',
    'connect_timeout': 30,
    'salt': 'madman',
}

authenticator = UserAuthenticator(DB_CONFIG)
authenticator.connect()
res = authenticator.login_loop()
authenticator.disconnect()
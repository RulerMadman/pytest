import hashlib
password = "password"
token = "ahd"
md5password = password + token
print(hashlib.md5(md5password.encode("utf-8")).hexdigest())
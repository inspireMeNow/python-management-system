from Crypto.Cipher import AES
import hashlib
from cryptography.fernet import Fernet
import json
import base64


def encrypt(string):
    salt = Fernet.generate_key()  # 随机生成盐值
    key = Fernet(salt)  # 使用Fernet加密器对象
    new_salt = base64.urlsafe_b64encode(salt)
    encrypted_pass = key.encrypt(string)
    data = {'salt': new_salt, 'password': encrypted_pass}
    # 创建一个AES加密对象
    return data
def sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()[0:20]
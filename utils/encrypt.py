import hashlib


class Encrypt:

    def md5(data):
        return hashlib.md5(data.encode()).hexdigest()

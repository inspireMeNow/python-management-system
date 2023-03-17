import re


def check_password_strength(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$"
    common_passwords = ["password", "123456", "qwerty", "abc123"]

    # 密码长度至少8位
    if len(password) < 8:
        return 0

    # 检查常用密码
    elif password.lower() in common_passwords:
        return 1

    # 密码复杂度
    elif not re.match(pattern, password):
        return 2

    # 强密码
    else:
        return 3


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

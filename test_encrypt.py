import sys
from utils import server_encrypt
from utils import check


if __name__ == "__main__":
    try:
        
        print(server_encrypt.sha256('dkyDKY1593574628'))
        # print(encrypt.md5("1945331896fe38d734e")[0:19])

    except Exception as e:
        print(str(e))
        sys.exit(1)

    finally:
        sys.exit()
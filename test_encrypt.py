import sys
from utils import encrypt
from utils import check


if __name__ == "__main__":
    try:
        
        # print(encrypt.md5("dkyDKY159357"))
        print(encrypt.md5("DKY357896")[0:19])

    except Exception as e:
        print(str(e))
        sys.exit(1)

    finally:
        sys.exit()
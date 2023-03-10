import sys
from utils.encrypt import Encrypt


if __name__ == "__main__":
    try:
        
        print(Encrypt.md5(""))

    except Exception as e:
        print(str(e))
        sys.exit(1)

    finally:
        sys.exit()
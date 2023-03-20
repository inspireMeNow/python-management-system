# import sys
# from client.login_window import LoginWindow
# from PyQt6.QtWidgets import QApplication

# if __name__ == "__main__":
#     try:

#         app = QApplication([])
#         client = LoginWindow()
#         client.show()
#         app.exec()


#     except Exception as e:
#         print(f"Error connecting to MariaDB Platform: {e}")
#         sys.exit(1)

#     finally:
#         sys.exit()
import socket
import ssl
import json
import sys
from utils import encrypt

try:
    host = 'localhost'
    port = 8888
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(cafile="server/cert/cert.pem")
    # context.check_hostname=False

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=host) as s:
            s.connect((host, port))
            send_data = {"key": "is_register", "value": {
                "id": "ssss", "password": "DKY123456", "email": "asa@def.com", "idtype": 1}}
            s.send(json.dumps(send_data).encode())
            # receive data from the server
            data = s.recv(1024)
            print(data.decode())

except Exception as e:
    print(f"Connection failed! {e}")
    sys.exit(1)

    # send data to the server
    # send_data = {'key': 'update_part', 'value': {'p_code': 'pj00000001', 'p_name': 'i9-13900k', 'p_type': 'cpu', 'manufacture': 'intel',
    #                                         'protime': '2022-12-07 18:18:00', 'warranty_time': 2, 'info': '散片', 'size': 40}}

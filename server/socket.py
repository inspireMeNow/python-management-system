import socket
import ssl
from service import part_service
from service import user_service
from service import in_out_service
from pojo.part import Part
from pojo.user import User
from pojo.in_order import In_Order
from pojo.out_order import Out_Order
import json


def run_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(
            certfile='server/cert/cert.pem', keyfile='server/cert/key.pem')
        server_socket = ssl_context.wrap_socket(
            server_socket, server_side=True)
        server_socket.bind(('127.0.0.1', 8888))

        server_socket.listen(10)

        while True:
            ssl_client_socket, address = server_socket.accept()
            data = ssl_client_socket.recv(1024)
            print("Client ", str(address), "'s Message: ", data.decode())
            if (json.loads(data.decode())['key'] == 'search_part'):
                part = part_service.find_by_code(
                    json.loads(data.decode())['value'])
                ssl_client_socket.send(str(part.to_json()).encode())

            elif (json.loads(data.decode())['key'] == 'insert_part'):
                part = Part()
                part.set_p_code(json.loads(data.decode())['value']['p_code'])
                part.set_args(json.loads(data.decode())['value']['p_name'],
                              json.loads(data.decode())['value']['p_type'],
                              json.loads(data.decode())[
                    'value']['manufacture'],
                    json.loads(data.decode())['value']['protime'],
                    json.loads(data.decode())[
                    'value']['warranty_time'],
                    json.loads(data.decode())['value']['info'],
                    json.loads(data.decode())['value']['size'])
                is_success = part_service.insert(part)
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'update_part'):
                part = Part()
                part.set_p_code(json.loads(data.decode())['value']['p_code'])
                part.set_args(json.loads(data.decode())['value']['p_name'],
                              json.loads(data.decode())['value']['p_type'],
                              json.loads(data.decode())[
                    'value']['manufacture'],
                    json.loads(data.decode())['value']['protime'],
                    json.loads(data.decode())[
                    'value']['warranty_time'],
                    json.loads(data.decode())['value']['info'],
                    json.loads(data.decode())['value']['size'])
                is_success = part_service.update_by_code(part)
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'find_all_part'):
                part = part_service.find_all()
                ssl_client_socket.send(str(part).encode())

            elif (json.loads(data.decode())['key'] == 'search_user'):
                user = user_service.find_user(
                    json.loads(data.decode())['value']['id'])
                ssl_client_socket.send(str(user.to_json()).encode())

            elif (json.loads(data.decode())['key'] == 'is_login'):
                user = User()
                user.set_args(json.loads(data.decode())['value']['id'],
                              json.loads(data.decode())['value']['password'],
                              '', 1)
                is_success = user_service.login(user)
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'is_register'):
                user = User()
                user.set_args(json.loads(data.decode())['value']['id'],
                              json.loads(data.decode())['value']['password'],
                              json.loads(data.decode())['value']['email'], 1)
                is_success = user_service.register(user)
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'set_email'):
                is_success = user_service.set_email(json.loads(
                    data.decode())['value']['id'], json.loads(data.decode())['value']['email'])
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'set_password'):
                is_success = user_service.set_password(json.loads(
                    data.decode())['value']['id'], json.loads(data.decode())['value']['password'])
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'admin_login'):
                user = User()
                user.set_args(json.loads(data.decode())['value']['id'],
                              json.loads(data.decode())['value']['password'],
                              '', 0)
                is_success = user_service.admin_login(user)
                ssl_client_socket.send(str(is_success).encode())

            elif (json.loads(data.decode())['key'] == 'find_all_user'):
                user = user_service.find_all()
                ssl_client_socket.send(json.dumps(user).encode())

            elif (json.loads(data.decode())['key'] == 'find_all_in_order'):
                order = in_out_service.find_all_in_order()
                ssl_client_socket.send(json.dumps(order,ensure_ascii=False).encode())
            
            elif (json.loads(data.decode())['key'] == 'find_all_out_order'):
                order = in_out_service.find_all_out_order()
                ssl_client_socket.send(json.dumps(order).encode())

            elif (json.loads(data.decode())['key'] == 'delete_user_by_id'):
                is_success = user_service.delete_user(json.loads(data.decode())['value'])
                ssl_client_socket.send(str(is_success).encode())

            else:
                ssl_client_socket.send(b'Invalid request!')

    except KeyboardInterrupt:

        ssl_client_socket.close()
        server_socket.close()
        ssl_client_socket.shutdown()
        server_socket.shutdown()

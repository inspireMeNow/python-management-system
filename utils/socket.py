import socket
import ssl
from service import part_service
from pojo.part import Part
import json


def run_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(
            certfile='utils/cert/cert.pem', keyfile='utils/cert/key.pem')
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
                part.set_args(json.loads(data.decode())['value']['p_name'], json.loads(data.decode())['value']['p_type'], json.loads(data.decode())['value']['manufacture'],
                          json.loads(data.decode())['value']['protime'], json.loads(data.decode())['value']['warranty_time'], json.loads(data.decode())['value']['info'], json.loads(data.decode())['value']['size'])
                is_success = part_service.insert(part)
                ssl_client_socket.send(str(is_success).encode())
            else:
                ssl_client_socket.send(b'Invalid request!')

    except KeyboardInterrupt:

        ssl_client_socket.close()
        server_socket.close()
        ssl_client_socket.shutdown()
        server_socket.shutdown()

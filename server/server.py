import socket
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import urllib.parse
from pojo.part import Part
from service import part_service
from service import user_service
from pojo.user import User

# 自定义子类，用于处理 HTTP 请求


class CustomHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        query = urllib.parse.urlparse(path).query
        params = urllib.parse.parse_qs(query)
        if path.startswith('/search_part'):

            part = Part()
            part = part_service.find_by_code(params['p_code'])
            if part is None:
                part = Part()
            print(part.to_json())
            # print(json.dumps(part.to_json()))
            # params = dict(urllib.parse.parse_qsl(query))
            # self.send_response(200)
            # self.end_headers()
            # print(str(params))
            # self.wfile.write(bytes(str(params), "utf8"))
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(part.to_json()).encode())

        elif path.startswith('/find_all_part'):
            part = part_service.find_all()
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(part).encode())

        elif path.startswith('/update_part'):
            part = Part()
            part.set_p_code(params['p_code'][0])
            part.set_args(params['p_name'][0], params['p_type'][0], params['manufacture'][0],
                          params['protime'][0], params['warranty_time'][0], params['info'][0], params['size'][0])
            is_success = part_service.update_by_code(part)
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

        elif path.startswith('/delete_part'):
            is_success = part_service.delete_by_code(params['p_code'][0])
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

        elif path.startswith('/insert_part'):
            part = Part()
            part.set_p_code(params['p_code'][0])
            part.set_args(params['p_name'][0], params['p_type'][0], params['manufacture'][0],
                          params['protime'][0], params['warranty_time'][0], params['info'][0], params['size'][0])
            is_success = part_service.insert(part)
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

        elif path.startswith('/search_user'):
            user = user_service.find_user(params['id'][0])
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(user.to_json()).encode())

        elif path.startswith('/set_password'):
            is_success = user_service.set_password(
                params['id'][0], params['password'][0])
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

        elif path.startswith('/set_email'):
            is_success = user_service.set_email(
                params['id'][0], params['email'][0])
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

        elif path.startswith('/is_login'):
            user = User()
            user.set_args(params['id'][0], params['password'][0],
                          '', 1)
            is_success = user_service.login(user)
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

        elif path.startswith('/is_register'):
            if 'email' in params:
                email = params['email'][0]
            else:
                email = ''
            if 'id' in params:
                id = params['id'][0]
            else:
                id = ''
            if 'password' in params:
                password = params['password'][0]
            else:
                password = ''
            if 'idtype' in params:
                idtype = params['idtype'][0]
            else:
                idtype = ''
            user = User()
            user.set_args(id, password, email, idtype)
            print(user.to_json())
            is_success = user_service.register(user)
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(is_success).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))


httpd = HTTPServer(('localhost', 8088), CustomHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()

import socket
import json

from http.server import HTTPServer,BaseHTTPRequestHandler
import socketserver


# 自定义子类，用于处理 HTTP 请求
class CustomHandler(BaseHTTPRequestHandler):

    __data=''

    def set_data(self,data):
        self.__data=data
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><head><title>Python HTTP Server</title></head>")
        self.wfile.write(b"<body><p>"+b"hello world"+b"</p></body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data=json.loads(post_data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

httpd = HTTPServer(('localhost', 8088), CustomHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()

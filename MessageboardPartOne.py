#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-length',0))
        data = self.rfile.read(length).decode()

        message = parse_qs(data)["message"][0]
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8085)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

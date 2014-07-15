#!/usr/bin/env python
import BaseHTTPServer, SimpleHTTPServer
import ssl

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)
 
    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
 
 
if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8443), MyHTTPRequestHandler)
#create pem using command : openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='<PATH TO PEM FILE>', server_side=True)
    httpd.serve_forever()
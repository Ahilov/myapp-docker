#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Python behind HTTPS!</h1>")
        self.wfile.write(b"<p>SSL and Reverse Proxy are working perfectly!</p>")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print("Server running on port 8000...")
    server.serve_forever()

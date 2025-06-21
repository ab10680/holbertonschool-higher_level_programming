#!/usr/bin/python3
"""Simple HTTP server with multiple endpoints"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"status": "OK"}
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode())

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

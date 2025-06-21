#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers(content_type='text/plain')
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self._set_headers()
            self.wfile.write(
                b'{"name":"John","age":30,"city":"New York"}')

        elif self.path == '/status':
            self._set_headers()
            self.wfile.write(b'{"status":"OK"}')

        elif self.path == '/info':
            self._set_headers()
            self.wfile.write(
                b'{"version":"1.0","description":"A simple API built with http.server"}')

        else:
            self._set_headers(404)
            self.wfile.write(b'{"error":"Endpoint not found"}')


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("🚀 Serving on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

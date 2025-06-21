#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def _send_json(self, data, status_code=200):
        self._set_headers(status_code)
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.path == '/':
            self._set_headers(content_type='text/plain')
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self._send_json({"name": "John", "age": 30, "city": "New York"})

        elif self.path == '/status':
            self._send_json({"status": "OK"})

        elif self.path == '/info':
            self._send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })

        else:
            self._send_json({"error": "Endpoint not found"}, status_code=404)


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Serving on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

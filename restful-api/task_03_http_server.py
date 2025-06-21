#!/usr/bin/python3
"""Python web server"""
import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, code=200, content_type="application/json"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self._set_headers()
            self.wfile.write(
                b'{"name":"John","age":30,"city":"New York"}'
            )

        elif self.path == "/status":
            self._set_headers()
            self.wfile.write(b'{"status":"OK"}')

        else:
            self._set_headers(404)
            self.wfile.write(b'{"error":"Endpoint not found"}')


Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

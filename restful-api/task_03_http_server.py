def do_GET(self):
    if self.path == '/':
        self._set_headers(content_type='text/plain')
        self.wfile.write(b"Hello, this is a simple API!")

    elif self.path == '/data':
        self._send_json({"name": "John", "age": 30, "city": "New York"})

    elif self.path == '/status':
        self._set_headers(200, 'application/json')
        self.wfile.write(b'{"status":"OK"}')

    elif self.path == '/info':
        self._send_json({
            "version": "1.0",
            "description": "A simple API built with http.server"
        })

    else:
        self._set_headers(404, 'application/json')
        self.wfile.write(b'{"error":"Endpoint not found"}')

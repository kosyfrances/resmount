from http.server import HTTPServer, BaseHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 5555)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

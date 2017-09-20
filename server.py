from http.server import HTTPServer, BaseHTTPRequestHandler

from mount_points import get_mount_points


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = get_mount_points()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(message, 'utf8'))


def run():
    server_address = ('0.0.0.0', 5555)
    print('Starting server on localhost:5555')
    httpd = HTTPServer(server_address, GetHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()

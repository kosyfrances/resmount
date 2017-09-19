from http.server import HTTPServer, BaseHTTPRequestHandler

from mount_points import get_mount_points


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = get_mount_points()
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('Starting server ...')
    server_address = ('localhost', 5555)
    httpd = HTTPServer(server_address, GetHandler)
    httpd.serve_forever()


run()

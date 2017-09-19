from http.server import HTTPServer, BaseHTTPRequestHandler


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = 'It works'
        self.send_response(200)
        self.send_header()
        self.wfile.write(message)
        return


def run():
    print('Starting server ...')
    server_address = ('localhost', 5555)
    httpd = HTTPServer(server_address, GetHandler)
    httpd.serve_forever()


run()

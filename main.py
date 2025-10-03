import setup_database
import backend_functions
import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers()
        self.wfile.write(b"Received GET request")

    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(f"Recieved POST request: {post_data.decode('utf-8')}".encode('utf-8'))
    
def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    config = configparser.ConfigParser()
    config.read("config.ini")
    database = config.get("Connection","Database")
    setup_database.setup_database(database)
    backendFunctions = backend_functions.BackendFunctions(database)

    server_address = ('', port)
    httpd = server_class(server_address,handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
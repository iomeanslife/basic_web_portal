import setup_database
import backend_functions
import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer

backendFunctions = None

class Handler(BaseHTTPRequestHandler):
    backendFunctions = None

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        print(self.headers.get('Cookie'))
        self._set_headers()

        if self.path == "/create_user":
            self.wfile.write(b"""<!DOCTYPE html>
<html>
<body>
<h2>Login Form</h2>
<form action="/create_user" method="POST">
  <label for="username">Username:</label><br>
  <input type="text" id="username" name="username" value=""><br>
  <label for="password">Password:</label><br>
  <input type="password" id="password" name="password" value=""><br>
  <label for="repeat_password">Repeat Password:</label><br>
  <input type="password" id="password" name="repeat_password" value=""><br>
  <input type="submit" value="CreateUser">
</form> 
</body>
</html>""")

        else:
            self.wfile.write(b"""<!DOCTYPE html>
<html>
<body>
<h2>Login Form</h2>
<form action="/login" method="POST">
  <label for="username">Username:</label><br>
  <input type="text" id="username" name="username" value=""><br>
  <label for="password">Password:</label><br>
  <input type="password" id="password" name="password" value=""><br>
  <input type="submit" value="Login">
  <a href="create_user" title="Create User">Create User</a>
</form> 
</body>
</html>""")

    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length)
        decoded = post_data.decode('utf-8').split('&')
        
        try:
            username = decoded[0][9:]
            hash = decoded[1][9:]
            if len(decoded) >= 3:
                repeat_hash = decoded[2][16:]
        
        except:
            self.send_response(422)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f"Processing Request Failed.".encode('utf-8'))
            return
  
        if self.path == "/create_user":
            if hash != repeat_hash or Handler.backendFunctions.create_user(username, hash) is not True:
                self.send_response(401)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(f"Signup Failed.".encode('utf-8'))                                                                   
                return
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.send_header('Set-Cookie',f'simple_token={username}; Max-Age=5560' ) # TODO: Generate some UUID and store it in the database which the cookie can be compared to.
            self.end_headers()

            self.wfile.write(f'User "{username}" was created'.encode('utf-8'))
            return
        elif self.path == "/login" and Handler.backendFunctions.login_user(username, hash) is not True:
            self.send_response(401)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f"Login Failed.".encode('utf-8'))
            return

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Set-Cookie',f'simple_token={username}; Max-Age=5560' )
        self.end_headers()

        self.wfile.write(f" POST request: {post_data.decode('utf-8')}".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    config = configparser.ConfigParser()
    config.read("config.ini")
    database = config.get("Connection","Database")
    setup_database.setup_database(database)
    Handler.backendFunctions = backend_functions.BackendFunctions(database)

    server_address = ('', port)
    httpd = server_class(server_address,handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
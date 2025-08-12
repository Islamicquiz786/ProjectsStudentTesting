from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class LearningServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('html/dashboard.html', 'rb') as file:
                self.wfile.write(file.read())
            return
        super().do_GET()

def run(server_class=HTTPServer, handler_class=LearningServer, port=8080):
    web_dir = os.path.join(os.path.dirname(__file__), '../html')
    os.chdir(web_dir)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
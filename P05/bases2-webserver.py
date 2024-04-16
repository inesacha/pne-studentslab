import http.server
import socketserver
import termcolor
from pathlib import Path

# -- Server network parameters
PORT = 8080

def read_html_file(filename):
    folder = "html/info/"
    file_contents = Path(folder + filename).read_text()
    return file_contents

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if "/info/A.html" == self.path:
            contents = read_html_file("A.html")
        elif "/info/C.html" == self.path:
            contents = read_html_file("C.html")
        elif "/info/G.html" == self.path:
            contents = read_html_file("G.html")
            self.send_response(200)
        elif "/info/T.html" == self.path:
            contents = read_html_file("T.html")
            self.send_response(200)
        elif self.path == "/" or self.path == "/index.html":
            contents = Path("html/index.html").read_text()
            self.send_response(200)
        else:
            myfile = self.path[1:]
            try:
                contents = Path(f"html/{myfile}").read_text()
                self.send_response(202)
            except FileNotFoundError:
                contents = Path("html/error.html").read_text()
                self.send_response(404)
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

# ------------------------
# - Server MAIN program
socketserver.TCPServer.allow_reuse_address = True
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
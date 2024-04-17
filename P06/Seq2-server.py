import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
# -- Server network parameters
PORT = 8080


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        if path == "/":
            contents = Path("html/index.html").read_text()
            self.send_response(200)
        elif path.startswith("/ping"):
            contents = Path("html/ping.html").read_text()
            self.send_response(200)
        else:
            contents = Path("html/error.html").read_text()
            self.send_response(404)


        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

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
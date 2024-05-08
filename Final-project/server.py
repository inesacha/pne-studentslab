import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

SERVER = 'rest.ensembl.org'
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def is_request_ok(SERVER, URL):
    error = False
    data = ""
    try:
        connection = http.client.HTTPSConnection(SERVER)
        connection.request("GET", URL)
        response = connection.getresponse()
        print(response.status)
        if response.status == 200:
            json_str = response.read().decode()
            data = json.loads(json_str)
        else:
            error = True
    except Exception:
        error = True
    return error, data


def for_error(path, message):
    context = {
        'endpoint': path,
        'message': message
    }
    return read_html_file("error.html").render(context=context)



def for_listSpecies(path, parameters):
    RESOURCE = '/info/species'
    PARAMETER = '?content-type=application/json'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(SERVER, "Error with Ensembl server")
        code = 404
    else:
        limit = None
        if 'limit' in parameters:
            limit = int(parameters['limit'][0])
        species = data['species']
        list_of_species = []
        for s in species[:limit]:
            list_of_species.append(s['display_name'])
        context = {
            'total_number': len(species),
            'client_limit': limit,
            'name_species':list_of_species
        }
        contents = read_html_file("species.html").render(context=context)
        code = 202
    return code, contents



def for_karyotype(path, parameters):
    RESOURCE = 'info/species'
    PARAMETER = '?content-type=application/json'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(path, "Error with Ensembl server")
        code = 404
    else:
        species = parameters['species'][0]
        context = {
            'specie': species,
            'karyotype': data['karyotype']
        }
        contents = read_html_file("karyotype.html").render(context=context)
        code = 202
    return contents, code

#def for_chromosome_lenght(parameters):
#al salir de bucle for, controlar si la lenght es None
#while lenght == None
#for


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        code = 200
        if path == "/":
            contents = Path("html/index.html").read_text()
        elif path == "/listSpecies":
            contents = for_listSpecies(path, arguments)
        self.send_response(code)


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


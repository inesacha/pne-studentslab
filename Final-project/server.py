import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

PORT = 8080
SERVER = 'rest.ensembl.org'
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def is_request_ok(SERVER, URL):
    error = False
    data = None
    try:
        connection = http.client.HTTPSConnection(SERVER)
        connection.request("GET", URL)
        response = connection.getresponse()
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


def for_listSpecies(parameters):
    ENDPOINT = '/listSpecies'
    RESOURCE = '/info/species'
    PARAMETER = '?content-type=application/json'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(ENDPOINT, "Error with Ensemblux server")
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
        code = 200
    return code, contents


def for_karyotype(parameters):
    ENDPOINT = '/karyotype'
    RESOURCE = '/info/assembly'
    species = parameters['species'][0]
    PARAMETER = f'/{species}?content-type=application/json'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(ENDPOINT, "Error with Ensembl server")
        code = 404
    else:
        context = {
            'specie': species,
            'karyotype': data['karyotype']
        }
        contents = read_html_file("karyotype.html").render(context=context)
        code = 200
    return code, contents


def for_chromosmeLength(parameters):
    ENDPOINT = '/chromosomeLength'
    RESOURCE = '/info/assembly'
    species = parameters['species'][0]
    PARAMETER = f'/{species}?content-type=application/json'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(ENDPOINT, "Error with Ensembl server")
        code = 404
    else:
        chr = data['top_level_region']
        chromosome = parameters['chr'][0]
        for c in chr:
            if c['name'] == chromosome:
                length = c['length']
                break
        context = {
            'chr': chromosome,
            'karyotype': length
        }
        contents = read_html_file("chromosomeLength.html").render(context=context)
        code = 200
    return code, contents



class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        endpoint = url_path.path
        parameters = parse_qs(url_path.query)
        code = 200
        if endpoint == "/":
            contents = Path("html/index.html").read_text()
        elif endpoint == "/listSpecies":
            code, contents = for_listSpecies(parameters)
        elif endpoint == "/karyotype":
            code, contents = for_karyotype(parameters)
        elif endpoint == "/karyotype":
            code, contents = for_karyotype(parameters)
        else:
            contents = for_error(endpoint, "Error with Ensembleeeee server")
            code = 404

        self.send_response(code)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()


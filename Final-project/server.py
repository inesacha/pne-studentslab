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
        contents = for_error(ENDPOINT, "Not a real number. Please try again")
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
            'name_species': list_of_species
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
        contents = for_error(ENDPOINT, f"{species} doesn't exist. Please try again.")
        code = 404
    else:
        context = {
            'specie': species,
            'karyotype': data['karyotype']
        }
        contents = read_html_file("karyotype.html").render(context=context)
        code = 200
    return code, contents


def for_chromosomeLength(parameters):
    ENDPOINT = '/chromosomeLength'
    RESOURCE = '/info/assembly'
    species = parameters['species'][0]
    PARAMETER = f'/{species}?content-type=application/json'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(ENDPOINT, "Error with Ensembl server to find the chromosome you are looking for. Please try again.")
        code = 404
    else:
        chr = data['top_level_region']
        chromosome = parameters['chromo'][0]
        length = None
        for c in chr:
            if c['name'] == chromosome:
                length = c['length']
                break
        context = {
            'chr': chromosome,
            'length': length
        }
        contents = read_html_file("chromosome.html").render(context=context)
        code = 200
    return code, contents

def for_geneID(gene):
    RESOURCE = '/homology/symbol/human/' + gene
    PARAMETER = '?content-type=application/json;format=condensed'
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    id = None
    if not error:
        id = data['data'][0]['id']
    return id


def for_geneSeq(parameters):
    ENDPOINT = '/geneSeq'
    RESOURCE = '/sequence/id'
    gene = parameters['gene'][0]
    id = for_geneID(gene)
    if not id is None:
        PARAMETER = f'/{id}?content-type=application/json'
        URL = RESOURCE + PARAMETER
        error, data = is_request_ok(SERVER, URL)
        if error:
            contents = for_error(ENDPOINT,"Error with Ensembl server to return the sequence of the human gene that you are looking for. Please try again.")
            code = 404
        else:
            seq = data['seq']
            context = {
                    'gene': gene,
                    'seq': seq
                }
            contents = read_html_file("seq.html").render(context=context)
            code = 200
    return code, contents

def for_geneInfo(parameters):
    ENDPOINT = '/geneInfo'
    RESOURCE = '/overlap/id'
    gene = parameters['gene'][0]
    id = for_geneID(gene)
    if not id is None:
        PARAMETER = f'/{id}?content-type=application/json;feature=gene'
        URL = RESOURCE + PARAMETER
        error, data = is_request_ok(SERVER, URL)
        if error:
            contents = for_error(ENDPOINT,"Error with Ensembl server to return information about the sequence of a human gene that you are looking for. Please try again.")
            code = 404
        else:
            data = data[0]
            name = data['assembly_name']
            start = data['start']
            end = data['end']
            context = {
                    'name': name,
                    'id': id,
                    'gene': gene,
                    'start': start,
                    'end': end,
                    'length': end - start,
                }
            contents = read_html_file("info.html").render(context=context)
            code = 200
    return code, contents

def for_geneCalc(parameters):
    from Seq1 import Seq
    ENDPOINT = '/geneCalc'
    RESOURCE = '/sequence/id'
    gene = parameters['gene'][0]
    id = for_geneID(gene)
    if not id is None:
        PARAMETER = f'/{id}?content-type=application/json'
        URL = RESOURCE + PARAMETER
        error, data = is_request_ok(SERVER, URL)
        if error:
            contents = for_error(ENDPOINT,"Error with Ensembl server to perform calculations about the sequence of the human gene that you are looking for. Please try again.")
            code = 404
        else:
            seq = data['seq']
            s = Seq(seq)
            context = {
                    'gene': gene,
                    'length': s.len(),
                    'infoA': f"{s.count_base('A')} ({round((s.count_base('A') / s.len() * 100),1)}%)",
                    'infoC': f"{s.count_base('C')} ({round((s.count_base('C') / s.len() * 100),1)}%)",
                    'infoG': f"{s.count_base('G')} ({round((s.count_base('G') / s.len() * 100), 1)}%)",
                    'infoT': f"{s.count_base('T')} ({round((s.count_base('T') / s.len() * 100), 1)}%)",
            }
            contents = read_html_file("calc.html").render(context=context)
            code = 200
    return code, contents

def for_geneList(parameters):
    ENDPOINT = '/geneList'
    RESOURCE = '/overlap/region/human'
    chromo = parameters['chromo']
    start = int(parameters['start'][0])
    end = int(parameters['end'][0])
    PARAMETER = f"/{chromo}:{start}-{end}?content-type=application/json;feature=gene"
    URL = RESOURCE + PARAMETER
    error, data = is_request_ok(SERVER, URL)
    if error:
        contents = for_error(ENDPOINT,"Error with Ensembl server to return the names of the genes located in the chromosome that you are looking for. Please try again.")
        code = 404
    else:
        list_of_genes_name = []
        for d in data:
            if 'external_name' in d:
                list_of_genes_name.append(d['external_name'])
        context = {
                'list': list_of_genes_name,
            }
        contents = read_html_file("list.html").render(context=context)
        code = 200
    return code, contents


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        endpoint = url_path.path
        parameters = parse_qs(url_path.query)
        code = 200
        print(parameters)
        if endpoint == "/":
            contents = Path("html/index.html").read_text()
        elif endpoint == "/listSpecies":
            code, contents = for_listSpecies(parameters)
        elif endpoint == "/karyotype":
            code, contents = for_karyotype(parameters)
        elif endpoint == "/chromosomeLength":
            code, contents = for_chromosomeLength(parameters)
        elif endpoint == "/geneSeq":
            code, contents = for_geneSeq(parameters)
        elif endpoint == "/geneInfo":
            code, contents = for_geneInfo(parameters)
        elif endpoint == "/geneCalc":
            code, contents = for_geneCalc(parameters)
        elif endpoint == "/geneList":
            code, contents = for_geneList(parameters)
        else:
            contents = for_error(endpoint, "If you are here is because the data you have entered does not exist on Ensembl. Sorry!")
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


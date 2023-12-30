from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 5443), SimpleHTTPRequestHandler)
httpd.socket = ssl.PEM_cert_to_DER_cert
httpd.serve_forever()
from http.server import HTTPServer, CGIHTTPRequestHandler
port = 8000
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print(f"Starting simple_httpd on: http://localhost:{httpd.server_port}")
httpd.serve_forever()

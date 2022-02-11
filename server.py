# Plain http.server sometimes answers with wrong text/plain MIME type.

import http.server
import socketserver


def main():
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.extensions_map = {
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js':	'application/x-javascript',
        '': 'application/octet-stream',  # Default
    }
    server = socketserver.TCPServer(("", 8000), Handler)
    print("Serving at port 8000")
    server.serve_forever() 


if __name__ == "__main__":
    main()

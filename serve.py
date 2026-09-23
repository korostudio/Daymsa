"""Servidor estatico local para la maqueta Daymsa.

Uso:  python serve.py [puerto]     (por defecto 5173)

Sirve la carpeta del proyecto y mapea la raiz "/" al diseno actual,
para que la URL sea http://127.0.0.1:5173/ en vez del nombre largo
del archivo .dc.html.
"""
import functools
import http.server
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOME = "index.html"                   # pagina que se sirve en "/"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5173


class Handler(http.server.SimpleHTTPRequestHandler):
    # HTTP/1.1 + keep-alive: el navegador reutiliza conexiones en vez de abrir
    # una por imagen, que es lo que hacia que algunas no cargaran.
    protocol_version = "HTTP/1.1"

    def translate_path(self, path):
        if path.split("?", 1)[0].rstrip("/") in ("", "/daymsa"):
            return str(ROOT / HOME)
        return super().translate_path(path)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    handler = functools.partial(Handler, directory=str(ROOT))
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    http.server.ThreadingHTTPServer.daemon_threads = True
    http.server.ThreadingHTTPServer.request_queue_size = 128   # ráfagas de imagenes
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"Daymsa -> http://127.0.0.1:{PORT}/   (Ctrl+C para parar)")
        httpd.serve_forever()

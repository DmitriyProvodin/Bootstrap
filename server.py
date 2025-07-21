import http.server
import socketserver
from pathlib import Path

PORT = 8000
TEMPLATE_PATH = Path("templates/index.html")
STATIC_PATH = Path("static/img")

images = [
    {"filename": "fbf17291e774624c7457c956431f7573.webp", "caption": "Фото 1"},
    {"filename": "c7746654406565828ad2810308e2050f.webp", "caption": "Фото 2"},
    {"filename": "583a50ff617df5f00b6c897d1f467eb3.webp", "caption": "Фото 3"},
    {"filename": "f191a2cdfe472fd34a2bdd0a53c9f9a0.webp", "caption": "Фото 4"},
]

def render_cards():
    cards_html = ""
    for img in images:
        cards_html += f"""
        <div class="col">
            <div class="card shadow-sm">
                <img src="/static/img/{img['filename']}" class="card-img-top" alt="{img['caption']}">
                <div class="card-body">
                    <p class="card-text">{img['caption']}</p>
                </div>
            </div>
        </div>
        """
    return cards_html

def generate_html():
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return template.replace("{{ cards }}", render_cards())

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = generate_html()
            self.wfile.write(html.encode("utf-8"))
        else:
            super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Сервер запущен: http://localhost:{PORT}")
        httpd.serve_forever()

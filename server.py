from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pages = {
            "/": "index.html",
            "/catalog": "catalog.html",
            "/category": "category.html",
            "/contacts": "contacts.html"
        }

        page = pages.get(self.path, "index.html")

        try:
            with open(f"templates/{page}", "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            self.send_error(404, "Страница не найдена")
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(body.decode())

        print("Получены POST-данные:")
        for key, value in data.items():
            print(f"{key}: {value}")

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Спасибо! Данные получены.</h1>")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()

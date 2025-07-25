from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            "/": "index.html",
            "/catalog": "catalog.html",
            "/category": "category.html",
            "/contacts": "contacts.html",
        }

        file_name = routes.get(self.path, "index.html")  # По умолчанию — главная

        file_path = os.path.join("templates", file_name)

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        else:
            self.send_error(404, "Страница не найдена")

    def do_POST(self):
        if self.path == "/contacts":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = parse_qs(body)

            print("\n--- Получены данные из формы ---")
            for key, value in data.items():
                print(f"{key}: {value[0]}")
            print("----------------------------------\n")

            # Вернуть обратно contacts.html
            file_path = os.path.join("templates", "contacts.html")
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            else:
                self.send_error(404, "Страница не найдена")
        else:
            self.send_error(404, "POST-запрос поддерживается только для /contacts")


def run():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Сервер запущен на http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

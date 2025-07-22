from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Путь до файла contacts.html
        with open('templates/contacts.html', 'r', encoding='utf-8') as f:
            html = f.read()

        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(body)

        print("Получены данные POST-запроса:")
        for key, value in data.items():
            print(f"{key}: {value[0]}")

        # Отправляем ту же страницу контактов в ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        with open('templates/contacts.html', 'r', encoding='utf-8') as f:
            html = f.read()
        self.wfile.write(html.encode('utf-8'))


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущен на http://localhost:8000 ...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()

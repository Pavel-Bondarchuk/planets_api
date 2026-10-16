from http.server import BaseHTTPRequestHandler, HTTPServer
import json

planets = [
    {
        "name": "Марс",
        "type": "Каменистая земля",
        "distance": "227,9 млн км"
    },
{
        "name": "Земля",
        "type": "Каменистая земля",
        "distance": "149,6 млн км"
    },
{
        "name": "Юпитер",
        "type": "Газовый гигант",
        "distance": "778,5 млн км"
    },
]

class PlanetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/planets":
            response = json.dumps(planets, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_error(404, "Путь не найден!")

server = HTTPServer(("127.0.0.1", 8000), PlanetHandler)

print("Сервер запущен!")
print("Открыть: http://127.0.0.1:8000/planets")

server.serve_forever()
# ==========================================
# AARYA AI v2.6
# API Server Core
# ==========================================

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from api import get_status



# Server Settings

HOST = "localhost"
PORT = 8000




class AARYAHandler(BaseHTTPRequestHandler):


    def do_GET(self):

        if self.path == "/status":

            response = get_status()


            data = json.dumps(
                response
            )


            self.send_response(200)

            self.send_header(
                "Content-type",
                "application/json"
            )

            self.end_headers()


            self.wfile.write(
                data.encode()
            )


        else:

            self.send_response(404)

            self.end_headers()




def start_server():


    server = HTTPServer(
        (HOST, PORT),
        AARYAHandler
    )


    print(
        "🤖 AARYA API Server Started"
    )


    print(
        f"Running at http://{HOST}:{PORT}"
    )


    server.serve_forever()




if __name__ == "__main__":

    start_server()
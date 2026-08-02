# ==========================================
# AARYA AI v2.7
# API Server + Memory Core Integration
# ==========================================


from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


from api import get_status



# ==========================
# Server Settings
# ==========================

HOST = "127.0.0.1"
PORT = 8000



# ==========================
# Memory File Location
# ==========================

MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "aarya_memory.json"
)



# ==========================
# Handler
# ==========================

class AARYAHandler(BaseHTTPRequestHandler):


    def send_json(self, data):

        response = json.dumps(
            data,
            indent=4
        )


        self.send_response(200)


        self.send_header(
            "Content-Type",
            "application/json"
        )


        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )


        self.end_headers()


        self.wfile.write(
            response.encode("utf-8")
        )



    def do_GET(self):


        print(
            "REQUEST:",
            self.path
        )



        # ==========================
        # Home
        # ==========================

        if self.path == "/":


            self.send_json({

                "system": "AARYA AI",

                "version": "v2.7",

                "status": "ONLINE",

                "message": "API Server Running"

            })




        # ==========================
        # Status API
        # ==========================

        elif self.path == "/status":


            data = get_status()


            self.send_json(
                data
            )




        # ==========================
        # Memory API
        # ==========================

        elif self.path == "/memory":


            try:


                with open(

                    MEMORY_FILE,

                    "r",

                    encoding="utf-8"

                ) as file:


                    data = json.load(
                        file
                    )



                print(
                    "MEMORY:",
                    data
                )



                self.send_json(
                    data
                )



            except Exception as error:


                print(
                    "MEMORY ERROR:",
                    error
                )


                self.send_json({

                    "error":
                    str(error)

                })




        # ==========================
        # 404
        # ==========================

        else:


            self.send_response(
                404
            )


            self.end_headers()



# ==========================
# Start Server
# ==========================


def start_server():


    server = HTTPServer(

        (HOST, PORT),

        AARYAHandler

    )


    print(
        "🤖 AARYA API Server Started"
    )


    print(
        "Running at http://127.0.0.1:8000"
    )


    print(
        "Endpoints:"
    )


    print(
        "/"
    )


    print(
        "/status"
    )


    print(
        "/memory"
    )


    server.serve_forever()





if __name__ == "__main__":


    start_server()
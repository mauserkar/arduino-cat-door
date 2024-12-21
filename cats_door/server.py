import socket

from cats_door.config import env
from cats_door.web import index_html, off_html, on_html
from cats_door.switch_pin import change_status, status


def start_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print(f'INFO: server http://{env["network_ip"]}:80')

    while True:
        cl, addr = s.accept()
        decode_request = cl.recv(1024).decode("utf-8")
        request = decode_request.splitlines()[0]

        print(f"INFO: {addr[0]} {request}")

        if "/on.html" in request:
            change_status(1)
            response = on_html()

        elif "/off.html" in request:
            change_status(0)
            response = off_html()
        else:
            response = index_html()

        # HTTP response
        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send(response)
        cl.close()

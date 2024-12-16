import socket

from cats_door.config import env
from cats_door.web import index_html


def start_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print("server http://{}:80".format(env.network_ip))

    while True:
        cl, addr = s.accept()
        request = cl.recv(1024).decode("utf-8")

        # print("client ip:", addr[0])
        # print("request:", request)

        if "/?led=on" in request:
            # led.value(1)
            # print(led.value())
            print("debug: led on")

        elif "/?led=off" in request:
            # led.value(0)
            # print(led.value())
            print("debug: led off")
        else:
            response = index_html()

        # HTTP response
        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send("<html><body><h1>{}</h1></body></html>".format(response))
        cl.close()

from cats_door.network import wireless_connect
from cats_door.server import start_server


try:
    wireless_connect()
    start_server()
except KeyboardInterrupt:
    print("server stopped.")

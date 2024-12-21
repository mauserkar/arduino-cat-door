import network
import time

from cats_door.config import env


def wireless_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.ifconfig(
        (
            env["network_ip"],
            env["network_mask"],
            env["network_gateway"],
            env["network_dns"],
        )
    )
    wlan.connect(env["network_ssid"], env["network_password"])
    while not wlan.isconnected():
        time.sleep(0.5)
    print(f'INFO: Network connected: {env["network_ssid"]}')

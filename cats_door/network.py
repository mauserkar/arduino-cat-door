import network

from cats_door.config import env


def wireless_connect():
    # print(f"DEBUG: {env}")
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
        pass
    print(f"INFO: {env["network_ssid"]} Network connected")

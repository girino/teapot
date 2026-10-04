# Copyright (c) 2026 Girino Vey.
# Licensed under the Girino Anarchist License: https://license.girino.org

import network
import rp2
import socket
import time

from wifi_secrets import WIFI_PASSWORD, WIFI_SSID

BODY = """\
   (         ____
    )    .;'`    `';,
   (    //          \\\
    ,_ ||  _..-n-.._ ||
   (c)\\||-"'-.....-"-;|
    \\  ;'             Y
     \\_/`              \\
     ;                  ;
     |                  |
     |                  |
      '.__          __.'
          ``\"\"\"\"\"\"``

       🫖 I'm a teapot 🫖

Copyright (c) 2026 Girino Vey.
Project: https://github.com/girino/teapot
License: https://github.com/girino/teapot/blob/main/LICENSE
""".encode("utf-8")

RESPONSE = (
    b"HTTP/1.1 418 I'm a teapot\r\n"
    b"Content-Type: text/plain; charset=utf-8\r\n"
    + b"Content-Length: "
    + str(len(BODY)).encode()
    + b"\r\nConnection: close\r\n\r\n"
    + BODY
)


def connect_wifi():
    rp2.country("BR")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    for _ in range(30):
        if wlan.isconnected():
            print("Teapot server: http://{}".format(wlan.ifconfig()[0]))
            return
        time.sleep(1)

    raise RuntimeError("Wi-Fi connection failed")


def serve():
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("0.0.0.0", 80))
    listener.listen(2)

    while True:
        client, _ = listener.accept()
        try:
            client.settimeout(2)
            client.recv(1024)
            client.sendall(RESPONSE)
        finally:
            client.close()


connect_wifi()
serve()

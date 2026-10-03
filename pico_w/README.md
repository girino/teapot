# Pico W teapot server

This MicroPython version serves the same HTTP `418 I'm a teapot` response as
the ESP32-C3 firmware.

1. Copy `wifi_secrets.py.example` to `wifi_secrets.py` and enter the local
   Wi-Fi credentials. The local file is ignored by Git.
2. Upload `main.py` and `wifi_secrets.py` to the Pico W filesystem. The
   existing MicroPython firmware can be used.
3. Reset the board. It prints the assigned IP address over `COM4` at 115200
   baud, then serves HTTP on port 80.

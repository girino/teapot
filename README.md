# Teapot

An intentionally tiny HTTP server that responds to every request with
`418 I'm a teapot`, an ASCII teapot, and project metadata.

Repository: <https://github.com/girino/teapot>

## License

Copyright (c) 2026 Girino Vey. Licensed under the
[Girino Anarchist License](LICENSE), sourced from
<https://license.girino.org>.

## ESP32-C3 SuperMini

The supported hardware target is an ESP32-C3 SuperMini connected over USB-C.

1. Install Arduino CLI and the Espressif ESP32 core locally under `.tools/`
   and `.arduino/`. These directories are ignored by Git.
2. Copy the Wi-Fi template and fill in the local credentials:

   ```powershell
   Copy-Item .\wifi_secrets.h.example .\wifi_secrets.h
   ```

3. Compile for the ESP32-C3 with USB serial enabled:

   ```powershell
   .\.tools\arduino-cli\arduino-cli.exe compile --config-file .\.arduino\arduino-cli.yaml --fqbn esp32:esp32:esp32c3:CDCOnBoot=cdc --output-dir .\build .
   ```

4. Find the serial port and upload:

   ```powershell
   .\.tools\arduino-cli\arduino-cli.exe board list --config-file .\.arduino\arduino-cli.yaml
   .\.tools\arduino-cli\arduino-cli.exe upload --config-file .\.arduino\arduino-cli.yaml --fqbn esp32:esp32:esp32c3:CDCOnBoot=cdc --port COM3 --input-dir .\build .
   ```

Replace `COM3` with the detected port. If upload does not start automatically,
hold `BOOT`, start the upload, and release it once the connection begins.

## Raspberry Pi Pico W

`pico_w/main.py` is a MicroPython implementation for a functional Pico W.
Copy `pico_w/wifi_secrets.py.example` to `pico_w/wifi_secrets.py`, add local
Wi-Fi credentials, then upload both files to the board filesystem.

The Pico W currently tested in this project cannot initialize its CYW43 Wi-Fi
radio, even with the official MicroPython Pico W UF2. Use the ESP32-C3 target
unless a working Pico W is available.

## Test

Read the ESP32 serial output at 115200 baud to obtain its DHCP address, then
run:

```powershell
curl.exe -i http://BOARD_IP/
```

# ESP32-C3 HTTP 418 teapot

This firmware responds to every HTTP request with `418 I'm a teapot` and a
plain-text `I'm a teapot` body.

## Local setup

1. Edit `wifi_secrets.h` with the Wi-Fi SSID and password. This local file is
   ignored by Git.
2. Compile using the project-local Arduino CLI:

   ```powershell
   .\.tools\arduino-cli\arduino-cli.exe compile --config-file .\.arduino\arduino-cli.yaml --fqbn esp32:esp32:esp32c3 --output-dir .\build .
   ```

3. With the board connected, list serial ports and upload using the port shown:

   ```powershell
   .\.tools\arduino-cli\arduino-cli.exe board list --config-file .\.arduino\arduino-cli.yaml
   .\.tools\arduino-cli\arduino-cli.exe upload --config-file .\.arduino\arduino-cli.yaml --fqbn esp32:esp32:esp32c3 --port COM3 --input-dir .\build .
   ```

Replace `COM3` with the detected port. If automatic upload fails, hold `BOOT`
while starting the upload and release it once the connection begins.

## Test

Read the board's printed IP address at 115200 baud, then run:

```powershell
curl.exe -i http://BOARD_IP/
```

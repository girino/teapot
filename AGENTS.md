# Agent Instructions

## Project Scope

This repository contains two implementations of the same HTTP 418 teapot
server:

- `teapot.ino`: Arduino firmware for ESP32-C3 SuperMini.
- `pico_w/main.py`: MicroPython firmware for Raspberry Pi Pico W.

## Secrets

- `wifi_secrets.h` and `pico_w/wifi_secrets.py` contain local Wi-Fi
  credentials and are ignored by Git.
- Never read, print, commit, or place Wi-Fi credentials in documentation.
- Update only the corresponding `*.example` file when changing configuration
  structure.

## ESP32-C3

- Use the project-local Arduino CLI at `.tools/arduino-cli/arduino-cli.exe`.
- Keep Arduino CLI data and Espressif packages in `.arduino/`.
- Build with `esp32:esp32:esp32c3:CDCOnBoot=cdc`.
- Detect the serial port with `arduino-cli board list`; never assume `COM3`.
- Verify a flash by testing for HTTP status `418` from the board's DHCP IP.

## Pico W

- The Pico W source targets MicroPython and needs `main.py` plus a local
  `wifi_secrets.py` on the device filesystem.
- Do not overwrite a physical board unless the user explicitly asks.
- The currently tested Pico W reports `Failed to start CYW43`; do not present
  the Pico W implementation as verified on that device.

## Changes

- Preserve the `418` response and UTF-8 content type.
- Keep the repository and license links in responses synchronized with
  `https://github.com/girino/teapot` and `LICENSE`.
- Run the relevant compile or syntax validation after code changes.
- Inspect `git status`, `git diff`, and recent history before committing.
- Commit completed changes, but do not push unless the user explicitly asks.

# Agent Instructions

## Project Scope

This repository contains an Arduino HTTP 418 teapot server for ESP32-C3
SuperMini boards.

## Secrets

- `wifi_secrets.h` contains local Wi-Fi credentials and is ignored by Git.
- Never read, print, commit, or place Wi-Fi credentials in documentation.
- Update only the corresponding `*.example` file when changing configuration
  structure.

## ESP32-C3

- Use the project-local Arduino CLI at `.tools/arduino-cli/arduino-cli.exe`.
- Keep Arduino CLI data and Espressif packages in `.arduino/`.
- Build with `esp32:esp32:esp32c3:CDCOnBoot=cdc`.
- Detect the serial port with `arduino-cli board list`; never assume `COM3`.
- Verify a flash by testing for HTTP status `418` from the board's DHCP IP.

## Changes

- Preserve the `418` response and UTF-8 content type.
- Keep the repository and license links in responses synchronized with
  `https://github.com/girino/teapot` and `LICENSE`.
- Run the ESP32 compile validation after code changes.
- Inspect `git status`, `git diff`, and recent history before committing.
- Commit completed changes, but do not push unless the user explicitly asks.

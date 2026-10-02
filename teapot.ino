#include <WiFi.h>
#include <WebServer.h>

#include "wifi_secrets.h"

WebServer server(80);

void serveTeapot() {
  server.send(418, "text/plain; charset=utf-8", "I'm a teapot\n");
}

void printServerUrl() {
  Serial.print("Teapot server: http://");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println();
  printServerUrl();

  server.onNotFound(serveTeapot);
  server.begin();
}

void loop() {
  server.handleClient();

  static unsigned long lastStatus = 0;
  if (millis() - lastStatus >= 5000) {
    lastStatus = millis();
    printServerUrl();
  }
}

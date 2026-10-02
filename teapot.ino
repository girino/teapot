#include <WiFi.h>
#include <WebServer.h>

#include "wifi_secrets.h"

WebServer server(80);

void serveTeapot() {
  server.send(418, "text/plain; charset=utf-8", "I'm a teapot\n");
}

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.print("Teapot server: http://");
  Serial.println(WiFi.localIP());

  server.onNotFound(serveTeapot);
  server.begin();
}

void loop() {
  server.handleClient();
}

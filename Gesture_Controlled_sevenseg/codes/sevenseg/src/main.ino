#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

const char* ssid = "ARUN_KUMAR";
const char* password = "arunkumar";

String direction = "";

/* Seven-Segment Display Pins */
const int segmentPins[] = {32, 33, 25, 26, 27, 14, 12}; // Adjust the pin numbers for your setup
const int commonPin = 16; // Adjust the pin number for your setup

void setup() {
  Serial.begin(115200);
  Serial.println("GPIO test!");

  /* Connect to WiFi */
  connectingToWiFi();

  server.on("/", handleRequest);
  server.onNotFound(handleRequest);

  /* Start Server */
  server.begin();
  Serial.println("Server started");

  /* Initialize Seven-Segment Display Pins */
  for (int i = 0; i < 7; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }
  pinMode(commonPin, OUTPUT);
}

void loop() {
  /* Handle Request */
  server.handleClient();
  String direction = server.arg("direction");
  Serial.println(direction);

  if (direction == "F") {
    displayNumber(1); /* Display "1" on seven-segment display */
  } else if (direction == "B") {
    displayNumber(2); /* Display "2" on seven-segment display */
  } else if (direction == "R") {
    displayNumber(4); /* Display "4" on seven-segment display */
  } else if (direction == "L") {
    displayNumber(3); /* Display "3" on seven-segment display */
  } else if (direction == "S") {
    displayNumber(0); /* Display "0" on seven-segment display */
  }
}

void handleRequest() {
  if (server.hasArg("direction")) {
    Serial.println(server.arg("direction"));
  }
  server.send(200, "text/html", "");
  delay(1);
}

void connectingToWiFi() {
  delay(3000);
  WiFi.disconnect();
  delay(1000);
  Serial.println("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (!(WiFi.status() == WL_CONNECTED)) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected");
  Serial.println("Local IP is: ");
  Serial.print(WiFi.localIP().toString());
  delay(5000);
}

/* Display Number on Seven-Segment Display (Common Anode) */
void displayNumber(int number) {
  // Define the seven-segment patterns for each number (common anode)
  const int digitPatterns[10][7] = {
    {0, 0, 0, 0, 0, 0, 1}, // 0
    {1, 0, 0, 1, 1, 1, 1}, // 1
    {0, 0, 1, 0, 0, 1, 0}, // 2
    {0, 0, 0, 0, 1, 1, 0}, // 3
    {1, 0, 0, 1, 1, 0, 0}, // 4
    {0, 1, 0, 0, 1, 0, 0}, // 5
    {0, 1, 0, 0, 0, 0, 0}, // 6
    {0, 0, 0, 1, 1, 1, 1}, // 7
    {0, 0, 0, 0, 0, 0, 0}, // 8
    {0, 0, 0, 0, 1, 0, 0}  // 9
  };

  // Check if the number is within the valid range
  if (number >= 0 && number <= 9) {
    // Set the segment pin states based on the digit pattern
    for (int i = 0; i < 7; i++) {
      digitalWrite(segmentPins[i], !digitPatterns[number][i]); // Invert the pattern for common anode
    }
  }

  // Enable the common pin to display the number
  digitalWrite(commonPin, HIGH); // Set common pin LOW for common anode
}



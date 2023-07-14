#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

const char* ssid = "ARUN_KUMAR";
const char* password = "arunkumar";

String direction = "";
int robospeed = 800; /* Defining speed limit min 400 to max 1023 */

/* Defining right and left motor pins */
int RMotor_1 = 0; /* Right Motor GPIO0(D3) */
int RMotor_2 = 2; /* Right Motor GPIO2(D4) */
int LMotor_1 = 13; /* Left Motor GPIO13(D7) */
int LMotor_2 = 15; /* Left Motor GPIO15(D8) */

/* Defining L298N enable pins */
int REnable = 14; /* Right Motor Enable Pin GPIO14(D5) */
int LEnable = 12; /* Right Motor Enable Pin GPIO12(D6)  */

void setup() {
  Serial.begin(115200);
  Serial.println("GPIO test!");

  /* Initialize Motor Control Pins as Output */
  pinMode(RMotor_1, OUTPUT);
  pinMode(RMotor_2, OUTPUT);
  pinMode(LMotor_1, OUTPUT);
  pinMode(LMotor_2, OUTPUT);

  /* Initialize Motor Enable Pins as Output */
  pinMode(REnable, OUTPUT);
  pinMode(LEnable, OUTPUT);

  /* Connect to WiFi */
  connectingToWiFi();

  server.on("/", handleRequest);
  server.onNotFound(handleRequest);

  /* Start Server */
  server.begin();
  Serial.println("Server started");

  /* Start Motors */
  analogWrite(REnable, robospeed);
  analogWrite(LEnable, robospeed);
}

void loop() {
  /* Handle Request */
  server.handleClient();
  String direction = server.arg("direction");
  Serial.println(direction);

  if (direction == "F") {
    move_forward(); /* If direction F moves forward */
  } else if (direction == "B") {
    move_backward(); /* If direction B moves backward */
  } else if (direction == "R") {
    turn_right(); /* If direction R turns right */
  } else if (direction == "L") {
    turn_left(); /* If direction L turns left */
  } else if (direction == "S") {
    move_stop(); /* If direction S stops moving */
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

/* Move Forward */
void move_forward() {
  digitalWrite(RMotor_1, LOW);
  digitalWrite(RMotor_2, HIGH);
  digitalWrite(LMotor_1, HIGH);
  digitalWrite(LMotor_2, LOW);
}

/* Move Backward */
void move_backward() {
  digitalWrite(RMotor_1, HIGH);
  digitalWrite(RMotor_2, LOW);
  digitalWrite(LMotor_1, LOW);
  digitalWrite(LMotor_2, HIGH);
}

/* Turn Right */
void turn_right() {
  digitalWrite(RMotor_1, LOW);
  digitalWrite(RMotor_2, HIGH);
  digitalWrite(LMotor_1, LOW);
  digitalWrite(LMotor_2, HIGH);
}

/* Turn Left */
void turn_left() {
  digitalWrite(RMotor_1, HIGH);
  digitalWrite(RMotor_2, LOW);
  digitalWrite(LMotor_1, HIGH);
  digitalWrite(LMotor_2, LOW);
}

/* Stop Move */
void move_stop() {
  digitalWrite(RMotor_1, LOW);
  digitalWrite(RMotor_2, LOW);
  digitalWrite(LMotor_1, LOW);
  digitalWrite(LMotor_2, LOW);
}



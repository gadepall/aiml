#include <Arduino.h>
#include <WiFi.h>
#include <esp32PWMUtilities.h>

/**
 * This is a header file which contains WiFi network credentials. 
 * Its contents are:
 *
 * const char *ssid = "YOUR-SSID-HERE";
 * const char *password = "YOUR-PASSWORD-HERE";
 *
*/
#include "credentials.h"

Motor Motor1;
Motor Motor2;
double th = -45.0;

void lock(int del) {
  delay(del);
  Motor1.lockMotor();
  Motor2.lockMotor();
  delay(1000);
}

// Move in forward direction
void front() {
  Motor1.moveMotor(127);
  Motor2.moveMotor(127);
  lock(300);
}

// Move in backward direction
void back() {
  Motor1.moveMotor(-127);
  Motor2.moveMotor(-127);
  lock(300);
}

// Rotate 90 degrees clockwise
void right() {
  Motor1.moveMotor(127);
  Motor2.moveMotor(-127);
  lock(190);
}

// Rotate 90 degrees anticlockwise
void left() {
  Motor1.moveMotor(-127);
  Motor2.moveMotor(127);
  lock(190);
}

// Get RSSI at a point
double getRSSI() {
  delay(100);
  double sig_read;
  while ((sig_read = WiFi.RSSI()) > 0);
  return sig_read;
}

// Infinite loop to prevent loop() from iterating again
void stop() {
  while (1);
}

void setup() {
  Motor1.attach(14, 16, 17);
  Motor2.attach(15, 18, 19);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED);
}

// Helper routine to get index position maximum of an array
int maxArray(double *arr, int sz) {
  double mx = arr[0];
  int idx = 0;
  for (int i = 1; i < sz; i++) if (mx < arr[i]) mx = arr[i], idx = i;
  return idx;
}

void loop() {
  // Need to read RSSI Values
  // At point, then ahead, and then behind
  // EDIT: Three points might be a bit bad... Let's
  // try five points?
  int N = 5;
  double rssi[N];
  rssi[0] = getRSSI();
  for (int i = 1; i < N; i++) {
      front();
      rssi[i] = getRSSI();
      if (rssi[i] >= th) stop();
  }
  int idx = maxArray(rssi, N); 
  for (int i = N - 1; i > idx; i--) back();
  if (idx > 0 && idx < N-1) left();
  else if (idx == 0) back();
  else front();
}

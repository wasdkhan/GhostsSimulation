#include <SoftwareSerial.h>
#define RX 2
#define TX 3
SoftwareSerial XBee(RX, TX); // RX, TX

void setup()
{
  pinMode(RX, INPUT);
  pinMode(TX, OUTPUT);
  XBee.begin(9600);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()) { 
    XBee.write((unsigned char)Serial.read());
  }
  if (XBee.available()) { 
    Serial.write((unsigned char)XBee.read());
  }
}

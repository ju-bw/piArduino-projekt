/*
6-12V Gleichstrommotor, Relay: Finder 40.61 12V 16A
*/
const int controlPin = 9;

void setup() { 
  pinMode(controlPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("6-12V Gleichstrommotor, Relay: Finder 40.61 12V 16A");
}

void loop() { 
  digitalWrite(controlPin, LOW);   // (1)
  Serial.println("low - Signal: 5s");
  delay(5000);
  digitalWrite(controlPin, HIGH);
  Serial.println("high - Signal: 2s");
  delay(2000);
}

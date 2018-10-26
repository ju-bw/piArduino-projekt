
const int controlPin = 13; 

void setup() {  
  pinMode(controlPin, OUTPUT);
}

void loop() {  
  digitalWrite(controlPin, HIGH);
  delay(5000);
  digitalWrite(controlPin, LOW);
  delay(2000);
}

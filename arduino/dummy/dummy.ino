
int ms = 500; // 1000 ms = 1s
const int ledPin = 13;   // digitaler Ausgang: Spannung 0V oder 5V

// Einrichtungsroutine, die einmal ausgeführt wird, wenn Arduino startet oder nach Reset
void setup()
{
  // Initialisierung
  pinMode(ledPin, OUTPUT);
}
// Schleife wird endlos wiederholt
void loop()
{
  //Schaltet die ledPin
  digitalWrite(ledPin, HIGH); // Schaltet die ledPin ein (Spannung 5V = HIGH)
  delay(ms);       // Wartet
  digitalWrite(ledPin, LOW);  // Schaltet die ledPin aus (Spannung 0V = LOW, Masse, GND)
  delay(ms);       // Wartet
}


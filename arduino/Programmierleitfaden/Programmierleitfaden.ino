/*
Programmierleitfaden Arduino C

GitHub-Repository zum Download  (git clone https://github.com/simonmonk/make_action.git .)

Arduino Uno Modell R3 (Revision 3), ATMega328, 32KB Flash-Speicher = Programmspeicher

- setup und loop
- variablen
- Digitale Eingänge: Pins D0 - D13, Anwendung: Taster
- Digitale Ausgänge: Pins D0 - D13, Anwendung: Led
- Analoge Eingänge:  Pins A0 - A5 , Anwendung: Sensoren und Regler
- Analoge Ausgänge:  Pins (~) D3, D5, D6, D9, D10 und D11, Anwendung: Leistung regeln
- Vergleiche
  > Größer als
  < Kleiner als
  <= Kleiner oder gleich
  >= Größer oder gleich
  != Ungleich
  == gleich
- logischen Operatoren:
  && (AND) 
  || (OR)
- If/else
- Funktionen

Editor: visual studio code
  // Code formatieren: <Shift+Alt+F>
  F1 = Arduino: Board Manager
  F1 = Arduino: Select Serial Board
  F1 = Arduino: Board Config
  F1 = Arduino: Change Baud rate
  F1 = Arduino: Select Programmer
* F1 = Arduino: Verify      // Prüfen, Autovervollständigung
* F1 = Arduino: Upload      // Hochladen
* F1 = Open Serial Monitor  // Serieller Monitor
*/

int ms = 500; // 1000 ms = 1s
const int ledPin = 13;   // digitaler Ausgang: Spannung 0V oder 5V
const int tasterPin = 7; // digitaler Eingang: Spannung 0V oder 5V
const int switchPin = 8; // digitaler Eingang: Spannung 0V oder 5V

// Analoge Eingänge
//Analogwert lesen und umrechnen: (zahlenwert * 5) / 1023 oder zahlenwert / 204,6
//int raw = analogRead(A0);  // analoger Eingang: Spannungen zwischen 0V und 5V
//float volts = raw / 204.6; // liefert Zahlenwert zwischen 0 (0V) und 1023 (5V)
//float volts = (raw * 5) / 1023;

//Analoge Ausgänge
//analogWrite(100, ??); // Zahl zwischen 0 und 255 (255 volle Leistung, 100% PWM)
// 490 Pulse pro Sekunde mit variabler Pulsweite
// (Ausnahme D5 und D6, die 980 Pulse pro Sekunde liefern)

// Einrichtungsroutine, die einmal ausgeführt wird, wenn Arduino startet oder nach Reset
void setup()
{
  // Initialisierung
  pinMode(ledPin, OUTPUT);
  pinMode(tasterPin, INPUT);        // ext. Pullup Widerstand 10 kB
  pinMode(switchPin, INPUT_PULLUP); // int. Pullup Widerstand 40 kB, wenn Schalter offen, dann 5V

  // LED blinkt zehnmal, und hält dann an
  for (int i = 0; i < 10; i++)
  {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }

  // Funktionsaufruf
  // led blinkt 5 mal
  blink(ledPin, 5);
}
// Schleife wird endlos wiederholt
void loop()
{
  //LED soll so lange blinken, wie eine mit einem digitalen Eingang verbundene Taste gedrückt wird
  while (digitalRead(9) == LOW)
  {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }

  // LED einschalten, wenn der Messwert zwischen 300 und 400 liegt
  int reading = analogRead(A0);
  if ((reading >= 300) && (reading <= 400))
  {
    digitalWrite(ledPin, HIGH);
  }
  else
  {
    digitalWrite(ledPin, LOW);
  }

  // LED einschalten, wenn der Messwert größer als 500 ist
  if (analogRead(A0) > 500)
  {
    digitalWrite(ledPin, HIGH);
  }
  else
  {
    digitalWrite(ledPin, LOW);
  }

  // LED einschalten, wenn der Eingang zum Zeitpunkt der Messung HIGH ist.
  if (digitalRead(tasterPin) == HIGH)
  {
    digitalWrite(ledPin, HIGH);
  }

  //Schaltet die ledPin
  digitalWrite(ledPin, HIGH); // Schaltet die ledPin ein (Spannung 5V = HIGH)
  delay(ms);       // Wartet
  digitalWrite(ledPin, LOW);  // Schaltet die ledPin aus (Spannung 0V = LOW, Masse, GND)
  delay(ms);       // Wartet
}

// Funktion
void blink(int pin, int n)
{
  for (int i = 0; i < n; i++)
  {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }
}
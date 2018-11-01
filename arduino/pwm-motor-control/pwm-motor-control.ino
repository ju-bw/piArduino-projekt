/*
Den kleinsten noch brauchbaren Tastgrad für einen Motor herausfinden

Bei sehr niedrigen Werten, z. B. bei 10 oder vielleicht auch schon bei 20, kann
es sein, dass sich der Motor nicht mehr dreht, sondern eher ein gequältes Jaulen
von sich gibt, weil nicht mehr genug Leistung bei ihm ankommt, um die Reibung
zu überwinden.
*/

const int controlPin = 9;

void setup() {                    // (1)
  pinMode(controlPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("6-12V Gleichstrommotor, Mosfet: 2N7000G I(conti) 200mA I(pulsed)500mA");
  Serial.println("Enter Duty Cycle (13 to 100)");//Tastgrad 0 to 100
}

void loop() {                     // (2)
  if (Serial.available()) {       // (3) Eingabe: prüft, ob serielle Daten vorhanden sind
    int duty = Serial.parseInt(); // Zahl umwandeln Datentyp int
    if (duty < 13 || duty > 100) {  // (4)//Tastgrad < 0 || > 100
      Serial.println("13 to 100");//Tastgrad 0 to 100
    }
    else {
      int pwm = duty * 255 / 100; // 0 to 255 = Tastgrad von 0 % to 100 %
      analogWrite(controlPin, pwm);
      Serial.print("duty set to ");
      Serial.println(duty);
      delay(5000);// 5s
      analogWrite(controlPin, 0);// Motor aus
    }
  }
}

#include <Servo.h>

int pinVerde = 7;  // Pin para acceso permitido
int pinRojo = 6;
int pinAzul = 5;

Servo myservo;    // Crear un objeto servo
int pos = 0;      // Posición inicial del servo
bool puerta_abierta = false; // Estado de la puerta

void setup() {
  pinMode(pinVerde, INPUT);
  pinMode(pinRojo, INPUT);
  pinMode(pinAzul, INPUT);
  Serial.begin(9600);
  myservo.attach(9); // Configurar el pin del servo
}

void loop() {
  int estado_WELCOME = digitalRead(pinVerde);
  int estado_DENIED = digitalRead(pinRojo);
  int estado_PUERTA = digitalRead(pinAzul);

  if (estado_WELCOME == HIGH) {
    Serial.println("V");
    delay(5000);
  } else if (estado_DENIED == HIGH) {
    Serial.println("R");
    delay(5000);
  } else if (estado_PUERTA == HIGH && !puerta_abierta) {  
    Serial.println("a");
    moverServo(180, 0);
    puerta_abierta = true;
  } else if (estado_PUERTA == LOW && puerta_abierta) {
    Serial.println("c");
    moverServo(0, 180);
    puerta_abierta = false;
  }
  delay(1000);
}

void moverServo(int desde, int hasta) {
  if (desde < hasta) {
    for (int pos = desde; pos <= hasta; pos += 1) {
      myservo.write(pos);
      delay(15); // Ajusta el delay según la velocidad deseada
    }
  } else {
    for (int pos = desde; pos >= hasta; pos -= 1) {
      myservo.write(pos);
      delay(15); // Ajusta el delay según la velocidad deseada
    }
  }
}

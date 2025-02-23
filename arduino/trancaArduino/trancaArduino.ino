const int relayPin = 13;  // Pino do relé que controla a tranca
bool isLocked = true;    // Estado inicial da tranca (true = fechada, false = aberta)

void setup() {
    Serial.begin(9600);
    pinMode(relayPin, OUTPUT);
    digitalWrite(relayPin, HIGH);  // Garante que a tranca começa fechada
    Serial.println("Arduino pronto!");
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();  // Remove espaços e novas linhas extras

        if (command == "A" && isLocked) {
            digitalWrite(relayPin, LOW);  // Abre a tranca
            isLocked = false;
            Serial.println("Tranca aberta!");
        } else if (command == "F" && !isLocked) {
            digitalWrite(relayPin, HIGH);  // Fecha a tranca
            isLocked = true;
            Serial.println("Tranca fechada!");
        } else if (command == "status") {
            if (isLocked) {
                Serial.println("A tranca está fechada.");
            } else {
                Serial.println("A tranca está aberta.");
            }
        } else {
            Serial.println("Comando inválido ou já em estado solicitado.");
        }
    }
}

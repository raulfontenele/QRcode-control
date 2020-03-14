
char msg;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    if (Serial.available() > 0) {
      msg = Serial.read();
      if(msg == '1'){
        Serial.println("Recebeu");
      }
      else{
        Serial.println("Nao recebeu");
      }
    }
}

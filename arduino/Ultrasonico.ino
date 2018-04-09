
int ledGreen  = 8;
int ledYellow = 9;
int trigger = 7;
int echo = 6;
int distancia;
int duracion;



void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigger, HIGH);
  delay(1);
  digitalWrite(trigger, LOW);
  duracion = pulseIn(echo, HIGH);
  distancia = duracion / 58.2;
  Serial.println(distancia);
  delay(200);

  if (distancia <= 20 && distancia >=0){
    digitalWrite(ledYellow, LOW);
    delay(100);
    digitalWrite(ledGreen, HIGH);
    delay(100);
  }else{
    digitalWrite(ledGreen, LOW);
    delay(100);
    digitalWrite(ledYellow, HIGH);
    delay(100);
  }
  
}

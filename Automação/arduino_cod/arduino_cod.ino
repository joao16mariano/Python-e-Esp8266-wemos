
//Para Esp8266 Wemos D1 Mini Pro
#define Rele1 D0  //Pinos
#define Rele2 D1
#define Rele3 D3
#define Rele4 D4
#define Rele5 D5
#define Rele6 D6

/*PARA ARDUINO
#define Rele1 0 //Pinos
#define Rele2 1
#define Rele3 3
#define Rele4 4
#define Rele5 5
#define Rele6 6
*/

String cod;

void setup() {
  Serial.begin(9600);
  pinMode(Rele1, OUTPUT);
  pinMode(Rele2, OUTPUT);
  pinMode(Rele3, OUTPUT);
  pinMode(Rele4, OUTPUT);
  pinMode(Rele5, OUTPUT);
  pinMode(Rele6, OUTPUT);

   digitalWrite(Rele1, LOW);
   digitalWrite(Rele2, LOW);
   digitalWrite(Rele3, LOW);
   digitalWrite(Rele4, LOW);
   digitalWrite(Rele5, LOW);
   digitalWrite(Rele6, LOW);
}

void loop() {
  
  while(Serial.available()){
    delay(10);
    char aux = Serial.read();
    cod += aux;
  }
  
  if(cod == "001"){
    digitalWrite(Rele2, HIGH);
    cod = "";
  }
  if(cod == "003"){
    digitalWrite(Rele2, LOW);
    cod = "";
  }
  
  
   if(cod == "005"){
    digitalWrite(Rele1, HIGH);
    cod = "";
  }
   if(cod == "008"){
    digitalWrite(Rele1, LOW);
    cod = "";
  }

  
   if(cod == "011"){
    digitalWrite(Rele3, HIGH);
    cod = "";
  }
   if(cod == "014"){
    digitalWrite(Rele3, LOW);
    cod = "";
  }

  if(cod == "017"){
    digitalWrite(Rele4, HIGH);
    cod = "";
  }
   if(cod == "020"){
    digitalWrite(Rele4, LOW);
    cod = "";
  }

  if(cod == "023"){
    digitalWrite(Rele5, HIGH);
    cod = "";
  }
   if(cod == "026"){
    digitalWrite(Rele5, LOW);
    cod = "";
  }

 if(cod == "029"){
    digitalWrite(Rele6, HIGH);
    cod = "";
  }
   if(cod == "032"){
    digitalWrite(Rele6, LOW);
    cod = "";
  }
  
  delay(15);
}

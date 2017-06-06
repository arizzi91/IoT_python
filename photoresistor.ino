int sensorValue;
int sensorLow = 1023;
int sensorHigh = 0;

int buttonPressed=0;


void setup() {


  
  Serial.begin(9600);
  pinMode(7,INPUT);
  
  

  
}

void loop() {

         buttonPressed= digitalRead(7);
          
        
         if (buttonPressed == HIGH)
              {
                sensorValue = analogRead (A0);
            //    Serial.println("Valore fotoresistenza: ");
                Serial.println(sensorValue);
              }
        
       
         delay(300);
         
}

//Initializing photoresistor and button variables
int sensorValue;
int buttonPressed=0;


void setup() {

  //Starting 9600 bps serial communication to see sensor values through serial monitor
  Serial.begin(9600);
  //Defining input pin to control button status
  pinMode(7,INPUT);
  
}

void loop() {

         //To retrieve voltage on digital input and storing it in buttonPressed variable
         buttonPressed= digitalRead(7); 
          
         //If there is voltage on pin 7 buttonPressed becomes HIGH, otherwise it becames LOW
         if (buttonPressed == HIGH)
              { 
                //Reading photoresistor value on A0 pin
                //0<=rangeOfA0value<=1023 when 0 Volt<=V<=5 Volt is read 
                sensorValue = analogRead (A0);
                //Sending to photoresistor value to raspberry connected  
                Serial.println(sensorValue);
              }
        
         //Setting pause for 300 milliseconds to allow ADC correct working
         delay(300);
         
}

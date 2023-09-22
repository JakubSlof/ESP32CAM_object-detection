#include <Arduino.h>
#include <esp32cam.h>

#define LED_BUILTIN 4


void setup(){
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  Serial.println();
}

void loop()
{
  

        int number = Serial.parseInt();
    

    if (number == 1){
        digitalWrite(LED_BUILTIN, HIGH);
        delay(2000);
        Serial.println("69");
    }
    if (number == 2){
        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN, LOW);
        delay(1000);
         digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        Serial.println("69");
    }
    else{
            digitalWrite(LED_BUILTIN, LOW);
    }

}
//include libraries
#include <LiquidCrystal.h>
//define lcd_pins
#define rs 7
#define en 6
#define D4 5
#define D5 4
#define D6 3
#define D7 2
// define serial output
int d=0;
//setup lcd pins
LiquidCrystal lcd (rs,en,D4,D5,D6,D7);

void setup() {
  // put your setup code here, to run once:

lcd.begin(16,2);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  //if arduino recived 'f' from pc print fire detected on lcd //
 d=Serial.read();
 if(d=='f'){
   lcd.clear();
   delay(1000);
   lcd.print("^Fire detected^");
   delay(1000); 
  // blink text every 1second
 }
 //if no fire detected print safe
else if (d=='s'){
  lcd.clear();
  lcd.print("safe");
}
}

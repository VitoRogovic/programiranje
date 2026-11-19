unsigned int napon = 3750;
unsigned int kapacitet = 2600;
float naponV;
float kapacitetAh;
unsigned long ukupna_energija;
void setup(){
 Serial.begin(9600);
 ukupna_energija = (unsigned long)napon * kapacitet;
 Serial.print("ukupna energija: ");
 Serial.println(ukupna_energija);
  naponV = (float)napon /1000;
 Serial.print("napon u voltima je: ");
 Serial.println(naponV);
   kapacitetAh = (float)kapacitet /1000;
 Serial.print("kapacitet je: ");
 Serial.println(kapacitetAh);
}
void loop(){}

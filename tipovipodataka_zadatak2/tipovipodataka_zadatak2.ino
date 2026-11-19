unsigned long otpornik = 100000;
float kapacitet = 47e-6;
float tau;
float vrijeme;
void setup(){
  Serial.begin (9600);
  tau = otpornik * kapacitet;
  Serial.println(tau, 3);
  vrijeme = (5 * tau);
  Serial.print("vrijeme punjenja");
  Serial.print(vrijeme);
}
void loop(){}

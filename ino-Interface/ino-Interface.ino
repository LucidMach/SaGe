#define LED 2
int io;
// the inbuilt LED in Lema-NodeMCU is active cathode, i.e HIGH behaves as LOW and LOW behaves as HIGH
void setup()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
} 

void loop()
{
  io = Serial.read();
  delay(200);
  if (io == 'H')
  {
    digitalWrite(LED, LOW);
    delay(1000);
    digitalWrite(LED, HIGH);
  }
}
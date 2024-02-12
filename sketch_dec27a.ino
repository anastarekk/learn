#define motor1d1 12 //right back
#define motor1d2 13 // right forward
#define motor1speed 11 // right speed
#define motor2d1 7 //left back
#define motor2d2 8 //left forward
#define motor2speed 9 //left speed
#define irsensor1 A0  //left sensor
#define irsensor2 A1  //right sensor

// define every component output or input
void setup() {
  pinMode(motor1d1 , OUTPUT);
  pinMode(motor1d2 , OUTPUT);
  pinMode(motor2d1 , OUTPUT);
  pinMode(motor2d2 , OUTPUT);
  pinMode(motor1speed , OUTPUT);
  pinMode(motor2speed , OUTPUT);
  pinMode(irsensor1 , INPUT);
  pinMode(irsensor2 , INPUT);



}
//move forward function
void forward ()
{
 digitalWrite(motor1d1, LOW);
 digitalWrite(motor1d2, HIGH);
 digitalWrite(motor2d1, LOW);
 digitalWrite(motor2d2, HIGH);
 analogWrite(motor1speed, 170);
 analogWrite(motor2speed, 170);
}
//move right function
void right ()
{
 digitalWrite(motor1d1, LOW);
 digitalWrite(motor1d2, LOW);
 digitalWrite(motor2d1, LOW);
 digitalWrite(motor2d2, HIGH);
 analogWrite(motor1speed, 0);
 analogWrite(motor2speed, 150);
  
}
//move left function
void left ()
{
 digitalWrite(motor1d1, LOW);
 digitalWrite(motor1d2, HIGH);
 digitalWrite(motor2d1, LOW);
 digitalWrite(motor2d2, LOW);
 analogWrite(motor1speed, 150);
 analogWrite(motor2speed, 0);

}
//stop function
void stop ()
{
 digitalWrite(motor1d1, LOW);
 digitalWrite(motor1d2, LOW);
 digitalWrite(motor2d1, LOW);
 digitalWrite(motor2d2, LOW);
 analogWrite(motor1speed, 0);
 analogWrite(motor2speed, 0);
}


void loop() {
int ir1 = digitalRead(irsensor1); // taking the reading of left sensor
int ir2 = digitalRead(irsensor2); // taking the reading of right sensor



if (ir1 == LOW && ir2 == LOW) // black line in the middle (right and left sensors not reading black)
{
forward(); // car goes forward
delay(10);
}
else if(ir1 == HIGH && ir2 == LOW) // black line on the right (right sensor only reading black)
{
right(); // car goes right
delay(10);
}
else if(ir1 == LOW && ir2 == HIGH) // black line on the left (left sensor only reading black)
{
left(); // car goes left 
delay(10); 
}

else // both sensors reading black 
{
stop(); // car stops
}
}









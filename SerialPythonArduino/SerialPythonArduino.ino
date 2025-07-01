//#include<string.h>
unsigned long lastTime, sampleTime;

String inputString = "";
bool stringComplete = false;
const char separator = ',';
const int dataLength = 2;
double data[dataLength];
void setup() {
 Serial.begin(9600);
 sampleTime = 100;
 lastTime = millis();

}

void loop() {
  if (stringComplete)
  {
    for(int i = 0; i < dataLength; i++){
    int index = inputString.indexOf(separator);
    data[i] = inputString.substring(0,index).toFloat();
    inputString = inputString.substring(index+ + 1);
    }
    inputString = "";
    stringComplete = false;

  }
  if(millis()-lastTime >= sampleTime){
   lastTime = millis();
   Serial.println(data[0],3);
   Serial.println(data[1],3);
  }
}
void serialEvent(){

  while(Serial.available()){
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar =='\n'){
      stringComplete = true;
    }
  }
}

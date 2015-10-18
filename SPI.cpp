#include <SPI.h>

const int CLOCK = PB_2;                        //the Mux clock which is manually ticked in this program
const int CS_NOT = PE_0;                      //controls whether or not the output gate can be altered
const int DIN = PF_0;                              
const int DELAY = 500;





void setup()
{
  pinMode(DIN, INPUT);
  pinMode(CLOCK, OUTPUT);
  pinMode(CS_NOT, OUTPUT);
  delayMicroseconds(1);
  
  Serial.begin(9600);
  SPI.begin();
  SPI.setBitOrder(MSBFIRST);
  SPI.setDataMode(SPI_MODE0);
  SPI.setClockDivider(SPI_CLOCK_DIV4);

  delay(100);
}

void loop()
{
    //read only when its in is high
    if (digitalRead(DIN) == HIGH)
    {
        digitalWrite(CS_NOT, LOW);
        SPI.transfer(0x10);     //send the enabler bit
        result = SPI.transfer(0X00); //read from 0
        digitalWrite(CS_NOT, HIGH);

    }

}
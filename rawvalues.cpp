

const int CLOCK = PB_2;                        //the Mux clock which is manually ticked in this program
const int CS_NOT = PE_0;                      //controls whether or not the output gate can be altered
const int DIN = PF_0;                              //the pin through which the control array is sent
const int NUM_MUXES = 4;                   //the number of daisy-chained Muxes
const int DELAY = 500;


void setup()
{ 
  pinMode(DIN, OUTPUT);
  pinMode(CLOCK, OUTPUT);
  pinMode(CS_NOT, OUTPUT);
  delayMicroseconds(1);
  
  Serial.begin(9600);

  delay(DELAY);

}

void loop()
{
  
  int count = 0;
  for(int currentMux = 0; currentMux< NUM_MUXES; currentMux++)
  {
   
    for( int currentOutput = 0; currentOutput < 8; currentOutput++)
    {
        

         int *selectArray =  setOutput(currentMux, currentOutput);
          selectOutput(selectArray);
          delay(1);
          int reading = analogRead(A0);
      
          Serial.print(reading);
          Serial.print(" ");
          Serial.print(count);
         // Serial.print((currentMux + 1) * (currentOutput + 1));
          Serial.print("\n");
          count++;
          if(count == 30)
          {
            count = 0;
            break;
          }
        }

   }
    delay(DELAY + 10);

  }


void selectOutput(int* selectArray)                            //Function that sends array to MUX
{
  CSNOT_HIGH();                                //CSNOT set to HIGH
  CLOCK_HIGH();                                //CLOCK set to HIGH
    
  for(int i = 0; i < (4*NUM_MUXES); i++)
  {
    CLOCK_LOW();                              //ClOCK set to LOW
    digitalWrite(DIN, selectArray[i]);
    CLOCK_HIGH();                             //CLOCK is set to HIGH as MUX reads bits
  }
  
  CSNOT_LOW();                                //CSNOT set to LOW
  CLOCK_LOW();                                //ClOCK set to LOW
}

int* setOutput(int mux, int input)           //Function that prepares array that is to be sent to mux
{
  
 
   int selectArray[4*NUM_MUXES];
   int adjustedMux = 4 * mux;                //index of bit that is serves as the enabler for the chosen mux (indeces 0, 4, 8, 12)
         
   for(int i = 0; i < (NUM_MUXES*4); i++)    //initialize the array with LOW
   {
     selectArray[i] = LOW;
   }
     
   selectArray[adjustedMux] = HIGH;          //turn the enabling pin to HIGH bit that accesses multiplexer
   
   selectArray[adjustedMux + 1] = input%2;  //calculate the binary for the pin backwards due to documentation
   input/=2;                                //3 bits needed to determine pin number 0-7
   selectArray[adjustedMux + 2] = input%2;
   input/=2;
   selectArray[adjustedMux + 3] = input%2;
   return selectArray;
}

void CSNOT_HIGH()                           //CSNOT set to HIGH  
{
  digitalWrite(CS_NOT, HIGH);   
}

void CSNOT_LOW()                            //CSNOT set to LOW
{
  digitalWrite(CS_NOT, LOW);
}

void CLOCK_LOW()                           //CLOCK set to LOW
{
  digitalWrite(CLOCK, LOW);
  delayMicroseconds(1);
  
}

void CLOCK_HIGH()                         //CLOCK set to HIGH
{
  digitalWrite(CLOCK, HIGH);
  delayMicroseconds(1);
}


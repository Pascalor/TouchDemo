
const int size = 16;
const int CLOCK = PB_2;                        //the Mux clock which is manually ticked in this program
const int CS_NOT = PE_0;                      //controls whether or not the output gate can be altered
const int DIN = PF_0;                              //the pin through which the control array is sent
const int NUM_MUXES = 4;                   //the number of daisy-chained Muxes
const int DELAY = 300;


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
    
    int count = 0;  //this is the counter
    
    for(int pin = 0; pin < 32; pin++)
    {
        if( pin - 2 < 0)
        {continue;}
        boolean selectArray[size];
        setOutput(selectArray, size, pin );
        selectOutput(selectArray);
        delay(1);
        
        int reading = analogRead(A1);
        
        Serial.print(reading);
        Serial.print(" ");
        Serial.print(pin - 2);
        Serial.print("\n");
        
        delay(50);
        
    }
    
    delay(DELAY);
    
    
}



void selectOutput(boolean selectArray[])                            //Function that sends array to MUX
{
    CSNOT_HIGH();                                //CSNOT set to HIGH
    CLOCK_HIGH();                                //CLOCK set to HIGH
    
    for(int i = 0; i < (4*NUM_MUXES); i++)
    {
        CLOCK_LOW();                              //ClOCK set to LOW
        digitalWrite(DIN, selectArray[i]);        //Bits set in
        CLOCK_HIGH();                             //CLOCK is set to HIGH as MUX reads bits
    }
    
    CSNOT_LOW();                                //CSNOT set to LOW
    CLOCK_LOW();
    //ClOCK set to LOW
}

void setOutput(boolean selectArray[], int size, int number)           //Function that prepares array that is to be sent to mux
{
    //hardcoding shouldnt be but have to modify this
    
    boolean array[][16] =  {     {HIGH,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {HIGH,LOW, LOW, HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {HIGH,LOW, HIGH, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {HIGH,LOW, HIGH, HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {HIGH,HIGH, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {HIGH,HIGH, HIGH, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {HIGH,HIGH, HIGH, HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,LOW,LOW,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,LOW,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,LOW,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,HIGH,LOW,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,HIGH,HIGH,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,LOW,LOW,HIGH,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,LOW,HIGH,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,LOW,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,HIGH,LOW,HIGH,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH,LOW,LOW,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,LOW,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,LOW,LOW,HIGH},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,LOW,HIGH,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,LOW,HIGH,HIGH},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,HIGH,LOW,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,HIGH,LOW,HIGH},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,LOW},
        {LOW,LOW, LOW, LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH},
        
    };
    
    //initialize the list
    
    
    
    for (int iter = 0; iter < 16; iter++)
    {
        selectArray[iter] = array[number][iter];
    }
    
    
    
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




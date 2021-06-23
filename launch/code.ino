#include <SD.h>


#include <Arduino.h>
#include <Wire.h>

#include <BMP180I2C.h>

#define I2C_ADDRESS 0x77

//create an BMP180 object using the I2C interface
BMP180I2C bmp180(I2C_ADDRESS);

 
File myFile;
bool reading;
String Pres;
String NH3;
String CO;
String NO2;
String Temp;
String line;


String filename = "data5.csv";

 
void setup()
{
  Serial.begin(9600);

  Wire.begin();

  //begin() initializes the interface, checks the sensor ID and reads the calibration parameters.  
  if (!bmp180.begin())
  {
    Serial.println("begin() failed. check your BMP180 Interface and I2C Address.");
    while (1);
  }

  //reset sensor to default parameters.
  bmp180.resetToDefaults();

  //enable ultra high resolution mode for pressure measurements
  bmp180.setSamplingMode(BMP180MI::MODE_UHR);

  
  Serial.print("Initializing SD card...");
  // On the Ethernet Shield, CS is pin 4. It's set as an output by default.
  // Note that even if it's not used as the CS pin, the hardware SS pin 
  // (10 on most Arduino boards, 53 on the Mega) must be left as an output 
  // or the SD library functions will not work. 
   pinMode(10, OUTPUT);
 
  if (!SD.begin(10)) {
    Serial.println("initialization failed!");
    return;
  }
  Serial.println("initialization done.");
 
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  myFile = SD.open(filename, FILE_WRITE);
 
  // if the file opened okay, write to it:
  if (myFile) {
    Serial.print("Writing....");
    myFile.println("millis,Pres,Temp,NH3,CO,NO2");
    reading = true;
    
  } else {
    // if the file didn't open, print an error:
    Serial.println("error in opening");
  }
}
 
void loop()
{
  if (myFile && reading) {
      //start a temperature measurement
    if (!bmp180.measureTemperature())
    {
      Serial.println("could not start temperature measurement, is a measurement already running?");
      return;
    }
  
    //wait for the measurement to finish. proceed as soon as hasValue() returned true. 
    do
    {
      delay(100);
    } while (!bmp180.hasValue());
  
    Temp = String(bmp180.getTemperature());
  
    //start a pressure measurement. pressure measurements depend on temperature measurement, you should only start a pressure 
    //measurement immediately after a temperature measurement. 
    if (!bmp180.measurePressure())
    {
      Serial.println("could not start perssure measurement, is a measurement already running?");
      return;
    }
  
    //wait for the measurement to finish. proceed as soon as hasValue() returned true. 
    do
    {
      delay(100);
    } while (!bmp180.hasValue());
  
    Pres = String(bmp180.getPressure());

    NH3 = String(analogRead(A1));
    CO = String(analogRead(A2));
    NO2 = String(analogRead(A2));

    line = String(millis()) + "," + Pres + "," + Temp + "," + NH3 + "," + CO + "," + NO2;

    Serial.println(line);
    Serial.print("Writing....");
    myFile.println(line);
    myFile.close();
    myFile = SD.open(filename, FILE_WRITE);
    
    do
    {
      delay(100);
    } while (!myFile);
    
  }
}

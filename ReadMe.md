Flexband Pressure sensor set up:


30 pixel pressure sensor which is set up through a breadboard.


The breadboard

 Digital potentiometer is set to 5 megaohms
 There are 4 multiplexers which operate based off of a truth table i.e. 1 is on 0 is off. There is a datasheet that explains how each pin is being accessed but that is already true in the code itself.

Picture is taken




*Energia is used to operate on the microcontroller 

*open energia and select rawvalues.ino , If it can't be found repull from git



*If repulled from git rawvalues.cpp should be placed in a rawdata.ino file in order for it to be run on the TI TM4 launchpad

*upload and verify the code i.e. check button and or arrow button 

*If there is an IDIC device error make sure the board is plugged in and turned on correctly 

*Make sure the serial port is configured properly 

*The device is a TI tm4c123 80Mhz

*view serial monitor to see the data coming out

*Always reupload the code in energia to see if there are any erros involved with it


*Python GUI

*There are a couple of objects and classes that construct the gui
*Each class performs its own function aka reading the serial values/Drawing the grid/ Drawing the frame

*Baseline.py provides interface to average out the values being read into from the sensor

*Touch2d.py is an interface for creating the grids themselves 

*Touch2DGrid.py is the final version of the GUI which incopeates all of the objects 










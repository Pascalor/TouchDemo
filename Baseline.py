

import serial 
import statistics 


class Baseline :

	def __init__(self, target, size):
		self.usbport = "/dev/tty.usbmodem0E20E711"
		self.target = target #number of target pixel 
		self.basevalue = int() #the list of pixels 
		self.ser = serial.Serial(self.usbport, 9600)
		self.size = size #reading size 

	def setbasevalue(self):
		found = int()
		reading = []
		pressure = int(0)
		#find the pixel
		while len(reading) < self.size:
			value = self.ser.readline().split()
			try:
			 found = int(value[1])
			 pressure = int(value[0])
			except :
			 	print("Reading")	

			if found == self.target:
			 reading.append(pressure)


		base = int(statistics.mean(reading))
		return base

	def value(self):
		found = int()
		pressure = int(0)
		while True:
    		 value = self.ser.readline().split()
    		 try:
    			found = int(value[1])
    			pressure = int(value[0])
    		 except :
    			pass	
    		
    		 if found == self.target:
    			return  pressure 


		

# if __name__ == '__main__':
# 	baseline = Baseline(target = 29, size = 32)
# 	baseline.setbasevalue()
# 	while True:
# 		print(baseline.value())

	
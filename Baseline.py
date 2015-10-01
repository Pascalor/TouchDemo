

import serial 
import statistics 


class Baseline :

	

	def __init__(self,target,size):
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

			while found != self.target:
				value = self.ser.readline().split()
				try:
					found = int(value[1])
				except IndexError:
					pass	
				pressure = int(value[0])
				if found == self.target:
					break

			reading.append(pressure)
		
		reading.sort()		
		self.basevalue = int(statistics.median(reading))


	def value(self):
		
		found = int()
		pressure = int(0)
		while found != self.target:
				value = self.ser.readline().split()
				try:
					found = int(value[1])
				except IndexError:
					pass	
				pressure = int(value[0])
				if found == self.target:
					break
		return  pressure - self.basevalue

if __name__ == '__main__':
	baseline = Baseline(target = 1, size = 2)
	baseline.setbasevalue()
	while True:
		print(baseline.value())
	# ser = serial.Serial("/dev/tty.usbmodem0E20E711", 9600)
	
	# found = int()
	# pressure = int(0)
	# target = 2

	# while found != target:
	#  	value = ser.readline().split()
	# 	found = int(value[1])
	# 	pressure = int(value[0])
	# 	if found == target:
	# 		print(value)
	# 		break
	
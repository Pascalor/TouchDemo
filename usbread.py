
import serial 

def main():
    #while True:
    usbport = "/dev/tty.usbmodem0E20EB11"
    serialport = serial.Serial(usbport, 9600)
    print(serialport.readline())


if __name__ == '__main__':
	main()

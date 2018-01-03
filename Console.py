import serial

#refer http://pyserial.readthedocs.io/en/latest/pyserial_api.html


class Console(object):
	

	def Serialinfo(self, port, baudrate, parity = None, stopbits = 1,\
				size = 8, timeout = 0):
		#port setting
		self.portname = port
		#baudrate setting
		self.baudrate = baudrate
		
		#parity bit setting
		if(parity == None):
			 self.parity = serial.PARITY_NONE
		elif parity == "odd":
			 self.parity = serial.PARITY_ODD
		elif parity == "even":
			self.parity = serial.PARITY_EVEN
		
		#stop bits setting
		if(stopbits == 1):
			self.stopbits = serial.STOPBITS_ONE
		else:
			self.stopbits = serial.STOPBITS_TWO
			
		#size setting
		if(size == 8):
			self.bytesize = serial.EIGHTBITS
		elif (size == 5):
			self.bytesize = serial.FIVEBITS
		elif (size == 6):
			self.bytesize = serial.SIXBITS
		elif (size == 7):
			self.bytesize = serial. SEVENBITS
		
		#timeout setting
		self.timeout = timeout
		
		
	def Serialcon(self):
		self.ser = serial.Serial(port = self.portname,\
								baudrate = self.baudrate,\
								parity = self.parity,\
								stopbits = self.stopbits,\
								bytesize = self.bytesize,\
								timeout = self.timeout)
	
		print serial.tools.list_ports




def main():
	print "main"
	console = Console()
	console.Serialinfo("\\\\.\\pipe\\com_1", 115200)
	console.Serialcon()

	
	
	
if __name__ == "__main__":
	print "[*] Main Start"
	main()
from pynfc import Nfc, Desfire, Timeout 

class Rfid_NP532:

	def read_uid(self):

		n = Nfc("pn532_uart:/dev/ttyS0:115200") 
		DESFIRE_DEFAULT_KEY = b'\x00' * 8 
		MIFARE_BLANK_TOKEN = b'\xFF' * 1024 * 4 
		print("Esperant targeta") 
		
		generador = n.poll()

		return str(next(generador).uid, 'utf-8').upper()
#El next es el que fa que sols agafi el primer uid

if __name__ == "__main__":
	rf = Rfid_NP532()
	uid = rf.read_uid()
	print(uid)


#!/usr/bin/python
'''
Created on Aug 22, 2017

@author: Damian
'''
def leer():
	import time
	import serial

	RFID = serial.Serial(
    		port='/dev/ttyACM0',
    		baudrate=9600,
    		stopbits=serial.STOPBITS_ONE,
    		xonxoff=True,
    		bytesize=serial.EIGHTBITS,
    		timeout=3
	)
	#print(ser)
	if RFID.isOpen():
    		RFID.close()
	RFID.open()
	RFID.isOpen()
	#print(RFID.isOpen())
	RFID.write(b'\x01\x03\x80\x00\x00\x83')
	#print('escribio')
	#out = b''
	# let's wait one second before reading output (let's give device time to answer)
	time.sleep(1)
	#print(RFID.inWaiting)
	while RFID.inWaiting() > 0:
    		#print('entro al while')
    		out = RFID.read(40)

	#if out != b'':
	#print(out)

	out2 =[hex(ord(c)) for c in out]
	#print(out2)
	out3=""
	for d in out2:
		out3 = out3 + "/"+ d

	#PRUEBA  MEJORAR WEB
	out4 = 'Content-type: text/html\n'+'<html>\n'+'<body>\n'+'<p>Aqui esta la lectura:</p>\n'+'<ul>\n'+'<h2><li>La lectura es: "%s".</li></h2>' % out3 + '</ul>\n'+'<form>\n'+'<input value="Reload Page" onclick="history.go(0)" type="button">\n'+'</form>\n'+ '</body>\n'+'</html>'

	RFID.close()
	return out4


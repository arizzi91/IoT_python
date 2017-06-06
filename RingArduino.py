import os, RPi.GPIO as GPIO, time, datetime
import MySQLdb
import serial

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

path = '/var/www/html/IoTProject/'
http_path = 'http://192.168.1.69/IoTProject/'

if __name__ == '__main__':
	while True:
		if (arduinoSerialData.readline() is not None):
			bright = arduinoSerialData.readline()
			brightfloat = float(bright)
			bright_norm= int(round((1-(brightfloat/1023))*100))
			ts = time.time()
			im_name = 'screen' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S') + '.jpg'
			packet = http_path + im_name
			os.system("python3 Publisher.py %s" % packet)
			com = 'sudo fswebcam -r 640x480 -S 15 -s brightness=' +str(bright_norm)+'%  --shadow screen.jpg ' + path + im_name
			os.system(com)
			pth = "\'" + packet + "\'"
			db = MySQLdb.connect(host = "localhost", user = "root", passwd = "raspberry", db = "iot_database")
			cur = db.cursor()
			cur.execute("insert into Images (PATH) values(" + pth + ")")
			db.commit()
			db.close()

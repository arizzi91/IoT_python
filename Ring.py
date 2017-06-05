import os, RPi.GPIO as GPIO, time, datetime
import MySQLdb

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

path = '/var/www/html/IoTProject/'
http_path = 'http://192.168.1.69/IoTProject/'

if __name__ == '__main__':
	while True:
		if GPIO.input(18) == False:
			ts = time.time()
			im_name = 'screen' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S') + '.jpg'
			packet = http_path + im_name
			os.system("python3 Publisher.py %s" % packet)
			com = 'sudo fswebcam -r 640x480 -S 15 --shadow screen.jpg ' + path + im_name
			os.system(com)
			pth = "\'" + packet + "\'"
			db = MySQLdb.connect(host = "localhost", user = "root", passwd = "raspberry", db = "iot_database")
			cur = db.cursor()
			cur.execute("insert into Images (PATH) values(" + pth + ")")
			db.commit()
			db.close()

import logging, asyncio, os, MySQLdb

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0

"""
def_config = {
	'keep_alive': -1,
	'auto_reconnect': True,
	'reconnect_max_interval': 2,
	'reconnect_retries': 10
	}
"""


def uptime_coro():
	C = MQTTClient(client_id = 'pero')
	yield from C.connect('mqtt://127.0.0.1:5000',cleansession = False)
	yield from C.subscribe([('query', QOS_0)])
	urlPack = ""
	while True:
		try:
			message = yield from C.deliver_message()
			query = message.publish_packet
			print(query.payload.data.decode("utf-8"))
			db = MySQLdb.connect(host = "localhost", user = "root", passwd = "raspberry", db = "iot_database")
			cur = db.cursor()
			cur.execute(query.payload.data.decode("utf-8"))
			print("------"+str(cur.rowcount)+"------")
			if(cur.rowcount > 0):
				for value in cur.fetchall():
						urlPack = urlPack + "::" + value[0]
				os.system("python3 Publisher.py %s" % urlPack)
				urlPack = ""
			else:
				os.system("python3 Publisher.py \'Nessun risultato trovato\'")

		except ClientException as ce:
			yield from C.unsubscribe(['ring'])
			yield from C.disconnect()
			db.close()
			print("Client exception: %s" % ce)

if __name__ == '__main__':
	asyncio.get_event_loop().run_until_complete(uptime_coro())

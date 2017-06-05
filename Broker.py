from hbmqtt.broker import Broker
import logging, asyncio, os


def_config = {
	'listeners':{
		'default':{
			'type':'tcp',
			'max_connections':10
		},
		'my-listener1':{
			'bind':'192.168.1.69:5000'
		},
		'my-listener2':{
			'bind':'127.0.0.1:5000'
			}
	},
	'auth':{
		'plugins':['auth-anonymous'],
		'allow-anonymous':True,
		}
	}


broker = Broker(def_config)

def broker_coro():
	yield from broker.start()

try:
	if __name__ == '__main__':
		formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
		logging.basicConfig(level=logging.INFO, format=formatter)
		asyncio.get_event_loop().run_until_complete(broker_coro())
		asyncio.get_event_loop().run_forever()

except hbmqtt.broker.BrokerException as e:
	print(e)
	asyncio.get_event_loop().run_until_complete(broker.shutdown())
	input()

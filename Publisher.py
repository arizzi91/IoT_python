import logging, asyncio, sys

from hbmqtt.client import MQTTClient, ConnectException
from hbmqtt.mqtt.constants import QOS_0

logger = logging.getLogger(__name__)

def pub_link():
	try:
		C = MQTTClient()
		ret = yield from C.connect('mqtt://127.0.0.1:5000',cleansession = False)
		message = yield from C.publish('ring', sys.argv[1].encode(), qos = QOS_0)
		logger.info("Message published.")
		yield from C.disconnect()

	except ConnectException as ce:
		logger.error("Connection failed: %s" % ce)
		asyncio.get_event_loop().stop()


if __name__ == "__main__":
	formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
	logging.basicConfig(level=logging.DEBUG, format=formatter)
	asyncio.get_event_loop().run_until_complete(pub_link())
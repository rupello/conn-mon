import zmq
import random
import os
import time

port =  os.environ["CM_PORT_PUBLISHER"]

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:%s" % port)
publisher_id = random.randrange(0,9999)
while True:
    topic = random.randrange(1,10)
    messagedata = "server#%s" % publisher_id
    print("%s %s" % (topic, messagedata))
    socket.send_multipart(["%d" % topic, "%s" % messagedata])
    time.sleep(1)
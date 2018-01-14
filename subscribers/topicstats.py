import time
import sys
import os
import zmq

from util.ratecounter import RateCounter

port =  os.environ["CM_PORT_SUBSCRIBER"]

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)

# subscribe to all topics
socket.setsockopt(zmq.SUBSCRIBE, '')

report_interval = 5.
stats = {}
start=time.time()
while True:
    [topic, messagedata] = socket.recv_multipart()
    stats.setdefault(topic,RateCounter()).update(len(messagedata))
    if time.time()-start > report_interval:
      for t in stats:
        print("topic:{} -> {}".format(t,stats[t].report()))
        stats[t].reset()
      start=time.time()

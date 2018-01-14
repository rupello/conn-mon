"""a generic subscriber that listens on a given port & topics"""
import sys
import zmq

port =  sys.argv[1]
topics = sys.argv[2].split(",")

assert(int(port)>0), "usage subscriber.py "
assert(len(topics))

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)

for topic in topics:
  socket.setsockopt(zmq.SUBSCRIBE, topic)

for update_nbr in range(1000):
    [topic, messagedata] = socket.recv_multipart()
    print(topic, messagedata)
    sys.stdout.flush()
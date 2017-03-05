import sys
import zmq

port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)
topicfilter = b"9"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
for update_nbr in range(1000):
    string = socket.recv()
    topic, messagedata = string.split()
    print(topic, messagedata)
    sys.stdout.flush()
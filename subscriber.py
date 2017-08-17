import sys
import zmq

port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)

# subscribe to topics 5, 7 & 9
socket.setsockopt(zmq.SUBSCRIBE, b"5")
socket.setsockopt(zmq.SUBSCRIBE, b"7")
socket.setsockopt(zmq.SUBSCRIBE, b"9")

for update_nbr in range(1000):
    [topic, messagedata] = socket.recv_multipart()
    print(topic, messagedata)
    sys.stdout.flush()
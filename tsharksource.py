import subprocess
import json
import zmq

if __name__ == '__main__':
  context = zmq.Context()
  socket = context.socket(zmq.PUB)
  socket.connect("tcp://localhost:5559")

  proc = subprocess.Popen(['tshark', '-T', 'ek', '-Y', 'tcp.flags.syn==1 and tcp.flags.ack==0'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
  while proc.poll() is None:
      try:
	  packet = json.loads(proc.stdout.readline())
	  print(packet['layers']['ip'][u'ip_text'])
	  socket.send_multipart(["7", str(packet['layers']['ip']['ip_text'])])
      except Exception as exc:
	  pass

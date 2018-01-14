import argparse
import os
import time

import zmq

from util.ratecounter import RateCounter

port =  os.environ["CM_PORT_PUBLISHER"]

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-r","--rate",action="store")
  args = parser.parse_args()

  if args.rate is None:
    args.rate = 10

  context = zmq.Context()
  socket = context.socket(zmq.PUB)
  socket.connect("tcp://localhost:%s" % port)

  interval = 1.0/args.rate
  message = "{'text' : 'The boy stood on the burning deck'}"
  rc = RateCounter()
  while True:
    tstart = time.time()
    socket.send_multipart(["perftest",message])

    rc.update(len(message))
    if rc.count > args.rate:
      rc.report()
      rc.reset()

    tend = time.time()
    if (tend-tstart) < interval:
      time.sleep(interval-(tend-tstart))

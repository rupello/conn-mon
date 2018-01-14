import sys
import os
import subprocess
import json
import zmq
import argparse

port =  os.environ["CM_PORT_PUBLISHER"]

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-p","--pcap",action="store")
  args = parser.parse_args()

  # where are the packets coming from?
  packet_source = []
  sync_packet_timestamps = False
  if args.pcap is not None:
    if not os.path.exists(args.pcap):
      raise Exception("{} pcap not found".format(args.pcap))
    else:
      packet_source = ['-r',args.pcap]
      sync_packet_timestamps = True
  else:
    pass # todo add a command line to specify a live net iface

  # display filter
  # example:
  #   display_filter = ['Y','tcp.flags.syn==1 and tcp.flags.ack==0']
  display_filter = []

  context = zmq.Context()
  socket = context.socket(zmq.PUB)
  socket.connect("tcp://localhost:%s" % port)

  tshark_args = ['tshark'] + packet_source + ['-T', 'ek'] + display_filter
  proc = subprocess.Popen(tshark_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
  while proc.poll() is None:
    try:
      message = proc.stdout.readline().strip()
      if message:
        packet = json.loads(message)
        if packet.has_key('layers'):
          socket.send_multipart(["tshark",message])
      # todo: if we are reading from a pcap, delay for realtime
    except Exception as exc:
      print(exc)
      print(message)

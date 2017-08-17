"""Send selected item data to a zmq endpoint"""
from __future__ import print_function

import zmq
import json

# Local imports
from chains.sinks import sink
from chains.utils import net_utils

class ZMQSink(sink.Sink):
    """Print packet information"""

    def __init__(self, endpoint, topic):
        """Initialize PacketSummary Class"""

        # Call super class init
        super(ZMQSink, self).__init__()

        self.endpoint = endpoint
        self.topic = topic


    def pull(self):
        """Print out summary information about each packet from the input_stream"""
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.connect(self.endpoint)

        # For each packet in the pcap process the contents
        for item in self.input_stream:
            socket.send_multipart([self.topic,json.dumps(item['packet']['type'])])

def test():
    """Test for PacketSummary class"""
    from chains.sources import packet_streamer
    from chains.links import packet_meta
    from chains.links import reverse_dns
    from chains.utils import file_utils

    # Create a PacketStreamer and set its output to PacketSummary input
    data_path = file_utils.relative_dir(__file__, 'pcaps/udp.pcap')

    streamer = packet_streamer.PacketStreamer(iface_name=data_path, max_packets=50)
    meta = packet_meta.PacketMeta()
    rdns = reverse_dns.ReverseDNS()
    printer = ZMQSink("tcp://localhost:5559","7")

    # Set up the chain
    meta.link(streamer)
    rdns.link(meta)
    printer.link(rdns)

    # Pull the chain
    printer.pull()

if __name__ == '__main__':
    test()

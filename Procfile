# use honcho start <this file>
#    https://honcho.readthedocs.io/en/latest/index.html
#
# *** Important: set PYTHONUNBUFFERED=1 in your .env file!

# zeromq device to fwd published messages to all subscribers
forwarder: python forwarder_device.py

# this will start a subscriber for each websocket connection
websocketsrv: websocketd --devconsole --port="$CM_PORT_WEBSCKT" --loglevel debug python ./subscribers/subscriber.py $CM_PORT_SUBSCRIBER "tshark"

# reports stats on all topics to stdout
stats: python ./subscribers/topicstats.py

# publish some random messages to the system
publisher: python ./publishers/publisher.py

# publish packets from tshark
tshark: python ./publishers/tsharksource.py

# publish a test stram of messages at a fixed rate
perfsource: python ./publishers/perfsource.py

# start the web server
web: python -m SimpleHTTPServer # python 2
#web: python -m http.server     # python 3


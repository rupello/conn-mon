# use honcho start <this file>
#    https://honcho.readthedocs.io/en/latest/index.html

# zeromq device to fwd published messages to all subscribers
forwarder: python forwarder_device.py

# this will start a subscriber for each websocket connection
websocketsrv: websocketd --port="$CM_PORT_WEBSCKT" python subscriber.py

# publish some input messages to the system
publisher: PYTHONUNBUFFERED=true python publisher.py

# start the web server
web: python -m SimpleHTTPServer # python 2
#web: python -m http.server     # python 3


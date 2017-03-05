import subprocess
import time
import os
import sys

if __name__ == '__main__':
    py = sys.executable
    proxy = os.path.join(os.getcwd(), 'forwarder_device.py')
    server = os.path.join(os.getcwd(), 'forwarder_server.py')
    subscriber = os.path.join(os.getcwd(), 'forwarder_subscriber.py')
    assert os.path.exists(proxy)
    assert os.path.exists(server)
    assert os.path.exists(subscriber)

    # zmq proxy
    subprocess.Popen([py, proxy])

    # zmq server (the message source)
    subprocess.Popen([py, server])

    # the websocketd -> starts a subscriber for each new ws connection
    subprocess.Popen(['websocketd','--port=8008', py, subscriber])

    # webserver
    subprocess.Popen([py ,'-m','http.server'])

    while(True):
        time.sleep(1.)
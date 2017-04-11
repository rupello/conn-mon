import zmq
import os

def main():

    pub_facing_port =  os.environ["CM_PORT_PUBLISHER"]
    sub_facing_port =  os.environ["CM_PORT_SUBSCRIBER"]

    try:
        context = zmq.Context(1)

        # Socket facing publishers
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:%s" % pub_facing_port)

        frontend.setsockopt(zmq.SUBSCRIBE,b"")

        # Socket facing subscribers
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:%s" % sub_facing_port)

        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()


if __name__ == "__main__":
    main()
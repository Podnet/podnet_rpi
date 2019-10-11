"""Podnet Library for Raspberry Pi"""

import json
import time
from RF24 import *
from RF24Network import *

octlit = lambda n: int(n, 8)
POD_ADDRESS = octlit("00")
DEFAULT_STRING_ENCODING = "utf-8"


class UnconfiguredNodeException(Exception):
    pass


def chunkstring(string, length):
    return (string[0 + i : length + i] for i in range(0, len(string), length))


class Podnet:
    def __init__(self, thing_id, debug=False):
        radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)
        network = RF24Network(radio)

        self.thing_id = thing_id
        self.radio = radio
        self.network = network
        self.node_id = octlit("01")

        radio.begin()
        time.sleep(0.1)
        network.begin(90, self.node_id)
        if debug:
            radio.printDetails()

        # Asking Pod for next available address
        if debug:
            print("Sending msg to Pod for new Node ID assignment.")
        network.update()
        msg = json.dumps({"tid": self.thing_id, "m": "assignNodeID"})

        if self.sendWithRetryToPod(msg):
            print("Assign NodeID msg sent")
        else:
            raise UnconfiguredNodeException("Unable to send msg for assigning Node ID.")

        # network.write(RF24NetworkHeader(POD_ADDRESS), msg)
        time.sleep(1)

        # Listen for response from Pod
        if debug:
            print("Waiting for response from Pod for Node ID")

        if debug:
            print("Listening for NodeID response...")
        while True:
            network.update()
            if network.available():
                if debug:
                    print("Received a response.")
                try:
                    header, payload = network.read(100)
                    msg = payload.decode(DEFAULT_STRING_ENCODING)
                    resp = json.loads(msg)
                    self.node_id = octlit(str(resp["response"]))
                    if debug:
                        print("Changing Node ID...")
                    network.begin(90, self.node_id)
                    break
                except json.decoder.JSONDecodeError:
                    print("Unable to decode JSON msg.")
                    raise UnconfiguredNodeException(
                        "Unable to configure node because response from Pod could not be parsed."
                    )
            time.sleep(1)

        # Case when new address wasn't assigned
        if self.node_id == octlit("01"):
            raise UnconfiguredNodeException(
                "This node is unconfigured. No Node ID was assigned by Pod."
            )

        print("Node configured.")

    def sendWithRetryToPod(self, msg, msg_type=0, retry=5):
        """Retries for given no. of times before returning False."""
        if isinstance(msg, str):
            msg = msg.encode(DEFAULT_STRING_ENCODING)

        attempts = 0
        while not self.network.write(RF24NetworkHeader(octlit("00"), msg_type), msg):
            if attempts > retry:
                return False
            attempts += 1
            time.sleep(1)

        return True

    def sendMultipartMessage(self, msg, debug=False):
        parts = list(chunkstring(msg, 72))
        part_sent = list()

        # Msg has only one part
        if len(parts) == 1:
            return self.sendWithRetryToPod(parts[0])

        # Msg has multiple parts
        else:
            i = 0
            while i < len(parts):
                # Send last msg with header.type = 80
                if i == (len(parts) - 1):
                    part_sent.append(self.sendWithRetryToPod(parts[i], 80))

                # All other msgs have header.type = 79
                else:
                    part_sent.append(self.sendWithRetryToPod(parts[i], 79))

                if debug:
                    print(str(parts[i]) + " : " + str(part_sent[i]))

                i += 1
                time.sleep(1)

        return all(part_sent)

    def sendToCloud(self, msg, debug=False):
        data = json.dumps({"tid": self.thing_id, "p": msg, "m": "sendToCloud"})
        return self.sendMultipartMessage(data, debug=debug)

    def sendTo(self, msg, other_thing_id, debug=True):
        data = json.dumps({"tid": self.thing_id, "p": msg, "m": "sendTo", "otid": other_thing_id})
        return self.sendMultipartMessage(data, debug=debug)


    def recv(self):
        while True:
            self.network.update()
            if self.network.available():
                header, payload = self.network.read(144)
                return payload.decode(DEFAULT_STRING_ENCODING)

            time.sleep(0.2)

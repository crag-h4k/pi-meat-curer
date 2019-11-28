#/usr/bin/python3

from time import sleep
from sys import argv
from datetime import datetime, timedelta

from Relay import Relay


if __name__ == '__main__':
    relay_no = "RELAY" + argv[1]
    R = Relay(relay_no)
    try:
        R.on()
        while True:
            pass;
    except KeyboardInterrupt:
        R.off()


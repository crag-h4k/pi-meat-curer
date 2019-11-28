#/usr/bin/python3

from time import sleep
from sys import argv
from datetime import datetime, timedelta

from Relay import Relay


if __name__ == '__main__':
    relay_no = "RELAY" + argv[1]
    limit = int(argv[2])
    i = 1
    R = Relay(relay_no)

    while i  <= limit:
        print("Test {}, {}".format(i, relay_no))
        i += 1
        R.on()
        sleep(1)
        R.off()
        sleep(1)


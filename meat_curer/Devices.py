#!/usr/bin/python3

import RPi.GPIO as GPIO
from Adafruit_DHT import DHT22, read_retry


PinAssignments = {
        'HT1': 3,
        'FAN1': 2,
        'RELAY1': 22,
        'RELAY2': 27,
        'RELAY3': 17,
        'RELAY4': 4,
        }

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Relay:
    # bcm mode pins
    def __init__(self, pin: int):
        self.pin = pin
        self.state = 'LOW'
        GPIO.setup(self.pin, GPIO.OUT)
        #GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        if self.state == 'HIGH':
            #print('state already {}'.format(self.state))
            return
        self.state = 'HIGH'
        GPIO.output(self.pin, GPIO.HIGH)
        #return 'HIGH'

    def off(self):
        if self.state == 'LOW':
            #print('state already {}'.format(self.state))
            return
        self.state = 'LOW'
        GPIO.output(self.pin, GPIO.LOW)


class HTSensor:
    def __init__(self, pin: int):
        self.pin = pin

    def humidity(self) -> float:
        return read_retry(DHT22, self.pin)[0]

    def temperature(self) -> float:
        return read_retry(DHT22, self.pin)[1]


if __name__ == '__main__':
    ht = HTSensor(PinAssignments.get('HT1'))
    h = ht.humidity()
    t = ht.temperature()
    print('Humidity: {}\nTemperature: {}'.format(h,t))

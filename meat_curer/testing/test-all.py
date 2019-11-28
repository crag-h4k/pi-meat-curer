#/usr/bin/python3

from time import sleep

from Devices import Relay, HTSensor, PinAssignments


if __name__ == '__main__':
    relay_pins = [22, 27, 17 , 4]
    ht_pin = 3

    for p in range(4):
        relay_no = 'RELAY' + str(p + 1)
        r_pin = PinAssignments.get(relay_no)
        R = Relay(r_pin)

        print('Relay {}: ON'.format(relay_no))
        R.on()
        sleep(1)
        R.off()
        sleep(1)

    ht = HTSensor(ht_pin)
    h = ht.humidity()
    t = ht.temperature()
    print('Humidity: {}\nTemperature: {}'.format(h,t))

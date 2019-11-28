#/usr/bin/python3

from time import sleep

from Devices import Relay, HTSensor, PinAssignments
from Meat import Meat
from check_environment import check_temp, check_hum, check_env 


def execute_commands(func_kv: dict, flags: list):
    for flag in flags:
        if flag not in func_kv:
            continue
        func = func_kv.get(flag)
        func()


if __name__ == '__main__':
    compressor = Relay(PinAssignments.get('RELAY1'))
    humidifier = Relay(PinAssignments.get('RELAY2'))
    fan = Relay(PinAssignments.get('RELAY3'))
    lamp = Relay(PinAssignments.get('RELAY4'))

    meat = Meat('LOMO')
    limit = 1000
    commands = {
            'FAN_ON': fan.on,
            'FAN_OFF': fan.off,
            'HUM_ON': humidifier.on,
            'HUM_OFF': humidifier.off,
            'COMP_ON': compressor.on,
            'COMP_OFF': compressor.off,
            'LAMP_ON': lamp.on,
            'LAMP_OFF': lamp.off,
        }
    try:
        for i in range(limit):
            sleep(1)
            ht_1 = HTSensor(PinAssignments.get('HT1'))
            temp = ht_1.temperature()
            hum = ht_1.humidity()
            current_cmds = check_env(temp, hum, meat)
            print(temp, hum, current_cmds, end='\r')
            execute_commands(commands, current_cmds)

    # turn all relay's off
    finally:
        compressor.off()
        lamp.off()
        fan.off()
        humidifier.off()

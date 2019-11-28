#!/usr/bin/python3

#Dry Cured Meat (Whole Muscle)           50-61°F/10-16°C     60-80%
#Dry Cured Salami (after fermentation)   50-61°F/10-16°C     60-80%
#Jerky and Biltong                       61-122°F/16-50°C    30-50%

from datetime import timedelta

class Meat:
    all_ranges = {
        'LOMO': {'duration': timedelta(weeks=6),
            'airflow': .20,
            't_low': 10.0, 't_high': 16.0,
            'h_low': 60.0, 'h_high': 80.0},
        'JERKY': {'duration': timedelta(days=2),
            'airflow': 1.00,
            't_low': 16.0, 't_high': 50.0,
            'h_low': 30.0, 'h_high': 50.0 },
        'MEAT': {'duration': timedelta(weeks=10),
            'airflow': .20,
            't_low': 10.0, 't_high': 16.0,
            'h_low': 60.0, 'h_high': 80.0},
        'SALAMI': {'duration': timedelta(weeks=10),
            'airflow': .30,
            't_low': 10.0, 't_high': 16.0,
            'h_low': 60.0, 'h_high': 80.0}
        }

    def __init__(self, meat_type):
        self.meat_type = meat_type
        self.ranges = self.all_ranges[meat_type]
        self.duration = self.ranges.get('duration')
        self.airlow = self.ranges.get('airflow')
        self.t_low = self.ranges.get('t_low')
        self.t_high = self.ranges.get('t_high')
        self.h_low = self.ranges.get('h_low')
        self.h_high = self.ranges.get('h_high')

if __name__ == '__main__':

    from pprint import pprint
    from sys import argv

    meat_type = argv[1]

    meat = Meat(meat_type)
    print(meat.ranges)
    print(meat.duration)
    print(meat.airlow)
    print(meat.t_low)
    print(meat.t_high)
    print(meat.h_low)
    print(meat.h_high)


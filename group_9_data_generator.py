'''
Group 9 - Reid Williams, Nicole Parsons, Brenton Hauth

Description:  This program contains a model for speed generation.
'''
import matplotlib.pyplot as plt
import random
from random import randint
import time
import group_9_util as util

class Speedometer:
    def generator(self,increment = True) -> float:
        if increment:
            self.value['base'] +=  self.value['delta']
        else:
            self.value['base'] -= self.value['delta']
        return self.value['base']



    

    def create_data(self):
        '''Creates a payload to be sent'''
        

        # Gets random first & last name
        first = self.random_first_names[randint(0, len(self.random_first_names) - 1)]
        last = self.random_last_names[randint(0, len(self.random_last_names) - 1)]
       
        

        self.start_id += 1
        
        try:
            speed=next()

            payload = {
                        'data': {
                            'id': self.start_id,
                            'timestamp': int(time.time()),  # timestamp
                            'speed': speed, # Random speed
                            'unit': 'km/h', # speed unit
                            'name': f'{first} {last}', # random person
                            'vehicle': { # vehicle info
                                'fuel_in_litres': randint(10, 80),
                                'model': f'{chr(randint(65, 90))}-{randint(15, 50) * 100}',
                                # random hex and removes 0x
                                'plate': hex(randint(0x100000, 0xFFFFFF)).upper()[2:]
                            }
                        }
                    }

            return util.ok(payload)#wraps payload with ok and code
        except:
            msg = "Something went wrong."
            return util.response(None, code=500, msg=msg)#don't send data

        #return payload

    

    def next(self, error_rate=0.1) -> float:
    # genrates a numbeer between 0.0 and 1.0
        if random.random() <= error_rate:
            raise Exception()
        else:
            r = self.speeds[randint(0, len(self.speeds) - 1)]
            return self.speeds[r]
    
        
    def __init__(self, sample_size = 0, speed = 0):
        """
        This is the class constructor.
        """
        self.sample_size = sample_size
        self.dataset = []
        self.value = {'base':speed, 'delta':0.15}
        self.speeds=[self.generator((x % random.gauss(250, 100)) ) for x in range(self.sample_size)]#### will always be doing about highway speed
        self.start_id = 67  # my favorite number is 67


        self.random_first_names = [
            'Kathleen',
            'Tia',
            'Leandro',
            'Ramiro',
            'Elvis',
            'Dylan',
            'Dayana',
            'Craig',
            'Mariela',
            'Adrienne',
            'Clinton',
            'Jamari',
        ]

        self.random_last_names = [
            'Hickman',
            'Austin',
            'Garner',
            'Bernard',
            'Ross',
            'Pittman',
            'Higgins',
            'Atkins',
            'Meza',
            'Park',
            'Torres',
            'Kirby',
        ]
        


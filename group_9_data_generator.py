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
        try:
            speed=self.next()

            payload = {
                'id': util.uid(),
                'timestamp': int(time.time()),  # timestamp
                'speed': speed, # Random speed
                'unit': 'km/h', # speed unit
                'name': self.name, # random person
                'vehicle': self.vehicle_info
            }

            return util.ok(payload) #wraps payload with ok and code
        except Exception as e:
            return util.response(None, code=500, msg=str(e))#don't send data

        #return payload

    

    def next(self, error_rate=0.1) -> float:
        # genrates a numbeer between 0.0 and 1.0
        if random.random() <= error_rate:
            raise Exception()
        else:
            r = randint(0, len(self.speeds) - 1)
            return self.speeds[r]
    
        
    def __init__(self, sample_size = 0, speed = 0):
        """
        This is the class constructor.
        """
        self.sample_size = sample_size
        self.dataset = []
        self.value = {'base':speed, 'delta':0.15}
        self.vehicle_info = util.rand_vehicle()
        self.name = util.rand_name()
        self.speeds=[self.generator((x % random.gauss(250, 100)) ) for x in range(self.sample_size)]#### will always be doing about highway speed
        


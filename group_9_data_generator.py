'''
Group 9 - Reid Williams, Nicole Parsons, Brenton Hauth

Description:  This program contains a model for speed generation.
'''
import matplotlib.pyplot as plt
import random

class Speedometer:
    def generator(self,increment = True) -> float:
        if increment:
            self.value['base'] +=  self.value['delta']
        else:
            self.value['base'] -= self.value['delta']
        return self.value['base']

    def generate_data(self, increment = True):
        """
        This method generates example data and displays it on a graph.
        """
        y = [self.generator((x % random.gauss(250, 100)) ) for x in range(self.sample_size)]#### will always be doing about highway speed
        self.dataset = y
        return y
        #plt.plot(y, 'r')
        #plt.show()

    def next(self, error_rate=0.1) -> float:
        # genrates a numbeer between 0.0 and 1.0
        if random.random() <= error_rate:
            raise Exception()
        else:
            r = random.randint(0, len(self.sample_size) - 1)
            return self.dataset[r]
        
    def __init__(self, sample_size = 0, speed = 0):
        """
        This is the class constructor.
        """
        self.sample_size = sample_size
        self.dataset = []
        self.value = {'base':speed, 'delta':0.15}
        

if __name__ == '__main__':
    speedometer = Speedometer(100, 300)
    speedometer.generate_data()

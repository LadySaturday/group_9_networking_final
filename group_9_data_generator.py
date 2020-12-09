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
        y = [self.generator((x % random.gauss(50, 5.0)) > 24) for x in range(self.sample_size)]
        #plt.plot(y, 'r')
        #plt.show()
        
        
    def __init__(self, sample_size = 0, speed = 0):
        """
        This is the class constructor.
        """
        self.sample_size = sample_size
        self.value = {'base':speed, 'delta':0.15}
        


speedometer = Speedometer(500, 50)
speedometer.generate_data()

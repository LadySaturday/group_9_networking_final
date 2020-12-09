'''
Group 9 - Reid Williams, Nicole Parsons, Brenton Hauth

Description:  This program contains line chart of a dynamic data set.
'''

import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import FormatStrFormatter
import tkinter as Tk
import array
import random
import threading
import sched, time

class DynamicDisplayOG:
    def __init__(self):
        self.s = sched.scheduler(time.time, time.sleep)
        self.constValues = [50,200,40,59,123,165]#test values
        self.counter = 1
        self.root = Tk.Tk()
        self.f = Figure(figsize=(3,4), dpi=100)
        self.ax = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.root)
        self.xCol = []
        self.yCol = []
        self.maxValues=5


    def changeList(self):
        self.constValues.pop(0)  
        self.constValues.append(random.randint(0, 300))
        self.show_bar(self.constValues) 
        self.root.after(500, self.changeList) 

    def add_value(self, val):
        pass  # TODO: add a value to the graph

    def show_bar(self, data):
        self.ax.clear()
        self.counter += 1

        if(len(self.yCol) > self.maxValues):
            self.xCol.pop(0)
            self.yCol.pop(0)

        
        self.xCol.append(self.counter)   
        self.yCol.append(data[5])
        
        #canvas.draw()   
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.NONE, expand=0.5)
        self.canvas.get_tk_widget().pack_forget()
        self.f = Figure(figsize=(8,6), dpi=100)
        self.ax = self.f.add_subplot(111)
        self.ax.set_ylim(0, 300)  # limit fixed height
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%d km/hr'))
        self.canvas = FigureCanvasTkAgg(self.f, master=self.root)
        self.ax.plot(self.xCol,self.yCol, label="Speed", color='g')
        self.ax.set_xlabel("Trial")
        self.ax.tick_params(axis = "x", which = "both", bottom = False, top = False, labelcolor='w')#only side ticks and labels
        self.canvas.draw()   
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.NONE, expand=0.5)

    def start(self):
        self.show_bar(self.constValues)

        #thread
        t = threading.Thread(target=self.changeList())
        t.setDaemon(True)
        t.start()
        self.root.mainloop()

og = DynamicDisplayOG()
og.start()
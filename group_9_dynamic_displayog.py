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
        # self.s = sched.scheduler(time.time, time.sleep)
        self.constValues = [50, 200, 40, 59, 123, 165]#test values
        self.counter = 0
        self.root = Tk.Tk()
        self.f = Figure(figsize=(3,4), dpi=100)
        self.ax = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.root)
        self.xCol = []
        self.yCol = []
        self.maxValues=5
        self.queue = []
        self.lastPlotted=0
        self.plotNew=True


    def changeList(self):
        self.add_value(random.randint(0, 300))
        self.root.after(500, self.changeList)

    def set_list(self, lst):
        self.show_bar(lst)
    

    def watch(self):
        if (self.plotNew):
            self.show_bar(self.constValues)
            self.plotNew=False
        self.root.after(500, self.watch)

    def add_value(self, val):
        if(val!=self.lastPlotted):
            if len(self.constValues) > 5:
                self.constValues.pop(0)
            self.constValues.append(val)
            self.plotNew=True
        # self.show_bar(self.constValues)

    def show_bar(self, data):
        self.ax.clear()
        self.counter += 1

        if len(self.yCol) > self.maxValues:
            self.xCol.pop(0)
            self.yCol.pop(0)

        
        self.xCol.append(self.counter)
        if len(data) > 0:
            self.yCol.append(data[-1])
        
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




        # print(f'TARGET: {target}')
        #thread
        # self.changeList()
        self.watch()
        #t = threading.Thread(target=None)
        # t = threading.Thread(target=start_tk, args=[self])
        # t.start()
        # return t
        # t.setDaemon(True)
        # t.start()
        self.root.mainloop()

def start_tk(dd):
    dd.show_bar(dd.constValues)
    dd.root.mainloop()

if __name__ == '__main__':
    og = DynamicDisplayOG()
    og.start()

    for i in range(10):
        x = random.randint(0, 100)
        og.add_value(x)
        time.sleep(1.5)
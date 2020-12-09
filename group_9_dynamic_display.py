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

s = sched.scheduler(time.time, time.sleep)
constValues = [50,200,40,59,123,165]#test values
global counter
counter = 1
root = Tk.Tk()
f = Figure(figsize=(3,4), dpi=100)
ax = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=root)
xCol = []
yCol = []
maxValues=5

def changeList():
    global constValues   
    constValues.pop(0)  
    constValues.append(random.randint(0,300))
    show_bar(constValues) 
    root.after(500,changeList) 
    

def show_bar(data):
    global ax
    global canvas
    global counter
    ax.clear()
    counter = counter + 1

    if(len(yCol)>maxValues):
        xCol.pop(0)
        yCol.pop(0)

    
    xCol.append(counter)   
    yCol.append(data[5])
    
    
    
    #canvas.draw()   
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.NONE, expand=0.5)
    canvas.get_tk_widget().pack_forget()
    f = Figure(figsize=(8,6), dpi=100)
    ax = f.add_subplot(111)
    ax.set_ylim(0, 300)  # limit fixed height
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d km/hr'))
    canvas = FigureCanvasTkAgg(f, master=root)
    ax.plot(xCol,yCol, label="Speed", color='g')
    ax.set_xlabel("Trial")
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False, labelcolor='w')#only side ticks and labels
    canvas.draw()   
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.NONE, expand=0.5)


#show_bar(constValues)

#thread
t = threading.Thread(target=changeList())
t.setDaemon(True)
t.start()
#Tk.mainloop() 
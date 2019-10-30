"""
===============
Embedding in Tk
===============

"""

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

def _quit():
    root.quit()     # stops mainloop
    root.destroy()

def tobinary(data):
    level=8
    x=bin(data).replace("0b","")
    y=str(x)
    l=[]
    t=level-len(y)
    for i in range(t):
        l.append(0)
    for i in y:
        l.append(int(i))
    print("for sample",data,"bits are ",l)
    return l

def _clear():
    plt.clf()
    

def showit():
    data=E1.get()
    d=[]
    for i in data:
        if(i!=' '):
            d.append(i)
    y4=[]
    y3=[]
    for i in d:
        r=ord(i)
        y4=tobinary(r)
        print(y4)
        for j in y4:
            y3.append(j)
    #y3=[]
    #x=data.split(" ")
    #for i in range(len(x)):
    #    y3.append(int(x[i]))
    y3.append(0)
    print(y3)
    xs1=[]
    ys1=[]
    plt2=fig.add_subplot(421)
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt1=fig.add_subplot(425)
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt2.set_title('Digital signal(Input)')
    plt1.set_title('Analog signal(output)')
    xs = np.repeat(range(len(y3)), 2)
    ys = np.repeat(y3, 2)
    xs1.append(0)
    ys1.append(0)
    for i in xs:
        xs1.append(i)
    for j in ys:
        ys1.append(j)
                #print(xs,ys)
    xs1 = xs1[1:]
    ys1 = ys1[:-1]
                #print(xs1,ys1)
    print(xs1,ys1)
    temp=0
    baseline=1.000000001
    plt2.plot(xs1,ys1)
    for i in range(len(y3)-1):
        x=np.arange(temp,temp+1.00000001,0.01)
        if y3[i]==1:
            y=np.sin(4*np.pi*x)*2
        else:
            y=np.sin(0*x*np.pi)*8
        temp=temp+1.000000001
        #print("x is ",x)
        #print("len of x ",len(x))
        #print("y is ",y)
        #print("len of y ",len(y))
        plt1.plot(x,y,c='b')
    # A tk.DrawingArea.
    canvas.draw()



root = tkinter.Tk()
frame=tkinter.Frame(root)
frame.pack(side=tkinter.TOP)
bottomframe=tkinter.Frame(root)
bottomframe.pack()
root.wm_title("Embedding in Tk")
L1 =tkinter.Label(frame, text="Data")#.grid(row=1,column=0)
L1.pack( side = tkinter.LEFT)
E1 = tkinter.Entry(frame, bd =5)#.grid(row=1,column=1)
E1.pack(side = tkinter.LEFT)

show=tkinter.Button(master=frame, text="Show", command=showit)
show.pack(side=tkinter.LEFT)

button = tkinter.Button(master=bottomframe, text="Quit", command=_quit)#.grid(row=2,column=0)
button.pack(side=tkinter.BOTTOM)

button = tkinter.Button(master=frame, text="Clear", command=_clear)#.grid(row=2,column=0)
button.pack(side=tkinter.LEFT)

fig=plt.figure()
##fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=bottomframe)
canvas.get_tk_widget().pack(side=tkinter.TOP,fill=tkinter.BOTH, expand=2)
#canvas.get_tk_widget().grid(row=3)
##toolbar = NavigationToolbar2Tk(canvas, root)
##toolbar.update()
##canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

##
##def on_key_press(event):
##    print("you pressed {}".format(event.key))
##    key_press_handler(event, canvas, toolbar)
##

##
##canvas.mpl_connect("key_press_event", on_key_press)


  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate





tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.

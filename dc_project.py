import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure
from tkinter import ttk
import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style

import numpy as np

style.use("ggplot")


LARGE_FONT=("Verdana",30)
M_FONT=("Verdana",12)

fig=Figure(figsize=(5,5), dpi=100)
fig=plt.figure()

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
    return l


class DC_Project(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        tk.Tk.wm_title(self,"DC_Project")
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (StartPage,PageOne,PageTwo):
            frame=F(container,self)

            self.frames[F]=frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        label=ttk.Label(self,text="Welcome to Signal Converter",font=LARGE_FONT)
        label.pack(pady=100,padx=10)

        
        self.button2=ttk.Button(self,text="Digital to Analog",width=30,
                          command=lambda: controller.show_frame(PageTwo))
        self.button2.pack(pady=10)


class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller

        self.label=tk.Label(self,text="Digital to Analog",font=LARGE_FONT)
        self.label.place(y=50,x=550)

        self.label=tk.Label(self,text="Data",font=M_FONT)
        self.label.place(y=200,x=450)

        self.data=tk.Entry(self,bd=1,width=50)
        self.data.place(x=700,y=200)

        self.label=tk.Label(self,text="Frequency(Carrier Wave)",font=M_FONT)
        self.label.place(y=300,x=450)

        self.freq=tk.Entry(self,bd=1,width=50)
        self.freq.place(x=700,y=300)
        self.freq.insert(0,'4')

        self.label=tk.Label(self,text="Highest Amp",font=M_FONT)
        self.label.place(y=400,x=450)

        self.amp1=tk.Entry(self,bd=1,width=50)
        self.amp1.place(x=700,y=400)
        self.amp1.insert(0,'8')

        self.label=tk.Label(self,text="Lowest Amp",font=M_FONT)
        self.label.place(y=500,x=450)

        self.amp2=tk.Entry(self,bd=1,width=50)
        self.amp2.place(x=700,y=500)
        self.amp2.insert(0,'0')
        
        self.button3=ttk.Button(self,text="Next",width=25,
                          command=lambda: self.go_to_page_one())
        self.button3.place(x=660,y=600)


        button1=ttk.Button(self,text="Back to Home",
                          command=lambda: controller.show_frame(StartPage))
        button1.place(x=700,y=650)


    def go_to_page_one(self):
        self.controller.Freq = self.freq.get() #save text from entry to some var
        self.controller.Amp1 = self.amp1.get() #save text from entry to some var
        self.controller.Amp2 = self.amp2.get() #save text from entry to some var
        self.controller.Data = self.data.get() #save text from entry to some var
        self.controller.frames[PageOne].digital() #call correct_label function
        self.controller.frames[PageOne].analog() #call correct_label function
        self.controller.frames[PageOne].both() #call correct_label function
        self.controller.show_frame(PageOne) #show page one

    
class PageOne(tk.Frame):

    
    def digital(self):
        plt.clf()
        data=self.controller.Data
        d=[]
        for i in data:
            if(i!=' '):
                d.append(i)
        y4=[]
        y3=[]
        for i in d:
            r=ord(i)
            y4=tobinary(r)
            for j in y4:
                y3.append(j)
        y3.append(0)
        xs1=[]
        ys1=[]
        plt2=fig.add_subplot(111)
        plt.xlabel('time (s)')
        plt.ylabel('Amplitude')
        plt2.set_title('Digital signal(Input)')
        xs = np.repeat(range(len(y3)), 2)
        ys = np.repeat(y3, 2)
        xs1.append(0)
        ys1.append(0)
        for i in xs:
            xs1.append(i)
        for j in ys:
            ys1.append(j)
        xs1 = xs1[1:]
        ys1 = ys1[:-1]
        temp=0
        baseline=1.000000001
        plt2.plot(xs1,ys1)

        self.canvas.draw()

        
    def analog(self):
        a1=int(self.controller.Amp1)
        a2=int(self.controller.Amp2)
        f=int(self.controller.Freq)
        plt.clf()
        data=self.controller.Data
        d=[]
        for i in data:
            if(i!=' '):
                d.append(i)
        y4=[]
        y3=[]
        for i in d:
            r=ord(i)
            y4=tobinary(r)
            for j in y4:
                y3.append(j)
        y3.append(0)
        xs1=[]
        ys1=[]
        plt1=fig.add_subplot(111)
        plt.xlabel('time (s)')
        plt.ylabel('Amplitude')
        plt1.set_title('Analog signal(output)')
        xs = np.repeat(range(len(y3)), 2)
        ys = np.repeat(y3, 2)
        xs1.append(0)
        ys1.append(0)
        for i in xs:
            xs1.append(i)
        for j in ys:
            ys1.append(j)
        xs1 = xs1[1:]
        ys1 = ys1[:-1]
        temp=0
        baseline=1.000000001
        for i in range(len(y3)-1):
            x=np.arange(temp,temp+1.00000001,0.01)
            if y3[i]==1:
                y=np.sin(f*np.pi*x)*a1
            else:
                y=np.sin(f*x*np.pi)*a2
            temp=temp+1.000000001
            plt1.plot(x,y,c='b')
        self.canvas.draw()

    
    def both(self):
        f=int(self.controller.Freq)
        a1=int(self.controller.Amp1)
        a2=int(self.controller.Amp2)
        plt.clf()
        data=self.controller.Data
        d=[]
        for i in data:
            if(i!=' '):
                d.append(i)
        y4=[]
        y3=[]
        for i in d:
            r=ord(i)
            y4=tobinary(r)
            print("the binary conversion of ",i," is ",y4) 
            for j in y4:
                y3.append(j)
        y3.append(0)
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
        xs1 = xs1[1:]
        ys1 = ys1[:-1]
        temp=0
        baseline=1.000000001
        plt2.plot(xs1,ys1)
        for i in range(len(y3)-1):
            x=np.arange(temp,temp+1.00000001,0.01)
            if y3[i]==1:
                y=np.sin(f*np.pi*x)*a1
            else:
                y=np.sin(f*x*np.pi)*a2
            temp=temp+1.000000001
            plt1.plot(x,y,c='b')
        self.canvas.draw()
        
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)

        label=tk.Label(self,text="Signals",font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        self.canvas=FigureCanvasTkAgg(fig,self)
        button2=ttk.Button(self,text="Digital Signal",
                          command= lambda:self.digital(),width=25)
        button2.pack(pady=5)

        button4=ttk.Button(self,text="Analog Signal",
                          command= lambda:self.analog(),width=25)
        button4.pack(pady=5)

        button5=ttk.Button(self,text="Both Signal",
                          command= lambda:self.both(),width=25)
        button5.pack(pady=5)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        

        button3=ttk.Button(self,text="Previous",
                          command=lambda: controller.show_frame(PageTwo))
        button3.pack(pady=5)

        button1=ttk.Button(self,text="Back to Home",
                          command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        self.toolbar=NavigationToolbar2Tk(self.canvas,self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
                    

app=DC_Project()
app.mainloop()
    

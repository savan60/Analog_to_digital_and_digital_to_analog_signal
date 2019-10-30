import matplotlib.pyplot as plt
import numpy as np
import math
from IPython.display import HTML

def tobinary(data,level):
    x=bin(data).replace("0b","")
    y=str(x)
    l=[]
    t=int(level)-len(y)
    for i in range(t):
        l.append(0)
    for i in y:
        l.append(int(i))
    print("for sample",data,"bits are ",l)
    return l

print("----------------------Welcome to Digital Electronic project---------------------------")
print("\n\n")

b=True
c=True
while(b):
    print("1.To convert Digital Signal to Analog Signal\n2.To convert Analog Signal to Digital Signal\n9.exit")
    input_var=int(input())
    print()
    if(input_var==1):
        while(c):
            print("1.To run 9.exit")
            inp=int(input())
            print()
            if(inp==1):
                print("Give the value of bits seperated with spaces")
                data=[int(j) for j in input().split()]
                print()
                print("Value of frequency of carrier wave")
                f=int(input())
                print()
                print("value of highest amp")
                amp1=int(input())
                print()
                print("value of lowest amp")
                amp2=int(input())
                data.append(0)
                xs1=[]
                ys1=[]
                fig = plt.figure()
                pt2=fig.add_subplot(421)
                plt.xlabel('time (s)')
                plt.ylabel('Amplitude')
                pt2.set_title('Digital signal(Input)')
                plt1=fig.add_subplot(425)
                plt.xlabel('time (s)')
                plt.ylabel('Amplitude')
                plt1.set_title('Analog signal(output)')
                temp=0
                baseline=1.000000001
                for i in range(len(data)-1):
                    x=np.arange(temp,temp+1.00000001,0.01)
                    if data[i]==1:
                        y=np.sin(f*np.pi*x)*amp1
                    else:
                        y=np.sin(f*x*np.pi)*amp2
                    temp=temp+1.000000001
                    #print("x is ",x)
                    #print("len of x ",len(x))
                    #print("y is ",y)
                    #print("len of y ",len(y))
                    
                    plt1.plot(x,y,c='b')

                xs = np.repeat(range(len(data)), 2)
                ys = np.repeat(data, 2)
                xs1.append(0)
                ys1.append(0)
                if(data[0]==1):
                    for i in xs:
                        xs1.append(i)
                    for j in ys:
                        ys1.append(j)
                #print(xs,ys)
                xs1 = xs1[1:]
                ys1 = ys1[:-1]
                #print(xs1,ys1)

                pt2.plot(xs1, ys1)
                print("\n\n")
                plt.show()
                
            elif(inp==9):
                c=False
                print("\n\n\n")
            else:
                print("please give valid input\n\n")
    elif(input_var==2):
        print("what is the max and min value of amp seperated by a line")
        ma=int(input())
        mi=int(input())
        print()
        print("Give the value of samples seperated with space")
        data=[float(j) for j in input().split()]
        print()
        print("Number of levels")
        level=int(input())
        delta=(ma-mi)/level
        print("delta is ",delta)
        d1=[]
        df=[]

        for i in range(len(data)):
            data[i]=data[i]/delta
            if(data[i]>0):
                data[i]=int(data[i])+0.5
            else:
                data[i]=int(data[i])-0.5
            data[i]=int(data[i])+level//2
            d1=tobinary(data[i],math.log(level,2))
            for i in d1:
                df.append(i)
        print(df)
        xs1=[]
        ys1=[]
        df.append(0)
        xs = np.repeat(range(len(df)), 2)
        ys = np.repeat(df, 2)

        #print(xs,ys)
        xs = xs[1:]
        ys = ys[:-1]
        #print(xs1,ys1)

        plt.plot(xs, ys,c='b')
        print("\n\n")
        plt.show()
    elif(input_var==9):
        b=False
        print("\n\n\n")
    else:
        print("please give valid input\n\n")

    

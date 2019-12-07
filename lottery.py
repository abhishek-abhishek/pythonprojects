import random
from tkinter import *

def Lotton_No():
    q = random.randint(1,999);
    w = random.randint(1,999);
    e = random.randint(1,999);
    r = random.randint(1,999);
    t = random.randint(1,999);
    y = random.randint(1,999);
        
    num1.set(q)
    num2.set(w)
    num3.set(e)
    num4.set(r)
    num5.set(t)
    num6.set(y)

    return


Lottery = Tk()
Lottery.geometry("800x360+0+0")
frame = Frame(Lottery)
frame.pack()

lblTitle=Label(Lottery, text="Lottery Number Generator",padx=16,pady=16,bd=16,
               fg="#000000",font=('arial',54,'bold'),
               bg="sky blue", relief="raise", width= 32, height= 1)
lblTitle.pack()



num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lottory")

frame1=Frame(Lottery)
frame1.pack(side = TOP)




frame2=Frame(Lottery)
frame2.pack(side = TOP)
txtDisplay=Entry(frame2,textvariable=num1,bd=20,insertwidth=1,font=("arial",30),justify="center",width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable=num2,bd=20,insertwidth=1,font=("arial",30),justify="center",width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable=num3,bd=20,insertwidth=1,font=("arial",30),justify="center",width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable=num4,bd=20,insertwidth=1,font=("arial",30),justify="center",width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable=num5,bd=20,insertwidth=1,font=("arial",30),justify="center",width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable=num6,bd=20,insertwidth=1,font=("arial",30),justify="center",width=4)
txtDisplay.pack(side=LEFT)

frame3=Frame(Lottery)
frame3.pack(side = TOP)
button1 = Button(frame3,state=DISABLED,text="",bg="white")
button1.pack(side=TOP)
button2 = Button(frame3,padx=0,width=18,pady=8,textvariable=var,font=("arial",26),text="Generator",bg="red",command=Lotton_No)
button2.pack(side=BOTTOM)





Lottery.mainloop()







from tkinter import *
import math

root = Tk()
root.geometry("1354x650+0+0")
root.title("Advance Calculator")
root.configure(background = "Black")

Tops = Frame(root,width = 1350,height=160 ,bd=8,relief="raise")
Tops.pack(side=TOP)

Bottom = Frame(root,width = 1350,height=500 ,bd=8,relief="raise")
Bottom.pack(side=BOTTOM)

lblTitle = Label(Tops , font = ("Helvetica",55,"bold"),text = "Advance Calculator",
                 bd=4).grid(row=0,column=0)


inBottom1 = Frame(Bottom,width = 1350,height=500 ,relief="raise")
inBottom1.pack(side=BOTTOM)

inBottom2 = Frame(Bottom,width = 650,height=500 ,bd=4,relief="raise")
inBottom2.pack(side=BOTTOM)

LF = Frame(inBottom2,width = 1350,height=800 ,bd=0,relief="raise")
LF.pack(side=LEFT)

RT = Frame(inBottom2,width = 1350,height=800 ,bd=0,relief="raise")
RT.pack(side=LEFT)

Buttons = Frame(inBottom1,width = 1350,height=300 ,bd=4,relief="raise")
Buttons.pack(side=BOTTOM)

AnsBottom2 = Frame(inBottom1,width = 1350,height=500 ,bd=4,relief="raise")
AnsBottom2.pack(side=BOTTOM)

def Sum():
        if var.get()==1:
            Qty1 = float(firstnum.get())
            Qty2 = float(secondnum.get())
            SumUp = Qty1 + Qty2
            Total.set(SumUp)
            
        elif var.get()==2:
            Qty1 = float(firstnum.get())
            Qty2 = float(secondnum.get())
            SumUp = Qty1 - Qty2
            Total.set(SumUp)

        elif var.get()==3:
            Qty1 = float(firstnum.get())
            Qty2 = float(secondnum.get())
            SumUp = Qty1 * Qty2
            Total.set(SumUp)

        elif var.get()==4:
                Qty1 = float(firstnum.get())
                Qty2 = float(secondnum.get())
                SumUp = Qty1 / Qty2
                Total.set(SumUp)

        elif var.get()==5:
                Qty1 = float(firstnum.get())
                Qty2 = float(secondnum.get())
                SumUp = Qty1 % Qty2
                Total.set(SumUp)

        elif var.get()==6:
                Qty1 = float(firstnum.get())
                Qty2 = float(secondnum.get())
                SumUp = (Qty1*Qty1 + 2*Qty1*Qty2 + Qty2*Qty2)
                Total.set(SumUp)

        elif var.get()==7:
                Qty1 = float(firstnum.get())
                Qty2 = float(secondnum.get())
                SumUp = (Qty1*Qty1*Qty1 + 3*Qty1*Qty1*Qty2 + 3*Qty1*Qty2*Qty2 + Qty2*Qty2*Qty2)
                Total.set(SumUp)

        elif var.get()==8:
                Qty1 = float(firstnum.get())
                Total.set(math.sqrt(Qty1))

        elif var.get()==9:
                Qty1 = float(firstnum.get())
                Qty2 = float(secondnum.get())
                Total.set(math.pow(Qty1,Qty2))

        elif var.get()==10:
                Qty1 = float(firstnum.get())
                Total.set(math.sin(Qty1))

        elif var.get()==11:
                Qty1 = float(firstnum.get())
                Total.set(math.cos(Qty1))

        elif var.get()==12:
                Qty1 = float(firstnum.get())
                Total.set(math.tan(Qty1))

        elif var.get()==13:
                Total.set(math.pi)

        elif var.get()==14:
                Qty1 = float(firstnum.get())
                Total.set(math.exp(Qty1))


def Reset():
    firstnum.set("")
    secondnum.set("")
    Total.set("")
    
    
var = IntVar()
firstnum = IntVar()
secondnum = IntVar()
Total = IntVar()

firstnum.set("")
secondnum.set("")
Total.set("")

#--------------------------------------basic---------------------------------------------

Addition = Radiobutton(LF,text="Addition",variable = var, value=1,
                       font = ("Helvetica",17,"bold")).grid(row=0,sticky=W)

Substraction = Radiobutton(LF,text="Substraction",variable = var, value=2,
                       font = ("Helvetica",17,"bold")).grid(row=1,sticky=W)

Multiply = Radiobutton(LF,text="Multiply",variable = var, value=3,
                       font = ("Helvetica",17,"bold")).grid(row=2,sticky=W)

Division = Radiobutton(LF,text="Division",variable = var, value=4,
                       font = ("Helvetica",17,"bold")).grid(row=3,sticky=W)

Modulus = Radiobutton(LF,text="Modulus ",variable = var, value=5,
                       font = ("Helvetica",17,"bold")).grid(row=4,sticky=W)

Square = Radiobutton(LF,text="(a+b)^2",variable = var, value=6,
                       font = ("Helvetica",17,"bold")).grid(row=5,sticky=W)

Cube = Radiobutton(LF,text="(a+b)^3",variable = var, value=7,
                       font = ("Helvetica",17,"bold")).grid(row=6,sticky=W)

#------------------------------------------advance---------------------------------------

Sqrt = Radiobutton(RT,text="Square root",variable = var, value=8,
                       font = ("Helvetica",17,"bold")).grid(row=0,sticky=W)

pow = Radiobutton(RT,text="Power of a number",variable = var, value=9,
                       font = ("Helvetica",17,"bold")).grid(row=1,sticky=W)

sin = Radiobutton(RT,text="Sine",variable = var, value=10,
                       font = ("Helvetica",17,"bold")).grid(row=2,sticky=W)

cos = Radiobutton(RT,text="Cosine",variable = var, value=11,
                       font = ("Helvetica",17,"bold")).grid(row=3,sticky=W)

tan = Radiobutton(RT,text="Tan",variable = var, value=12,
                       font = ("Helvetica",17,"bold")).grid(row=4,sticky=W)

pi = Radiobutton(RT,text="PI Value",variable = var, value=13,
                       font = ("Helvetica",17,"bold")).grid(row=5,sticky=W)

exp = Radiobutton(RT,text="Exponent",variable = var, value=14,
                       font = ("Helvetica",17,"bold")).grid(row=6,sticky=W)


#---------------------------------------------------------------------------------------------


lblfirst = Label(AnsBottom2,font = ("Helvetica",20,"bold"),text="Enter First number",
                 fg="black",bd=4).grid(row=0,column=0,sticky=W)

txtfirst = Entry(AnsBottom2,font = ("Helvetica",20,"bold"),bd=4,width=34,bg="white",
                 textvariable=firstnum).grid(row=0,column=1)

lblsecond = Label(AnsBottom2,font = ("Helvetica",20,"bold"),text="Enter Second number",
                 fg="black",bd=4).grid(row=1,column=0,sticky=W)

txtsecond = Entry(AnsBottom2,font = ("Helvetica",20,"bold"),bd=4,width=34,bg="white",
                 textvariable=secondnum).grid(row=1,column=1)

lblTotal = Label(AnsBottom2,font=("Helvetica",20,"bold"),text="Answer is",fg="black",
                 bd=4,justify="left")
lblTotal.grid(row=2,column=0,sticky=W)

Answer = Label(AnsBottom2,font = ("Helvetica",20,"bold"),bd=4,width=30,bg="white",
               textvariable=Total,relief="sunken").grid(row=2,column=1,sticky=W)

SumUp=Button(Buttons,pady=8,bd=4,fg="black",font = ("Helvetica",26,"bold"),width=13,command = Sum,
             text="Result").grid(row=0,column=0)

Reset=Button(Buttons,pady=8,bd=4,fg="black",font = ("Helvetica",26,"bold"),width=13,command = Reset,
             text="Reset").grid(row=0,column=1)





root.mainloop()

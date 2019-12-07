from tkinter import *
import math

root = Tk()
root.geometry("1354x650+0+0")
root.title("Length Convertor")
root.configure(background = "Red")

Tops = Frame(root,width = 1350,height=160 ,bd=8,relief="raise")
Tops.pack(side=TOP)

Bottom = Frame(root,width = 1350,height=500 ,bd=8,relief="raise")
Bottom.pack(side=BOTTOM)

lblTitle = Label(Tops , font = ("Helvetica",55,"bold"),text = "Length Convertor",
                 bd=4).grid(row=0,column=0)
lblTitle = Label(Tops , font = ("Helvetica",20,"bold"),text = "Convert anything to centimeter",
                 bd=4).grid(row=1,column=0)


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
            Convert = Qty1*0.1
            Total.set(Convert)
            
        elif var.get()==2:
            Qty1 = float(firstnum.get())
            Convert = Qty1*100
            Total.set(Convert)

        elif var.get()==3:
            Qty1 = float(firstnum.get())
            Convert = Qty1*100000
            Total.set(Convert)

        elif var.get()==4:
                Qty1 = float(firstnum.get())
                Convert = Qty1*2.54
                Total.set(Convert)

        elif var.get()==5:
                Qty1 = float(firstnum.get())
                Convert = Qty1*30.48
                Total.set(Convert)

        elif var.get()==6:
                Qty1 = float(firstnum.get())
                Convert = Qty1*91.44
                Total.set(Convert)

        elif var.get()==7:
                Qty1 = float(firstnum.get())
                Convert = Qty1*160934
                Total.set(Convert)

        elif var.get()==8:
                Qty1 = float(firstnum.get())
                Convert = Qty1*185200
                Total.set(Convert)

                


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

Millimeter = Radiobutton(LF,text="Millimeter",variable = var, value=1,
                       font = ("Helvetica",17,"bold")).grid(row=0,sticky=W)

Meter = Radiobutton(RT,text="Meter",variable = var, value=2,
                       font = ("Helvetica",17,"bold")).grid(row=1,sticky=W)

Kilometer = Radiobutton(LF,text="Kilometer",variable = var, value=3,
                       font = ("Helvetica",17,"bold")).grid(row=2,sticky=W)

inch = Radiobutton(RT,text="Inch",variable = var, value=4,
                       font = ("Helvetica",17,"bold")).grid(row=3,sticky=W)

foot = Radiobutton(LF,text="Foot/Feet",variable = var, value=5,
                       font = ("Helvetica",17,"bold")).grid(row=4,sticky=W)

yard = Radiobutton(RT,text="Yard",variable = var, value=6,
                       font = ("Helvetica",17,"bold")).grid(row=5,sticky=W)

mile = Radiobutton(LF,text="Mile",variable = var, value=7,
                       font = ("Helvetica",17,"bold")).grid(row=6,sticky=W)


mile2 = Radiobutton(RT,text="Nautical Miles",variable = var, value=8,
                       font = ("Helvetica",17,"bold")).grid(row=0,sticky=W)



#---------------------------------------------------------------------------------------------


lblfirst = Label(AnsBottom2,font = ("Helvetica",20,"bold"),text="Enter the number to convert",
                 fg="black",bd=4).grid(row=0,column=0,sticky=W)

txtfirst = Entry(AnsBottom2,font = ("Helvetica",20,"bold"),bd=4,width=34,bg="white",
                 textvariable=firstnum).grid(row=0,column=1)

lblTotal = Label(AnsBottom2,font=("Helvetica",20,"bold"),text="Answer in cm",fg="black",
                 bd=4,justify="left")
lblTotal.grid(row=2,column=0,sticky=W)

Answer = Label(AnsBottom2,font = ("Helvetica",20,"bold"),bd=4,width=30,bg="white",
               textvariable=Total,relief="sunken").grid(row=2,column=1,sticky=W)

Convert=Button(Buttons,pady=8,bd=4,fg="black",font = ("Helvetica",26,"bold"),width=13,command = Sum,
             text="Result").grid(row=0,column=0)

Reset=Button(Buttons,pady=8,bd=4,fg="black",font = ("Helvetica",26,"bold"),width=13,command = Reset,
             text="Reset").grid(row=0,column=1)





root.mainloop()

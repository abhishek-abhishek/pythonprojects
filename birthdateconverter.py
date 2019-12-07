from tkinter import *
from datetime import datetime
import tkinter.messagebox

class CalDate:

    def __init__(self,root):
        self.root = root
        self.root.title("Date Calculator")
        self.root.geometry("1350x550+0+0")
        self.root.configure(background="powder blue")

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopMain1 = Frame(MainFrame,bd=14,width=1350,height=550,pady=10,padx=10,relief=RIDGE,bg="cadet blue")
        TopMain1.grid(row=4,column=2)

        TopMain2 = Frame(TopMain1,bd=14,width=1300,height=450,pady=10,padx=10,relief=RIDGE,bg="cadet blue")
        TopMain2.grid(row=4,column=2)
        
        TopMain3 = Frame(TopMain2,bd=14,width=1500,height=400,pady=10,padx=10,relief=RIDGE,bg="cadet blue")
        TopMain3.grid(row=4,column=2)
        
        TopMain4 = Frame(TopMain3,bd=14,width=1200,height=350,pady=10,padx=10,relief=RIDGE,bg="cadet blue")
        TopMain4.grid(row=4,column=2)
        
        TopFrame = Frame(TopMain4,bd=14,width=1000,height=300,pady=10,padx=10,relief=RIDGE,bg="cadet blue")
        TopFrame.grid(row=4,column=2)


        def iExit():
            iExit = tkinter.messagebox.askyesno("Date Calculator","Confirm if you want to Exit")
            if iExit > 0:
                root.destroy()
                return

        def iReset():
            CheckInDate.set("")
            CheckOutDate.set("")
            TotalDays.set("")




        def iDate():

            d1=CheckInDate.get()
            d2=CheckOutDate.get()

            d1= datetime.strptime(d1, "%d/%m/%Y")
            d2= datetime.strptime(d2, "%d/%m/%Y")

            TotalDays.set(abs(d2-d1).days)

            

            
        




        

        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        TotalDays=StringVar()

        #-------------------------------------------------------------------------------

        self.lblTitle = Label(TopFrame,font=('arial',40,'bold'),text="date calculator",padx=2,pady=2,
                              bg="cadetBlue",fg="white")
        self.lblTitle.grid(row=0,column=0,columnspan=4)


        self.lblCheck_In_Date = Label(TopFrame,font=('arial',24,'bold'),text="check in date:",padx=2,pady=2,
                              bg="cadetBlue",fg="white")
        self.lblCheck_In_Date.grid(row=1,column=0,sticky=W)
        self.txtCheck_In_Date = Entry(TopFrame,font=('arial',24,'bold'),textvariable = CheckInDate,
                                      bd=7,width=41)
        self.txtCheck_In_Date.grid(row=1,column=1,padx=4,pady=21,columnspan=3)



        self.lblCheck_Out_Date = Label(TopFrame,font=('arial',24,'bold'),text="check out date:",padx=2,pady=2,
                              bg="cadetBlue",fg="white")
        self.lblCheck_Out_Date.grid(row=2,column=0,sticky=W)
        self.txtCheck_Out_Date = Entry(TopFrame,font=('arial',24,'bold'),textvariable = CheckOutDate,
                                      bd=7,width=41)
        self.txtCheck_Out_Date.grid(row=2,column=1,padx=4,pady=21,columnspan=3)
        


        self.lblTotalCost = Label(TopFrame,font=('arial',24,'bold'),text="calculated date",bd=7,
                              bg="cadetBlue",fg="white")
        self.lblTotalCost.grid(row=3,column=0,sticky=W)
        self.txtTotalCost = Entry(TopFrame,font=('arial',24,'bold'),textvariable = TotalDays,
                                      bd=7,width=41)
        self.txtTotalCost.grid(row=3,column=1,padx=9,pady=21,columnspan=3)

        #------------------------------------------------------------------------------------------

        self.btnTotal=Button(TopFrame,padx=16,pady=9,bd=4,fg='black',font=('arial',24,'bold'),
                             width=10,height=1,bg='powder blue',text="Total",command=iDate).grid(row=5,column=1,padx=4)


        self.btnReset=Button(TopFrame,padx=16,pady=9,bd=4,fg='black',font=('arial',24,'bold'),
                             width=10,height=1,bg='powder blue',text="Reset",command=iReset).grid(row=5,column=2,padx=4)


        self.btnExit=Button(TopFrame,padx=16,pady=9,bd=4,fg='black',font=('arial',24,'bold'),
                             width=10,height=1,bg='powder blue',text="Exit",command=iExit).grid(row=5,column=3,padx=4)

        


        


        

        




if __name__=='__main__':
    root = Tk()
    application = CalDate (root)
    root.mainloop()

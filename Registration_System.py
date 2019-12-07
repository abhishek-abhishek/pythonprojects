from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Registration:

    def __init__(self,root):
        self.root = root
        self.root.title("Club Member Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%y"))


        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()

        
                        
        Membership=StringVar()
        Membership.set("0")

        #----------------------------Function------------------------

        def iExit():
            iExit = tkinter.messagebox.askyesno("Club Member Registration System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")


            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")

            self.choProve_of_ID.current(0)
            self.choFee.current(0)
            self.choMember.current(0)
            self.choMode.current(0)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Club Member Registration System","Confirm if you want to add a new\
record")
            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                 Reset()
                 self.txtReceipt.delete("1.0",END)
                 return

        def Ref_No():
            x=random.randint(10903,600873)
            randomRef=str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"\t"+Ref.get()+"\t"+Firstname.get()+"\t"+Surname.get()+"\t"+Address.get()+"\t"+DateofOrder.get()
                                   +"\t"+Telephone.get()+"\n")
            
        #--------------------------Frame------------------------------
        Mainframe=Frame(self.root)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe,bd=20,width=1350,padx=26,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=("arial",59,"bold"), text="Club Member Registration ",
                            padx=2)
        self.lblTitle.grid()

        #---------------------------------LowerFrame--------------------------

        MemberDetailsFrame=LabelFrame(Mainframe,bd=20,width=880,height=400,relief=RIDGE,
                                 pady=5)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails=LabelFrame(MemberDetailsFrame,bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails,bd=10,width=350,height=400,
                                   font=("arial",12,"bold"),text="Customer Name",relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame= LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        
        #-----------------------------------------------------------------------------

        self.lblReferenceNo=Label(MembersName_F,font=("arial",14,"bold"), text="Reference No",
                                  bd=7)
        self.lblReferenceNo.grid(row=0,column=0)
        self.txtReferenceNo=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=Ref,
                                  state = DISABLED,insertwidth=2)
        self.txtReferenceNo.grid(row=0,column=1)
        

        self.lblfirstname=Label(MembersName_F,font=("arial",14,"bold"), text="First Name",
                                  bd=7)
        self.lblfirstname.grid(row=1,column=0,sticky=W)
        self.txtfirstname=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=Firstname,
                                insertwidth=2)
        self.txtfirstname.grid(row=1,column=1)


        self.lblsurnamename=Label(MembersName_F,font=("arial",14,"bold"), text="Surname",
                                  bd=7)
        self.lblsurnamename.grid(row=2,column=0,sticky=W)
        self.txtsurnamename=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=Surname,
                                insertwidth=2)
        self.txtsurnamename.grid(row=2,column=1)
        

        self.lblAddress=Label(MembersName_F,font=("arial",14,"bold"), text="Address",
                                  bd=7)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=Address,
                                insertwidth=2)
        self.txtAddress.grid(row=3,column=1)


        self.lblPostCode=Label(MembersName_F,font=("arial",14,"bold"), text="Pin Code",
                                  bd=7)
        self.lblPostCode.grid(row=4,column=0,sticky=W)
        self.txtPostCode=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=PostCode,
                                insertwidth=2)
        self.txtPostCode.grid(row=4,column=1)


        self.lblTelephone=Label(MembersName_F,font=("arial",14,"bold"), text="Phone Number",
                                  bd=7)
        self.lblTelephone.grid(row=5,column=0,sticky=W)
        self.txtTelephone=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=Telephone,
                                insertwidth=2)
        self.txtTelephone.grid(row=5,column=1)


        self.lblDate=Label(MembersName_F,font=("arial",14,"bold"), text="Date",
                                  bd=7)
        self.lblDate.grid(row=6,column=0,sticky=W)
        self.txtDate=Entry(MembersName_F,font=("arial",14,"bold"),bd=7,textvariable=DateofOrder,state = DISABLED,
                                insertwidth=2)
        self.txtDate.grid(row=6,column=1)


        #----------------------------------------------------------------------------------------

        self.lblProve_of_ID = Label(MembersName_F,font=("arial",14,"bold"),text="ID Prove",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0,sticky=W)

        self.choProve_of_ID=ttk.Combobox(MembersName_F,textvariable=var1,state="readonly",
                                         font=("arial",14,"bold"),width=19)
        self.choProve_of_ID["value"]=("","Driving Licence","Passport","Student ID")
        self.choProve_of_ID.current(0)
        self.choProve_of_ID.grid(row=7,column=1)

        self.lblFee = Label(MembersName_F,font=("arial",14,"bold"),text="Fee Structure",bd=7)
        self.lblFee.grid(row=8,column=0,sticky=W)

        self.choFee=ttk.Combobox(MembersName_F,textvariable=var2,state="readonly",
                                         font=("arial",14,"bold"),width=19)
        self.choFee["value"]=("","Rs 1000","Rs 1500","Rs 2000","Rs 3000")
        self.choFee.current(0)
        self.choFee.grid(row=8,column=1)

        self.lblMember = Label(MembersName_F,font=("arial",14,"bold"),text="Type of Member",bd=7)
        self.lblMember.grid(row=9,column=0,sticky=W)

        self.choMember=ttk.Combobox(MembersName_F,textvariable=var3,state="readonly",
                                         font=("arial",14,"bold"),width=19)
        self.choMember["value"]=("","Gold","Premium","Elite","Platinum")
        self.choMember.current(0)
        self.choMember.grid(row=9,column=1)

        self.lblMode = Label(MembersName_F,font=("arial",14,"bold"),text="Type of Payment",bd=7)
        self.lblMode.grid(row=10,column=0,sticky=W)

        self.choMode=ttk.Combobox(MembersName_F,textvariable=var4,state="readonly",
                                         font=("arial",14,"bold"),width=19)
        self.choMode["value"]=("","Cash","Debit Card","Credit Card","Netbanking")
        self.choMode.current(0)
        self.choMode.grid(row=10,column=1)

        #-------------------------------------------------------------------------------------------------


        self.txtReceipt = Text(Receipt_ButtonFrame,font=("arial",10,"bold"),width=112,height=22)
        self.txtReceipt.grid(row=1,column=0,columnspan=4)

        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18,bd=7,font=("arial",16,"bold"),
                               width=13,text="Receipt",command=Receipt).grid(row=2,column=0)
        self.btnReset=Button(Receipt_ButtonFrame,padx=18,bd=7,font=("arial",16,"bold"),
                               width=13,text="Reset",command=iResetRecord).grid(row=2,column=1)
        self.btnExit=Button(Receipt_ButtonFrame,padx=18,bd=7,font=("arial",16,"bold"),
                               width=13,text="Exit",command=iExit).grid(row=2,column=2)

        
        
        

if __name__=="__main__":
   root = Tk()
   application = Registration (root)
   root.mainloop()

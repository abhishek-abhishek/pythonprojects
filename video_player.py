import os

from tkinter import *

app = Tk()
app.title('Audio Player')

lblTitle=Label(app, text="Food Video",padx=16,pady=16,bd=16,
               fg="#000000",font=('arial',54,'bold'),
               bg="sky blue", relief="raise", width= 32, height= 1)
lblTitle.pack()

#---------------------------------Starter------------------------------------

def snd1():
    os.system("Strawberry_Ice_Cream_Rolls.mp4")

def snd2():
    os.system("Vanilla_&_Brownie_Ice_cream_Rolls.mp4")

def snd3():
    os.system("veg_momos_recipe.mp4")

def snd4():
    os.system("Blueberry_Ice_Cream_Rolls.mp4")

def snd5():
    os.system("custard_recipe.mp4")
    
def snd6():
    os.system("Roomali_Roti.mp4")

#-----------------------------------------------NonVeg----------------------------------------------------------

def snd7():
    os.system("Laal_Maas.mp4")

def snd8():
    os.system("\Roast_Chicken.mp4")

def snd9():
    os.system("Chicken_Lollipop.mp4")

def snd10():
    os.system("Chicken_Roll.mp4")

def snd11():
    os.system("Chicken_Tikka_Masala.mp4")

def snd12():
    os.system("Hyderabadi_Chicken_Dum.mp4")

#------------------------------------------Veg--------------------------------------------------------------

def snd13():
    os.system("mix_veg_recipe.mp4")

def snd14():
    os.system("Palak_Paneer.mp4")

def snd15():
    os.system("stuffed_capsicum.mp4")

def snd16():
    os.system("Veg_Dum_Biryani.mp4")

def snd17():
    os.system("veg_kurma.mp4")

def snd18():
    os.system("aloo_matar_recipe.mp4")



var = IntVar()



Bottom1 = Frame(app,width = 1350,height=500 ,bd=8,relief="raise")
Bottom1.pack(side=TOP)

LF = Frame(Bottom1,width = 1350,height=800 ,bd=0,relief="raise")
LF.pack(side=LEFT)

RT = Frame(Bottom1,width = 1350,height=800 ,bd=0,relief="raise")
RT.pack(side=RIGHT)

#----------------------------------------------------------------------------------------

Bottom2 = Frame(app,width = 1350,height=500 ,bd=8,relief="raise")
Bottom2.pack(side=BOTTOM)


MD = Frame(Bottom2,width = 1350,height=800 ,bd=0,relief="raise")
MD.pack(side=LEFT)


#---------------------------------------------------------------------------------------------------------------------
                                

rb1 = Radiobutton(LF,text="Strawberry Ice Cream Rolls",variable = var,value=1,font = ("Helvetica",17,"bold"),command=snd1).grid(row=0,sticky=W)

rb2 = Radiobutton(LF,text="Vanilla & Brownie Ice cream Rolls",variable = var,value=2,font = ("Helvetica",17,"bold"),command=snd2).grid(row=1,sticky=W)

rb3 = Radiobutton(LF,text="veg momos recipe",variable = var,value=3,font = ("Helvetica",17,"bold"),command=snd3).grid(row=2,sticky=W)

rb4 = Radiobutton(LF,text="Blueberry Ice Cream Rolls",variable = var,value=4,font = ("Helvetica",17,"bold"),command=snd4).grid(row=3,sticky=W)

rb5 = Radiobutton(LF,text="custard recipe",variable = var,value=5,font = ("Helvetica",17,"bold"),command=snd5).grid(row=4,sticky=W)

rb6 = Radiobutton(LF,text="Roomali Roti",variable = var,value=6,font = ("Helvetica",17,"bold"),command=snd6).grid(row=5,sticky=W)

#--------------------------------------------------------------------------------------------------------------------------

rb7 = Radiobutton(RT,text="Amritsari Chicken Masala",variable = var,value=7,font = ("Helvetica",17,"bold"),command=snd7).grid(row=6,sticky=W)

rb8 = Radiobutton(RT,text="Roast Chicken",variable = var,value=8,font = ("Helvetica",17,"bold"),command=snd8).grid(row=7,sticky=W)

rb9 = Radiobutton(RT,text="Chicken Lollipop",variable = var,value=9,font = ("Helvetica",17,"bold"),command=snd9).grid(row=8,sticky=W)

rb10 = Radiobutton(RT,text="Chicken Roll",variable = var,value=10,font = ("Helvetica",17,"bold"),command=snd10).grid(row=9,sticky=W)

rb11 = Radiobutton(RT,text="Chicken Tikka Masala",variable = var,value=11,font = ("Helvetica",17,"bold"),command=snd11).grid(row=10,sticky=W)

rb12 = Radiobutton(RT,text="Hyderabadi Chicken Dum",variable = var,value=12,font = ("Helvetica",17,"bold"),command=snd12).grid(row=11,sticky=W)

#------------------------------------------------------------------------------------------------------------------------------

rb13 = Radiobutton(MD,text="mix veg recipe",variable = var,value=13,font = ("Helvetica",17,"bold"),command=snd13).grid(row=12,sticky=W)

rb14 = Radiobutton(MD,text="Palak Paneer",variable = var,value=14,font = ("Helvetica",17,"bold"),command=snd14).grid(row=13,sticky=W)

rb15 = Radiobutton(MD,text="stuffed capsicum",variable = var,value=15,font = ("Helvetica",17,"bold"),command=snd15).grid(row=14,sticky=W)

rb16 = Radiobutton(MD,text="Veg Dum Biryani",variable = var,value=16,font = ("Helvetica",17,"bold"),command=snd16).grid(row=15,sticky=W)

rb17 = Radiobutton(MD,text="veg kurma",variable = var,value=17,font = ("Helvetica",17,"bold"),command=snd17).grid(row=16,sticky=W)

rb18 = Radiobutton(MD,text="aloo matar recipe",variable = var,value=18,font = ("Helvetica",17,"bold"),command=snd18).grid(row=17,sticky=W)



app.mainloop()

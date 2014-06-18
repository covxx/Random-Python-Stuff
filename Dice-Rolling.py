from Tkinter import *
import random
root=Tk()
root.geometry('520x300') 
root.title('Dice Roll')
root["bg"] = "white"
##==================Progress==================##
#Everything works besides changing the pictues
#Error given is that lambda is not given any args
# But args are given
##============================================##
def roll_d():
    tmp=(randrange(0,5))
    if x == 1:
        button_1.config(image=image_all[tmp])
    elif x == 2:
         button_2.config(image=image_all[tmp])
    elif x == 3:
         button_3.config(image=image_all[tmp])
    elif x == 4:
         button_4.config(image=image_all[tmp])
    elif x == 5:
         button_5.config(image=image_all[tmp])
##===================Logic=====================##
def roll_x():
    button_1.config(image=image_all[tmp])
    tmp=(randrange(0,6))
    button_2.config(image=image_all[tmp])
    tmp=(randrange(0,6))
    button_3.config(image=image_all[tmp])
    tmp=(randrange(0,6))
    button_4.config(image=image_all[tmp])
    tmp=(randrange(0,6))
    button_5.config(image=image_all[tmp])
    tmp=(randrange(0,6))
    button_6.config(image=image_all[tmp])
    tmp=(randrange(0,6))
##===================Load=Images==============##
image_1 = PhotoImage(file="images/1.gif")
image_2 = PhotoImage(file="images/2.gif")
image_3 = PhotoImage(file="images/3.gif")
image_4 = PhotoImage(file="images/4.gif")
image_5 = PhotoImage(file="images/5.gif")
image_6 = PhotoImage(file="images/6.gif")
image_all=[image_1,image_2,image_3,image_4,image_5,image_6]
####====================Frame=================##
frame = Frame(root,background='white')
frame.place(x=10,y=75)
frame.pack()
##============Images=On=Screen==============##
button_1 = Button(frame,image=image_1,bd=0,command=lambda x: roll_d("1"))
button_1.grid(row=1,column=1,padx=2,pady=2)
##
button_2 = Button(frame,image=image_2,bd=0,command=lambda x: roll_d("2"))
button_2.grid(row=1,column=2,padx=2,pady=2)
##
button_3 = Button(frame,image=image_3,bd=0,command=lambda x: roll_d("3"))
button_3.grid(row=1,column=3,padx=2,pady=2)
##
button_4 = Button(frame,image=image_4,bd=0,command=lambda x: roll_d("4"))
button_4.grid(row=1,column=4,padx=2,pady=2)
##
button_5 = Button(frame,image=image_5,bd=0,command=lambda x: roll_d("5"))
button_5.grid(row=1,column=5,padx=2,pady=2)
##
button_6 = Button(frame,text="Roll The Dice",command=lambda x: roll_d('0,5'))
button_6.grid(row=2,column=3,padx=2,pady=2)
##============================================##
root.mainloop()


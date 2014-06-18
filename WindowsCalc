#This doesn't actually do anything, its just a gui that looks like the windows one(kinda)
from Tkinter import * 
mGui=Tk()
mGui.geometry('213x240') 
mGui.title('Calculator')
mGui["bg"]="#D9E3F6"

##set images
image1 = PhotoImage(file="images/mc.gif")
image2 = PhotoImage(file="images/mr.gif")
image3 = PhotoImage(file="images/ms.gif")
image4 = PhotoImage(file="images/m+.gif")
image5 = PhotoImage(file="images/m-.gif")
##row1
image6 = PhotoImage(file="images/arrow.gif")
image7 = PhotoImage(file="images/ce.gif")
image8 = PhotoImage(file="images/c.gif")
image9 = PhotoImage(file="images/+-.gif")
image10 = PhotoImage(file="images/check.gif")
##row2
image11 = PhotoImage(file="images/7.gif")
image12 = PhotoImage(file="images/8.gif")
image13 = PhotoImage(file="images/9.gif")
image14 = PhotoImage(file="images/div.gif")
image15 = PhotoImage(file="images/percent.gif")
##row3
image16 = PhotoImage(file="images/4.gif")
image17 = PhotoImage(file="images/5.gif")
image18 = PhotoImage(file="images/9.gif")
image19 = PhotoImage(file="images/mult.gif")
image20 = PhotoImage(file="images/ricp.gif")
##row4
image21 = PhotoImage(file="images/1.gif")
image22 = PhotoImage(file="images/2.gif")
image23 = PhotoImage(file="images/3.gif")
image24 = PhotoImage(file="images/-.gif")
##row5
image26 = PhotoImage(file="images/0.gif")
image27 = PhotoImage(file="images/decpt.gif")
image28 = PhotoImage(file="images/plus.gif")
image29 = PhotoImage(file="images/=.gif")
image30 = PhotoImage(file="images/mc.gif")
##gui
##row
c = Label(mGui,text="maybe",width=20,height=3,bg="#FFFFFF")
c.grid(row=1,column=1,columnspan=5)
mbutton1 = Button(image=image1,bd=0).grid(row=5,column=1,padx=2,pady=2)
mbutton2 = Button(image=image2,bd=0).grid(row=5,column=2,padx=2,pady=2)
mbutton3 = Button(image=image3,bd=0).grid(row=5,column=3,padx=2,pady=2)
mbutton3 = Button(image=image4,bd=0).grid(row=5,column=4,padx=2,pady=2)
mbutton3 = Button(image=image5,bd=0).grid(row=5,column=5,padx=2,pady=2)
##row 2
mbutton4 = Button(image=image6,bd=0).grid(row=6,column=1,padx=2,pady=2)
mbutton5 = Button(image=image7,bd=0).grid(row=6,column=2,padx=2,pady=2)
mbutton6 = Button(image=image8,bd=0).grid(row=6,column=3,padx=2,pady=2)
mbutton7 = Button(image=image9,bd=0).grid(row=6,column=4,padx=2,pady=2)
mbutton8 = Button(image=image10,bd=0).grid(row=6,column=5,padx=2,pady=2)
##row 3
mbutton9 = Button(image=image11,bd=0).grid(row=7,column=1,padx=2,pady=2)
mbutton10 = Button(image=image12,bd=0).grid(row=7,column=2,padx=2,pady=2)
mbutton11 = Button(image=image13,bd=0).grid(row=7,column=3,padx=2,pady=2)
mbutton12 = Button(image=image14,bd=0).grid(row=7,column=4,padx=2,pady=2)
mbutton13 = Button(image=image15,bd=0).grid(row=7,column=5,padx=2,pady=2)
###row4
mbutton14 = Button(image=image16,bd=0).grid(row=8,column=1,padx=2,pady=2)
mbutton15 = Button(image=image17,bd=0).grid(row=8,column=2,padx=2,pady=2)
mbutton16 = Button(image=image18,bd=0).grid(row=8,column=3,padx=2,pady=2)
mbutton17 = Button(image=image19,bd=0).grid(row=8,column=4,padx=2,pady=2)
mbutton18 = Button(image=image20,bd=0).grid(row=8,column=5,padx=2,pady=2)
####row 5
mbutton19 = Button(image=image21,bd=0).grid(row=9,column=1,padx=2,pady=2)
mbutton20 = Button(image=image22,bd=0).grid(row=9,column=2,padx=2,pady=2)
mbutton21 = Button(image=image23,bd=0).grid(row=9,column=3,padx=2,pady=2)
mbutton23 = Button(image=image24,bd=0).grid(row=9,column=4,padx=2,pady=2)
mbutton28 = Button(image=image29,bd=0).grid(row=9,column=5,rowspan=2,padx=2,pady=2)
####row 6
mbutton25 = Button(image=image26,bd=0).grid(row=10,column=1,columnspan=2,padx=2,pady=2)
mbutton26 = Button(image=image27,bd=0).grid(row=10,column=3,padx=2,pady=2)
mbutton27 = Button(image=image28,bd=0).grid(row=10,column=4,padx=2,pady=2)

##menu
menubar=Menu(mGui)
filemenu= Menu(menubar)
editmenu= Menu(menubar)
helpmenu= Menu(menubar)
##
filemenu = Menu(menubar)
filemenu.add_command(label="Standard")
filemenu.add_command(label="Basic")
filemenu.add_command(label="History")
menubar.add_cascade(label="View",menu=filemenu)
##
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
menubar.add_cascade(label="Edit",menu=editmenu)
##
helpmenu.add_command(label="View Help")
helpmenu.add_command(label="About Calculator")
menubar.add_cascade(label="Help",menu=helpmenu)




mGui.config(menu=menubar)
mGui.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
win = tk.Tk()
win.title("python Gui")
win.resizable(True,False)
#Adding a label that will get modified
a_label=ttk.Label(win, text ="A Label")
a_label.grid(column =0,row=0)

#Button click Event function
def click_me():
    action.configure(text=' Hello '+name.get()+  number_chosen.get())
#Change our label
ttk.Label(win, text="Enter a name").grid(column=0,row=0)
#Adding a button
action= ttk.Button(win, text="Click me", command=click_me)
action.grid(column=2,row=1)
#Adding A text box Entry Widget
name=tk.StringVar()
name_entered=ttk.Entry(win, width=12,textvariable=name)
name_entered.grid(column=0,row=1)
action.configure(state='enabled')
ttk.Label(win, text="Choose a number:").grid(column=1,row=0)
number=tk.StringVar()
number_chosen=ttk.Combobox(win, width=12,textvariable=number,state='readonly')
number_chosen['value']= (1 ,2 ,3 ,4)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)
#Create trhree buttons
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win,text="Disabled",variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win,text="Unchecked",variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

#Radio Button golbal
COLOR1="Blue"
COLOR2="Gold"
COLOR3="Red"

#Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if radSel ==1:win.configure(background=COLOR1)
    elif radSel ==2:win.configure(background=COLOR2)
    elif radSel ==3:win.configure(background=COLOR3)
#create three radiobuttons using one variable
radVar=tk.IntVar()
rad1=tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)

rad2=tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)

rad3=tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)

# USing a srcolled Text control
scrol_w =30
scrol_h =3
scr=scrolledtext.ScrolledText(win,width=scrol_w,height=scrol_h,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

#Create a container to hold labels
button_frame =  ttk.LabelFrame(win,text='Label is a frame')
button_frame.grid(column=0,row=7)
#button_frame.grid(column=1,row=7)

#place labels into the container element
ttk.Label(button_frame,text="Label1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(button_frame,text="Label2").grid(column=1,row=0,sticky=tk.W)
ttk.Label(button_frame,text="Label3").grid(column=2,row=0,sticky=tk.W)

name_entered.focus()  #Place cursor into name Entry
############Start GUI################
win.mainloop()
#ATM-Account.py
from tkinter import *
from tkinter import ttk



global myAcc
myAcc = int(input('Please Enter your myAcc:'))

def calc():
	witdraw = int(wd.get())
	global myAcc
	myAcc = myAcc-witdraw
	ac.set(f'Account is : {myAcc:,d}')
	result.set(f'ถอนแล้วจำนวน {witdraw:,d} คงเหลือ {myAcc:,d}')

GUI = Tk()
GUI.geometry('500x500')
GUI.title('KS-CodeBank')

FONT = ('Angsana New',20)

ac = StringVar()
ac.set(f'Account is : {myAcc}')
wd = StringVar()
result = StringVar()

L1 = ttk.Label(GUI,textvariable=ac,font=FONT)
L1.pack(pady=50)

E1 = ttk.Entry(GUI,textvariable=wd,font=FONT)
E1.pack()

B1 = ttk.Button(GUI,text='ถอน',command=calc)
B1.pack(pady= 50)

LResult = Label(GUI,textvariable=result,font=FONT)
LResult.pack()

GUI.mainloop()
#MYATM.py
from tkinter import *
from tkinter import ttk



global Budget
Budget = int(input('Please Enter your Budget:'))

def calc():
	witdraw = int(wd.get())
	global Budget
	Budget = Budget-witdraw
	bd.set(f'Budget is : {Budget:,d}')
	result.set(f'ถอนแล้วจำนวน {witdraw:,d} คงเหลือ {Budget:,d}')

GUI = Tk()
GUI.geometry('500x500')
GUI.title('KS-CodeBank')

FONT = ('Angsana New',20)

bd = StringVar()
bd.set(f'Budget is : {Budget}')
wd = StringVar()
result = StringVar()

L1 = ttk.Label(GUI,textvariable=bd,font=FONT)
L1.pack(pady=50)

E1 = ttk.Entry(GUI,textvariable=wd,font=FONT)
E1.pack()

B1 = ttk.Button(GUI,text='ถอน',command=calc)
B1.pack(pady= 50)

LResult = Label(GUI,textvariable=result,font=FONT)
LResult.pack()

GUI.mainloop()
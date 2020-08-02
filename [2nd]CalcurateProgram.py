#CalcurateProgram.py
from tkinter import *
from tkinter import ttk,messagebox

def Calcurate():
	input1 = int(value1.get())
	input2 = int(value2.get())
	res = input1 + input2
	result.set(f'คำตอบคือ {res:,d}')

'''def CalcuratE():
	input1 = int(value1.get())
	input2 = int(value2.get())
	ser = input1 + input2
	Result.set(f'คำตอบคือ {ser:,d}')'''

def add():
	messagebox.showinfo('วิธีบวก','นี่คือตัวอย่าง 1 + 1 = 2')

def Cricle(): #ถ้าฟังก์ชั้นใช้แล้วจบ ตัวแปรซ้ำได้ไม่มีผล ถ้าฟังก์ชั้นยังไม่จบ จะมีผล
	x = int(KK.get())
	sec = Pi * (x ** 2) #สามารถทำแบบนี้ได้เลย sec = 3.14 * (x ** 2) ไม่จำเป็นต้องไปแทนค่าเป็นค่า Pi หรือ ตัดวงเล็บไปก็ได้ผลลัพท์เดิม
	#sec = Pi * x ** 2 หรือแบบนี้ก็ได้ sec = 3.14 * x ** 2 [** คือ ยกกำลัง]
	result1.set(f'คำตอบคือ {sec:,.2f}') #:,.xf<--->x คือ จำนวนทศนิยม 

#######################New File####################################
def New1File():
	GUI2 = Tk()
	GUI2.title('CalcurateProgram')
	GUI2.geometry('500x500')

	L1 = ttk.Label(GUI2,text='โปรแกรมคำนวณ[ผมคือแท็บใหม่]',font=FONT)
	L1.pack(pady=50)

	'''value1 = StringVar()
	value2 = StringVar()
	Result = StringVar()
	Result.set('-------')

	E1 = ttk.Entry(GUI2,textvariable=value1,font=FONT)
	E1.pack(ipadx=10,ipady=5)

	E2 = ttk.Entry(GUI2,textvariable=value2,font=FONT)
	E2.pack(ipadx=10,ipady=5,pady=50)

	B1 = ttk.Button(GUI2,text='คำนวณ',command=CalcuratE)
	B1.pack(ipadx=10,ipady=5)

	CResult = Label(GUI2,textvariable=Result)
	CResult.pack()'''

	GUI2.mainloop()
#######################New File####################################
GUI = Tk() #GUI เป็กการตั้งชื่อ เพื่อที่จะใช้ Tk() 

GUI.title('CalcurateProgram')
GUI.geometry('500x500')


Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH)

F1 = Frame(Tab)
F2 = Frame(Tab)

Tab.add(F1,text='พื้นฐานคำนวณ')
Tab.add(F2,text='วงกลม')

menubar = Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='Close',command=GUI.quit)
file.add_command(label='New File',command=New1File)
menubar.add_cascade(label='File',menu=file)#สิ่งที่จะเอาไปวาง

calc = Menu(menubar,tearoff=0)
calc.add_command(label='การบวก',command=add)
calc.add_command(label='การลบ')
calc.add_command(label='การคูณ')
calc.add_command(label='การหาร')
menubar.add_cascade(label='การคำนวณ',menu=calc)



FONT = ('Angsana New',20)

L1 = ttk.Label(F1,text='โปรแกรมคำนวณ',font=FONT)#Lable ตัวหนังสือ
L1.pack(pady=50)

value1 = StringVar()
value2 = StringVar()
result = StringVar()
result.set('-------')

E1 = ttk.Entry(F1,textvariable=value1,font=FONT)
E1.pack(ipadx=10,ipady=5)

E2 = ttk.Entry(F1,textvariable=value2,font=FONT)
E2.pack(ipadx=10,ipady=5,pady=50)

B1 = ttk.Button(F1,text='คำนวณ',command=Calcurate)
B1.pack(ipadx=10,ipady=5)

LResult = Label(F1,textvariable=result)
LResult.pack()

######################F2#######################
L2 = ttk.Label(F2,text='โปรแกรมคำนวณ พท. วงกลม',font=FONT)#Lable ตัวหนังสือ
L2.pack(pady=50)

KK = StringVar()
Pi = float(3.14) #int ไม่นับทศนิยม ทำให้ค่า 3.14 จะโดนตัดไม่เอาไปคำนวณจะเหลือแค่ 3.00 ทำให้ค่าที่คำนวณมาผิดพลาด ถ้าจะคำนวณทศนิยมด้วยต้องใช้ float
result1 = StringVar()
result1.set('-------')

E5 = ttk.Entry(F2,textvariable=KK,font=FONT)
E5.pack(ipadx=10,ipady=5)

B2 = ttk.Button(F2,text='คำนวณ',command=Cricle)
B2.pack(ipadx=10,ipady=5)

RResult = Label(F2,textvariable=result1)
RResult.pack()

GUI.mainloop()


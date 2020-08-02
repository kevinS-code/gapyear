#GUICal.py

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('800x500') #GUI.geometry('X') X ขนาดโปรแกรม
GUI.title('โปรแกรมคำนวนของฉัน')
F1 = Frame()
F1.place(x=0,y=0)

FONT = ('Angsana New',20) #Entry ใส่ได้ Label ใส่ได้ Button ใส่ไม่ได้ Button จะเป้นอีกแบบหนึ่ง

v_width = StringVar() #StringVar() คือการรับค่ามาแบบString
v_long  = StringVar()

img = PhotoImage(file='football.png').subsample(3)
IM1 = ttk.Label(GUI,image=img)#GUI คือสิ่งที่เราจะเอาองค์ประกอบต่างๆเข้าไปวาง เราสามารถกำหนดชื่อตัวแปรแล้วเท่ากับคำสั่ง Fram() และ .place,.pack อะไรก็ได้ตามด้วยค่า x,y หรือต่ำแหน่งที่เราต้องการให้อยู่
IM1.place(x=100,y=25) #ใช้packได้ pack(padx=...,pady=...)>>>pack(ipadx=...,ipady=...) #pad ระยะห่างต่ำแหน่งของปุ่ม #ipad ขนาดของปุ่ม #pad กับ ipad ใช้ได้แค่กับ pack


E1 = ttk.Entry(GUI,textvariable=v_width,font=FONT) #E1 ชื่อช่องเก็บ
E1.place(x=300,y=25)


E2 = ttk.Entry(GUI,textvariable=v_long,font=FONT) #E2 ชื่อช่องเก็บ
E2.place(x=300,y=75)

def Calc():
	W = int(v_width.get()) # .get ดึงค่ามาจาก v_width #int หรือ float ก็ได้ float จะเป็นจุดทศนิยม
	L = int(v_long.get() )# .get ดึงค่ามาจาก v_long
	print('W,L',W,L)
	print(W*L)
	cal = W*L
	v_result.set('สนามนี้มีพึ้นที่ {:,d} ตร.ม.'.format(cal)) #อยากให้มี[,]ทุกสามหลัก :,d

B1 = ttk.Button(GUI,text='calculate',command=Calc)
B1.place(x=350,y=125) #ค่า B1 กับ Result จะกึ่งกลางกัน ก็ต่อเมื่อ x ของ B1 > x ของ Result 20 

v_result = StringVar()
v_result.set('-----ผลลัพท์-----')
Result= ttk.Label(GUI,textvariable=v_result,font=FONT,foreground='green') #foreground สี
Result.place(x=330,y=150) 
#ค่า place(x=299,y=150) เวลาเปลี่ยนจากผลลัพท์เป็นสนามนี้มีพึ้นที่ {:,d} ตร.ม. จะพอดีกับครอบของ E1,E2 เมื่อขนาดโปรแกรมหรือ .geometry เท่ากับ (800x500)

#on F1
'''B2 = ttk.Button(F1,text=1)
B2.grid(row=0,column=10)
B3 = ttk.Button(F1,text=2)
B3.grid(row=0,column=11)
B4 = ttk.Button(F1,text=3)
B4.grid(row=1,column=10)
B5 = ttk.Button(F1,text=4)
B5.grid(row=1,column=11)
B6 = ttk.Button(F1,text='calculate')
B6.grid(row=0,column=12)'''
GUI.mainloop()

#openbroswer.py
import pyautogui 
import time 
import webbrowser #นำเข้า browser โดยจะใช้ browser หลักของคอมพิวเตอร์เครื่องนั้น
import pyperclip as cp
#as คือคำสั่งที่เราใช่เรียกแทนตัวแปร
#เช่นในกรณีนี้ให้ import pyperclip as cp
#คำสั่งที่เป็น pyperclip.x(y) จะเขียนแค่ cp.x(y)
#ถ้าเปลี่ยนคำหลัง as ว่า SG จะเขียนเป็น SG.x(y) (จะเป็นรูปแบบนี้ import pyperclip as SG)
#chrome = (269,743)#เป็นการกำหนดตัวแปร z=(x,y)ค่า z คือชื่่อตัวแปร ค่า x,y ในวงเล็บ() คือค่าแกน x แกน y
#ถ้าใช่คำสั่ง as แทนตัวแปรจะไม่สามารถกลับไปใช้ตัวแปรเดิมได้
#เช่น import pyperclip as cp ต้องใช่ cp จะใช่ pyperclip ไม่ได้
#ไม่งั่นจะขึ้น Error (จะเป็นรูปแบบนี้ NameError: name 'pyperclick' is not defined)
#pyautogui.click(chrome)#คำสั่ง pyautogui.click(z)จะคลิกไปยังตัวแปรที่เรากำหนด
#ซึ่งคอมแต่ละคนตัวแปรก็อาจไม่ได้อยู่ตำแหน่งเดียวกัน
url = 'https://www.google.com/'
webbrowser.open(url)

#time.sleep(x) สามารถเปลี่ยน x ได้ถ้า Browser ใครเปิดช้า
time.sleep(3)
pyautogui.write('Thailand',interval=0.2)
#interval คือ การแสดงผลข้อความที่ละตัว interval = x ยิ่ง x เยอะยิ่งช้า
#interval ใน Google Translate แปลว่าระยะห่าง
pyautogui.press('enter')

#########
def Search(word):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')
        

    pyautogui.press('backspace')
    #ไม่มี interval การแสดงผลของข้อความจะมาที่เดียวเลย
    pyautogui.write(word)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(word+ '.png')

Search('singapore')
Search('usa')
Search('china')
#################################
def SearchTH(word):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')
    pyautogui.press('backspace')
    #pyperclick.copy(world)
    cp.copy(word)
    time.sleep(3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(word+ '.png')
    
SearchTH('ประเทศญี่ปุ่น')
SearchTH('ประเทศรัสเซีย')
SearchTH('ประเทศสวิตเซอร์แลนด์')
#################################
#1st

#ATM.py


money = 20000

print('กด 1 : ถอดเงิน')
print('กด 2 : เช็คยอดเงินเงิน')
print('กด q : ออกจากระบบ')
print('------------')
menu = input('กรุณาเลือกเมนู: ') #user เลือกแล้วเราจะเก็บเมนูไว้

while menu != 'q':
	if menu == '1':
		print('<<<< ถอดเงิน >>>>')
		withdraw = int(input('กรุณากรองจำนวนเงิน: '))
		while withdraw > money:
			print('เงินในบัญชีไม่พอ กรุณากรองยอดงินในบัญขีให้ถูกต้อง')
			withdraw = int(input('กรุณากรองจำนวนเงิน: '))
		print('กรุณารับเงินงิน {} บาท'.format(withdraw))	
		money = money - withdraw # เอาจำนวนเงินตอนนี้มาลบกับเงินที่ถอน
		print('คุณมียอดเงินคงเหลือ {} บาท'.format(money))

	elif menu == '2':
		print('ยอดเงินของคุณคือ: {} บาท'.format(money))	
	print('กด 1 : ถอดเงิน')
	print('กด 2 : เช็คยอดเงินเงิน')
	print('กด Q : ออกจากระบบ')
	menu = input('กรุณาเลือกเมนู: ')
print('ขอบคุณที่ใช้บริการ กรุณารับบัตรคืน')
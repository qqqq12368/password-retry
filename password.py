password = 'a123456'
b = '3' #可輸入密碼次數
while True
	a = input('請輸入密碼')
	if a == password:
		print('登入成功')
		break
	elif a != password:
		b = b - 1
		print('密碼錯次', '還有',b,'次機會')

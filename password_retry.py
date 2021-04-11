# 密碼重試程式
# password = 'a123456'
# 讓使用者輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功"
# 如果不正確 就印出 "密碼錯誤 還有___次機會"
password = 'a123456' #正解
b = 3 #可輸入密碼次數
while b > 0:
	a = input('請輸入密碼')
	if a == password:
		print('登入成功')
		break
	else: 
		b = b - 1
		print('密碼錯次', '還有', b, '次機會')
		
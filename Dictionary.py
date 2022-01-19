from MyModule import*
rus_list=[]
rus=failist_lugemine('rus.txt',rus_list)
print(rus_list)
ang_list=[]
ang=failist_lugemine('ang.txt',ang_list)
print(ang_list)

print("***Словарь-переводчик с английского на русский и с русского на английский***")
while True :
	menu=input("Проговаривать-R,\nНовое слово-H,\nПосмотреть все слова-S")
	
	if menu.upper=="H":
		rus_list=uus_sõna("rus.txt",input("Новое слово:"))
		ang_list=uus_sõna("ang.txt",input("Новое слово:"))
	elif menu.upper=="S":
		print(rus_list)
		pritn(ang_list)
		
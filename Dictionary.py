from MyModule import*
rus_list=[]
ang_list=[]
rus=failist_lugemine('rus.txt',rus_list)
ang=failist_lugemine('ang.txt',ang_list)

print("***Словарь-переводчик с английского на русский и с русского на английский***")
while True :
	menu=input("Проговаривать-R,\nНовое слово-H,\nПосмотреть все слова-S\nДобавить слово-J\nПеревод-A\n")
	
	if menu.upper()=="H":
		rus_list=uus_sõna("rus.txt",input("Новое слово:"),rus_list)
		ang_list=uus_sõna("ang.txt",input("New:"),ang_list)
	elif menu.upper()=="S":
		for i in range (len(ang_list)):
			print(rus_list[i]+"-"+ang_list[i])
	elif menu.upper()=="J":
		correction()
	elif menu.upper()=="A":
		tõlkimine()
	elif menu.upper()=="R":
		keel=input("Что проговорить?")#ru et en
		sõna=input("Sõna:")
		heli(sõna,keel)
	else:
		break
		
break
		

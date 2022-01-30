from random import shuffle
import random
def failist_lugemine(f:str,l:list):
	"""Информация из файла l
	"""
	fail=open(f,'r',encoding="utf-8-sig")#,encoding="utf-8-sig"
	for rida in fail:
		l.append(rida.strip())#'\n'
	fail.close()
	return l

def uus_sõna(f:str,rida:str,l:list)->list:
	"""Одно слово или предложение (rida) мы сохраняем в файл
    :param str f : имя файла 
    :param str rida : добавить слово
    """
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	#l=failist_lugemine(f)
	#return l

def tõlkimine(l1:list,l2:list):
	"""Переводим слова 
	:param list l1:Список первого языка
	:param list l2:Список второго языка
	"""
	sõna=input("Введите слово:")
	if sõna in l1:
		tõlk=l2[l1.index(sõna)]
		print(sõna+"-"+tõlk)
	elif sõna in l2:
		tõlk =l1[l2.index(sõna)]
		print(sõna+"-"+tõlk)
	else:
		print("Слова нет")

def correction(sõna:str,l:list):
	for i in range(len(l)):
		if l[i]==sõna:
			uus_sona=sõna.replace(sõna,input("Новое слово: "))
			l.insert(i,uus_sõna)
			l.remove(sõna)
	return l

def kontrol(l1:list,l2:list):
    summa=0
    lists=[]
    lists.extend(l1)
    lists.extend(l2)
    random.shuffle(lists)
    print('random list ',lists)
    for i in range(len(l1)):
        otvet=input(f"Переведи данное слово - '{lists[i]}': ")
        if otvet in l1 or otvet in l2:
            if lists[i] in l1:
               if l1.index(lists[i])==l2.index(otvet):
                    summa+=1
                    print('правильно!')
                    print()
            elif lists[i] in l2:
                if l2.index(lists[i])==l1.index(otvet):
                    summa+=1
                    print('правильно!')
                    print()
        else:
            print('Неправильно!')
            print()
    resultPer=(summa/len(l1))*100
    print(f"Ваш результат: {resultPer}%")
#import os
#from gtts import gTTS

#def heli(text:str,keel:str):
#	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3") 
#	os.system("heli.mp3")

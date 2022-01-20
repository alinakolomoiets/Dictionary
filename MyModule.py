def failist_lugemine(f:str,l:list):
	"""Info failist f listisse l
	"""
	fail=open(f,'r',encoding="utf-8-sig")#,encoding="utf-8-sig"
	for rida in fail:
		l.append(rida.strip())#'\n'
	fail.close()
	return l

def rida_salvestamine(f:str,rida:str):
	"""Loetelu salvaestame failisse
	"""	
	fail=open(f,'a')#перезапись
	fail.write(rida+'\n')
	fail.close()

def uus_sõna(f:str,rida:str,l:list)->list:
	"""Üks sõna või lause (rida) salvestame failisse
    :param str f:fail nimetus
    :param str rida : lisatav sõna
    """
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	l=failist_lugemine(f)
	return l

def tõlkimine(l1:list,l2:list):
	sõna=input("Что переводить?")
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
			uus_sõna=sõna.replace(sõna,input("Новое слово"))
			l.insert(i,uus_sõna)
			l.remove(sõna)
	return l


import os
from gtts import gTTS

def heli(text:str,keel:str):
	obj=gTTs(text=text,lang=keel,slow=False).save("heli.mp3") 
	os.system("heli.mp3")



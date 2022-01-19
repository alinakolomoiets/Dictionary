def failist_lugemine(f:str,l:list):
	"""Info failist f listisse l
	"""
	fail=open(f,'r',encoding="utf-8-sig")#,encoding="utf-8-sig"
	for rida in fail:
		l.append(rida.strip())#'\n'
	fail.close()
	return l

def failist_lugemine(f:str,l:list):
	"""Info failist f listisse l
	"""	
	fail=open(f,'r',encoding="utf-8-sig")
	for rida in fail:
		l.append(rida.strip())
	fail.close()
	return l

def failisse_salvestamine(f:str,l:list):
	"""Loetelu salvaestame failisse
	"""	
	fail=open(f,'w')#перезапись
	for el in l:
		fail.write(el+'\n')
	fail.close()

def uus_sõna(f:str,rida:str)->list:
	"""Üks sõna või lause (rida) salvestame failisse
    :param str f:fail nimetus
    :param str rida : lisatav sõna
    """
	with open(f,'a',encoding="utf-8-sig") as fail:
		fail.write(rida+'\n')
	l=failist_lugemine(f)
	return l

#def kõik_sõna(f:str
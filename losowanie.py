import codecs
from random import randint

def losuj_imie(ile):
	filename='imiona.txt'
	names =[]
	wylosowane = set()
	with codecs.open(filename,'r',encoding='utf8') as f:
		names = f.read().splitlines()

	while(len(wylosowane)<ile):
		los = names[randint(0, len(names)-1)]
		wylosowane.add(los)
	return(wylosowane)

def losuj_nazwisko(ile):
	filename='nazwiska.txt'
	names =[]
	wylosowane = set()
	with codecs.open(filename,'r',encoding='utf8') as f:
		names = f.read().splitlines()

	while(len(wylosowane)<ile):
		los = names[randint(0, len(names)-1)]
		wylosowane.add(los)
	return(wylosowane)
#skrypt generujacy imie i nazwisko dla postaci 
#żyjącej w 20-leciu międzywojennym w polsce
#przydatny do sesji 'call of cthulu' osadzonych w polsce :)
import codecs

filename='scrapped_data.txt'

with codecs.open(filename,'r',encoding='utf8') as f:
	#names = f.readlines()
	names = f.read().splitlines() #pozbywam się /r/n

imiona = []
nazwiska = []
new_names = []

for n in names:
	new_names.append(n.split("(")[0])
	#oczyszam z 'X Y (generał)'

for n in new_names: # wyjątki! (Józef Krautwald de Annau) <- trzy ostatnie człony w tym przypadku to nazwisko a pierwszy to imię
	if(n.split()[-1]!='Sulima') & (n.split()[-1]!='Annau'):
		imiona.append(n.split()[:-1]) #bierzemy wszystkie imiona (np. Jan Adam Mariusz Iksiński)	
		nazwiska.append(n.split()[-1]) #nazwiska Y-Z traktuję jako jedno
	else:
		nazwiska.append(n.split()[-3]+" "+n.split()[-2]+" "+n.split()[-1]) #obsługa wyjątku ( X + 'de' + Y)

#łacze wszystkie wielokrotne imiona w jednowymiarowa liste
flat_list = [item for sublist in imiona for item in sublist]

#usuwam powtorzenia
flat_list = list(set(flat_list))
nazwiska = list(set(nazwiska))

#sortowanie alfabetyczne
flat_list.sort()
nazwiska.sort()

#zapis do pliku
with codecs.open('imiona.txt','w',encoding='utf8') as f:
	for i in flat_list:
		f.write(i + '\n')
with codecs.open('nazwiska.txt','w',encoding='utf8') as f:
	for i in nazwiska:
		f.write(i + '\n')
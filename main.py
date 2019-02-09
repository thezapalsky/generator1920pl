from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from losowanie import *
from os import listdir
from kivy.core.window import Window

kv_path = './kv/'
for kv in listdir(kv_path):
	Builder.load_file(kv_path+kv)
akt_mode=0
akt_gender=0

class Losuj1Button(Button):
	pass

class Losuj3Button(Button):
	pass

class Losuj10Button(Button):
	pass

class Gender(Button):
	pass

class Mode(Button):
	pass

class Container(GridLayout):
	display = ObjectProperty()
	akt_mode=0
	#zjanuszowane to loswanie, musze poprawic ale narazie dziala XD
	def losuj_jeden(self):
		self.display.text=""
		if(akt_mode==0):
			for imie in losuj_imie(1):
				self.display.text+=imie+'\n'
		if(akt_mode==1):
			for naz in losuj_nazwisko(1):
				self.display.text+=naz+'\n'
		if(akt_mode==2):
			for imie in losuj_imie(1):
				for naz in losuj_nazwisko(1):
					nazwisko = naz
				self.display.text+=imie+' '+nazwisko+'\n'
		
	def losuj_trzy(self):
		self.display.text=""
		if(akt_mode==0):
			for imie in losuj_imie(3):
				self.display.text+=imie+'\n'
		if(akt_mode==1):
			for naz in losuj_nazwisko(3):
				self.display.text+=naz+'\n'
		if(akt_mode==2):
			for imie in losuj_imie(3):
				for naz in losuj_nazwisko(1):
					nazwisko = naz
				self.display.text+=imie+' '+nazwisko+'\n'

	def losuj_dziesiec(self):
		self.display.text=""
		if(akt_mode==0):
			for imie in losuj_imie(10):
				self.display.text+=imie+'\n'
		if(akt_mode==1):
			for naz in losuj_nazwisko(10):
				self.display.text+=naz+'\n'
		if(akt_mode==2):
			for imie in losuj_imie(10):
				for naz in losuj_nazwisko(1):
					nazwisko = naz
				self.display.text+=imie+' '+nazwisko+'\n'

	def mode_change(self):
		#0 imie
		#1 nazwisko
		#2 imie + nazwisko
		global akt_mode
		akt_mode=(akt_mode+1)%3
		if(akt_mode==0):
			return "imie"
		if(akt_mode==1):
			return "nazwisko"
		if(akt_mode==2):
			return "imie + nazwisko"

	def gender_change(self):
		#0 man
		#1 woman
		global akt_gender
		akt_gender=(akt_gender+1)%2
		if(akt_gender==0):
			return "mezczyzna"
		else:
			return "kobieta [TBA]"

class MainApp(App):
	def build(self):
		self.title = 'Generator nazwisk z okresu 20-lecia międzywojennego'
		return Container()


if __name__ == "__main__":
	app = MainApp()
	Window.size = (1200, 600)
	app.run()
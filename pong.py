from tkinter import *
import random
import time


class Ball:
	def __init__(self,pole,rakietka, colour):
		self.pole = pole
		self.rakietka = rakietka 
		self.id = pole.create_oval(10,10,25,25, fill = colour)
		self.pole.move(self.id, 245,100)
		start = [-3 ,-2, -1, 1, 2, 3]
		random.shuffle(start)
		self.x = start[0]
		self.y = -3
		self.wysokosc_pola = self.pole.winfo_height()
		self.szerokosc_pola = self.pole.winfo_width()
		self.ziemia = False
	def trafienie (self,pozycja):
		pozycja_rakietki = self.pole.coords(self.rakietka.id)
		if pozycja[2] >= pozycja_rakietki[0] and pozycja [0] <= pozycja_rakietki[2]:
			if pozycja[3] >= pozycja_rakietki[1] and pozycja[3]<=pozycja_rakietki[3]:
				return True
			return False

	def rysuj(self):
		self.pole.move(self.id, self.x, self.y)
		pozycja = self.pole.coords(self.id)
		if pozycja[1] <= 0:
			self.y = 2
		if pozycja[3] >= self.wysokosc_pola:
			self.ziemia = True
		if self.trafienie(pozycja) == True:
			self.y = -2
		if pozycja[0] <= 0:
			self.x = 2
		if pozycja[2] >= self.szerokosc_pola:
			self.x = -2
			

class Rakietka:
	def __init__(self, pole, colour):
		self.pole = pole
		self.id = pole.create_rectangle(0,0,100,10, fill = colour)
		self.pole.move(self.id, 200, 300)
		self.x = 0
		self.szerokosc_pola = self.pole.winfo_width()
		self.pole.bind_all('<KeyPress-Left>', self.w_lewo)
		self.pole.bind_all('<KeyPress-Right>', self.w_prawo)
	def rysuj(self):
		self.pole.move(self.id, self.x, 0)
		pozycja_rakietki = self.pole.coords(self.id)
		if pozycja_rakietki[0] <= 0:
			self.x = 0
		elif pozycja_rakietki [2] >= self.szerokosc_pola:
			self.x = 0
	def w_lewo(self, zdarzenie):
		self.x = -2
	def w_prawo(self,zdarzenie):
		self.x = 2




tk = Tk()
tk.title("Pong")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
pole = Canvas(tk, width=500, height = 400, bd = 0, highlightthickness = 0)
pole.pack()
tk.update()

rakietka = Rakietka(pole, 'blue')
ball = Ball(pole, rakietka, 'red')

time.sleep(2)
while 1:
	#time.sleep(2)
	if ball.ziemia == False:
		ball.rysuj()
		rakietka.rysuj()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)


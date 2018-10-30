#/usr/bin/python3
from tkinter import *

 
class Anwendung(Frame):#Klasse = Bauplan für Objekte


  def __init__(self,master=None):
    Frame.__init__(self, master)
    t1 = 'text1'
    t2 = 'text2'
    t3 = 'text3'
    #label - grid
    Label(master,text=t1).grid(row=2, column=0, padx=5, pady=5)
    Label(master,text=t2).grid(row=2, column=1, padx=5, pady=5)
    Label(master,text=t3).grid(row=2, column=2, padx=5, pady=5)
    Label(master,text="Eingabe").grid(row=0)
    Button(master, text='Button 1', width=20,command=self.action, padx=10, pady=10).grid(row=3, column=0)
    Button(master, text='Button 2', width=20,command=self.action, padx=10, pady=10).grid(row=3, column=1)
    Button(master, text='Button 3', width=20,command=self.action, padx=10, pady=10).grid(row=3, column=2)
    self.lb1=Label(master, width=20)
    self.lb1.grid(row=0, column=2)
    self.nname=Entry(master)
    self.nname.grid(row=0, column=1)
  def action(self):
    self.lb1.config(text = self.nname.get())


myWin = Tk()# objekt erzeugen
myWin.wm_title('Titel')
app = Anwendung(master=myWin)
app.mainloop()

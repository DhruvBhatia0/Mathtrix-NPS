from tkinter import *
class statsprint:
    
    def __init__(self,win):
        #now displaying data
        
        self.lb1=Label(win, text='General information:')
        self.lb2=Label(win, text='Population: 2803855')
        self.lb3=Label(win, text='Cases: 462882')
        self.lb4=Label(win, text='Deaths: 10952')
        self.lb5=Label(win, text='Mortality Rate: 2.37%')
        self.lb6=Label(win, text='    Mortality Rates by Age:')
        self.lb7=Label(win, text='0-10  :     1.52%')
        self.lb8=Label(win, text='10-20 :     1.28%')
        self.lb9=Label(win, text='20-40 :     1.26%')
        self.lb0=Label(win, text='40-60 :     2.38%')
        self.lb11=Label(win, text='>60   :     5.09%')
        self.lb11=Label(win, text='Close this window for graphical analysis')
        
        self.lb1.place(x=0, y=0)
        self.lb2.place(x=0, y=50)
        self.lb3.place(x=0, y=100)
        self.lb4.place(x=0, y=150)
        self.lb5.place(x=0, y=200)
        self.lb6.place(x=0, y=250)
        self.lb7.place(x=0, y=300)
        self.lb8.place(x=0, y=350)
        self.lb9.place(x=0, y=400)
        self.lb0.place(x=0, y=450)
        self.lb11.place(x=0, y=500)
        
        
def finalstat():
    windowf2=Tk()
    mywin=statsprint(windowf2)
    windowf2.title('COVID Data Results')
    windowf2.geometry("2560x1600") 
    windowf2.mainloop()
finalstat()
import tkinterstatspic

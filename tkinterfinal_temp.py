from tkinter import *
global t
class MyWindow:
    def __init__(self, win):
        global t
        self.lbl1=Label(win, text='Enter your name')
        self.lbl2=Label(win, text='Enter your age')
        self.lbl3=Label(win, text='Do you have diabetes? [1 for yes/0 for no]')
        self.lbl4=Label(win, text='Do you have abnormal BP? [1 for yes/0 for no]')
        self.lbl5=Label(win, text='Do you have respiratory disorders? [1 for yes/0 for no]')
        self.lbl6=Label(win, text='Enter your x coordinate')
        self.lbl7=Label(win, text='Enter your y coordinate')
        self.lbl8=Label(win, text='After submitting, close this window. your results will pop up as a new window')
        #self.lbl=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.t4=Entry(bd=3)
        self.t5=Entry(bd=3)
        self.t6=Entry(bd=3)
        self.t7=Entry(bd=3)
        self.btn1 = Button(win, text='Proceed')
        #self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=0, y=0)
        self.lbl2.place(x=0, y=50)
        self.lbl3.place(x=0, y=200)
        self.lbl4.place(x=0, y=100)
        self.lbl5.place(x=0, y=150)
        self.lbl6.place(x=0, y=250)
        self.lbl7.place(x=0, y=300)
        self.lbl8.place(x=0, y=350)
        
        
        self.t1.place(x=150, y=0)
        self.t2.place(x=150, y=50)
        self.t3.place(x=270, y=100)
        self.t4.place(x=350, y=150)
        self.t5.place(x=270, y=200)
        self.t6.place(x=150, y=250)
        self.t7.place(x=150, y=300)
        self.b1=Button(win, text='Submit', command=self.trial)
        #self.b2=Button(win, text='Subtract')
        #self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=50, y=400)
        #self.b2.place(x=200, y=150)
        
    def trial(self):
        global t
        val1=(self.t1.get())
        val2=(self.t2.get())
        val3=(self.t3.get())
        val4=(self.t4.get())
        val5=(self.t5.get())
        val6=(self.t6.get())
        val7=(self.t7.get())
        t=(val1,val2,val3,val4,val5,val6,val7)

'''def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
'''
def main():
    global t
    window=Tk()
    mywin=MyWindow(window)
    window.title('COVID Data Analysis')
    window.geometry("1000x1000")
    window.mainloop()
    #print(t)
    return t
#print(main())
'''
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)

lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=180, y=50)

v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text="Cricket", variable=v1)
C2 = Checkbutton(window, text="Tennis", variable=v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

window.title('Covid data')
window.geometry("400x300+10+10")
window.mainloop()'''

from tkinter import *
class hm:
    def __init__(self,win):
        pass
    
def statspicdisplay():
    windowf1=Tk()
    mywin=hm(windowf1)
    windowf1.title('COVID Data Stats')
    windowf1.geometry("2560x1600")
    canvas = Canvas(windowf1, width = 800, height = 386)      
    canvas.pack()      
    img = PhotoImage(file="statspic.png")      
    canvas.create_image(20,20, anchor=NW, image=img) 
    windowf1.mainloop()
statspicdisplay()

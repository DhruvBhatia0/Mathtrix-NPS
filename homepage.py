'''main home page
for importing data '''
import tkinter as tk 
global a
root=tk.Tk() 

# setting the windows size 
root.geometry("2560x1600") 

# declaring string variable 
# for storing name and password 
name_var1=tk.StringVar()
name_var2=tk.StringVar()
name_var3=tk.StringVar()
name_var4=tk.StringVar()
name_var5=tk.StringVar()


# defining a function that will 
# get the name and password and 
# print them on the screen 
def submit():
    trial()
    name1=name_entry1.get()
    name2=name_entry2.get()
    name3=name_entry3.get()
    name4=name_entry4.get()
    name5=name_entry5.get()
    print("The name is : " + name1)
    print("The name is : " + name2)
    print("The name is : " + name3)
    print("The name is : " + name4)
    print("The name is : " + name5) 
    name_var1.set("")
    name_var2.set("")
    name_var3.set("")
    name_var4.set("")
    name_var5.set("")
    root.mainloop() 
    return (name1,name2,name3,name4,name5)
def trial():
        global a
        # creating a label for 
        # name using widget Label 
        name_label1 = tk.Label(root, text = 'Enter your name please:', font=('calibre', 10, 'bold'))
        name_entry1 = tk.Entry(root, textvariable = name_var1,font=('calibre',10,'normal'))

        name_label2 = tk.Label(root, text = 'Enter your age please:', font=('calibre', 10, 'bold')) 
        name_entry2 = tk.Entry(root, textvariable = name_var2,font=('calibre',10,'normal'))

        name_label3 = tk.Label(root, text = 'Do you have diabetes [y/n]', font=('calibre', 10, 'bold')) 
        name_entry3 = tk.Entry(root, textvariable = name_var3,font=('calibre',10,'normal'))

        name_label4 = tk.Label(root, text = 'Do you have abnormal BP [y/n]', font=('calibre', 10, 'bold')) 
        name_entry4 = tk.Entry(root, textvariable = name_var4,font=('calibre',10,'normal'))

        name_label5 = tk.Label(root, text = 'Do you have Respiratory Illness [y/n]', font=('calibre', 10, 'bold')) 
        name_entry5 = tk.Entry(root, textvariable = name_var5,font=('calibre',10,'normal'))

        # creating a button using the widget 
        # Button that will call the submit function 
        
        
        # placing the label and entry in 
        # the required position using grid 
        # method 
        name_label1.grid(row=0,column=0)
        name_entry1.grid(row=0,column=1)

        name_label2.grid(row=1,column=0)
        name_entry2.grid(row=1,column=1)

        name_label3.grid(row=2,column=0)
        name_entry3.grid(row=2,column=1)

        name_label4.grid(row=3,column=0)
        name_entry4.grid(row=3,column=1)

        name_label5.grid(row=4,column=0)
        name_entry5.grid(row=4,column=1) 
        sub_btn=tk.Button(root,text = 'Show results', command = smoothdestroy())
        sub_btn.grid(row=5,column=1) 
        if a:
            root.destroy()
        # performing an infinite loop 
        # for the window to display 
def smoothdestroy():
    global a
    a=True
submit()

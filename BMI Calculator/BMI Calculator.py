from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('BMI Calculator')
root.resizable(width=False, height=False)
w=550
h=350
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def BMI_calculator():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    height = height/100
    BMI = weight/(height*height)
    BMI_index = "Your Body Mass Index is {}".format(round(BMI,2))
    if (BMI > 0):
        if (BMI <= 16):
            txt.insert(INSERT, BMI_index)
            txt.insert(INSERT, "\nYou are severaly Underweight")
        elif (BMI <= 18.5):
            txt.insert(INSERT, BMI_index)
            txt.insert(INSERT, "\nYou are Underweight")
        elif (BMI <= 25):
            txt.insert(INSERT, BMI_index)
            txt.insert(INSERT, "\nYou are Perfect fit !!")
        elif (BMI <= 30):
            txt.insert(INSERT, BMI_index)
            txt.insert(INSERT, "\nYou are Overweight")
        else:
            txt.insert(INSERT, BMI_index)
            txt.insert(INSERT, "\nYou are severaly Overweight")
    else:
        messagebox.showerror("Error", "\tYour values are Invalid. \n\t Enter valid values")

title=Label(root, text="BMI Calculator",font=("times new roman",30,"bold"),bg="#00cc00",bd=10)
title.place(x=0,y=0,relwidth=1)

value_Frame = Frame(root,width=100,height=100,padx=20)
value_Frame.place(x=0, y=100)

height_label = Label(value_Frame, text = "Enter Height in cm : ", font=('Courier', 15))
height_label.grid(row = 1, column = 0)
weight_label = Label(value_Frame, text = 'Enter weight in kg : ', font=('Courier', 15))
weight_label.grid(row = 2, column = 0)

height_entry = Entry(value_Frame, bd=2, font=('Courier', 14))
height_entry.grid(row = 1, column = 1)
weight_entry = Entry(value_Frame, bd=2, font=('Courier', 14))
weight_entry.grid(row = 2, column = 1)

submit = Button(value_Frame, text='Add Email', command=BMI_calculator, font=('Courier', 14),bg="#008CBA")
submit.grid(row=3, column=1, pady=20, ipadx=50, ipady=3)

txt = Text(value_Frame, width=50, height=2, wrap=WORD, font=("times new roman",15,"bold"),bg="#00cc00")
txt.grid(row=4, column=0, columnspan=2, pady=5, ipadx=10, ipady=2)

root.mainloop()


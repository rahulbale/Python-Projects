from AddBook import *
from ViewBook import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


root = Tk()
root.title("Library management")
w = 550
h = 550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(width=False, height=False)

# Adding a background image
background_image = Image.open("background.jpg")
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340, image=img)
Canvas1.pack(expand=True, fill=BOTH)

'''
conn = sqlite3.connect('libary_books.db')

c = conn.cursor()


c.execute("""CREATE TABLE books
            (bid INT PRIMARY KEY NOT NULL, 
            title TEXT NOT NULL, 
            author TEXT NOT NULL, 
            status TEXT NOT NULL);""")

c.execute("""CREATE TABLE book_issued
            (bid INT PRIMARY KEY NOT NULL, 
            issueto TEXT );""")


print("Successfully  Table Created")

conn.commit()
conn.close()
'''


headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel1=Label(headingFrame1, text="Welcome to \n B.N.N Library", font=('Courier',15,"bold"), bg='black', fg='white')
headingLabel1.place(relwidth=1, relheight=1)

btn1 = Button(root, text = 'Add Book', font=('Courier', 12), bg = 'black', fg = 'white', command = addBooks)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root, text = 'Delete Book', font=('Courier', 12), bg = 'black', fg = 'white', command = deleteBook)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root, text = 'View Book List', font=('Courier', 12), bg = 'black', fg = 'white', command = viewBooks)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root, text = 'Issue Book to Student', font=('Courier', 12), bg = 'black', fg = 'white', command = issue_books)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root, text = 'Return Book', font=('Courier', 12), bg = 'black', fg = 'white', command = return_Book)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()

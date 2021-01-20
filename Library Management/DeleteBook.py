from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('libary_books.db')

cur = conn.cursor()

bookTable = "books"
issueTable = "book_issued"


def delete():
    bid = bookInfo1.get()

    try:
        if bookTable:
            cur.execute("DELETE FROM "+bookTable+" WHERE bid = "+bid)
            conn.commit()
        else:
            cur.execute("DELETE FROM " + issueTable + " WHERE bid = "+bid)
            conn.close()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showerror('Error', "Please check Book ID")


    bookInfo1.delete(0, END)

    root.destroy()


def deleteBook():

    global bookInfo1, root

    root = Tk()
    root.title("Library management")
    w = 550
    h = 550
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.resizable(width=False, height=False)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#91b0d8")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    Label(headingFrame1, text="Delete Book", font=('Courier', 15, "bold"),
          bg='black', fg='white').place(relwidth=1, relheight=1)

    mainFrame = Frame(root, bg='black')
    mainFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(mainFrame, text = "Book Id : ", font=('Courier', 12, "bold"),
          bg='black', fg='white').place(relx=0.07, rely=0.4)

    bookInfo1 = Entry(mainFrame, font=('Courier'))
    bookInfo1.place(relx=0.3, rely=0.4, relwidth=0.6, relheight=0.08)

    submitBtn = Button(root, text="Delete", bg="black", fg="white", font=('Courier', 10), command=delete)
    submitBtn.place(relx=0.25, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="black", fg="white", font=('Courier', 10), command=root.destroy)
    quitBtn.place(relx=0.55, rely=0.85, relwidth=0.18, relheight=0.08)

    root.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3


def bookInsert():

    try:
        cur.execute("INSERT INTO " + bookTable + " VALUES (:bid, :title, :author, :status)",
                    {
                        'bid': bookInfo1.get(),
                        'title': bookInfo2.get(),
                        'author': bookInfo3.get(),
                        'status': bookInfo4.get()
                    }
                    )
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', "Book added successfully")

    except:
        messagebox.showinfo("Error","Can't add data into Database")

    root.destroy()


def addBooks():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, conn, cur, bookTable, root

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
    Canvas1.config(bg="#35bfe6")
    Canvas1.pack(expand=True, fill=BOTH)


    conn = sqlite3.connect('libary_books.db')

    cur = conn.cursor()

    bookTable = "books"

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel1 = Label(headingFrame1, text="Add Books", font=('Courier', 15, "bold"), bg='black', fg='white')
    headingLabel1.place(relwidth=1, relheight=1)

    mainFrame = Frame(root, bg='black')
    mainFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(mainFrame, text="Book ID : ", bg="black", fg="white", font=('Courier', 12))
    lb1.place(relx=0.05, rely=0.2, relheight=0.1)

    bookInfo1 = Entry(mainFrame, font=('Courier', 12))
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.1)

    # Book Title
    lb2 = Label(mainFrame, text='Title : ', font=('Courier', 12), bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.1)

    bookInfo2 = Entry(mainFrame, font=('Courier', 12))
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.1)

    # Bool Author
    lb3 = Label(mainFrame, text='Author : ', font=('Courier', 12), bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.1)

    bookInfo3 = Entry(mainFrame, font=('Courier', 12))
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.1)

    # Bool Status
    lb4 = Label(mainFrame, text='Status : ', font=('Courier', 12), bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.1)

    bookInfo4 = Entry(mainFrame, font=('Courier', 12))
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.1)

    submitBtn = Button(root, text="Submit", bg="black", fg="white", font=('Courier', 10), command=bookInsert)
    submitBtn.place(relx=0.25, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="black", fg="white", font=('Courier', 10), command=root.destroy)
    quitBtn.place(relx=0.55, rely=0.85, relwidth=0.18, relheight=0.08)

    root.mainloop()





from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('libary_books.db')

cur = conn.cursor()

bookTable = "books"
issueTable = "book_issued"

allbid = []

def returnn():
    global status, check

    bid = bookInfo1.get()

    try:
        cur.execute("SELECT bid FROM " + issueTable)
        conn.commit()
        for i in cur:
            allbid.append(i[0])

        id = int(bid)
        if id in allbid:

            cur.execute("SELECT status FROM " + bookTable + " WHERE bid = " +bid)
            conn.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")


    try:
        issue_id = int(bid)
        if issue_id in allbid and status == True:
            cur.execute("DELETE FROM " + issueTable + " WHERE bid = " +bid)
            conn.commit()
            cur.execute("UPDATE " + bookTable + " set status = 'avail' where bid = " + bid)
            conn.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allbid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")


    allbid.clear()
    root.destroy()


def return_Book():

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
    Canvas1.config(bg="#f1d8cc")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    Label(headingFrame1, text="Return Book", font=('Courier', 15, "bold"),
          bg='black', fg='white').place(relwidth=1, relheight=1)

    mainFrame = Frame(root, bg='black')
    mainFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(mainFrame, text = "Book Id : ", font=('Courier', 12, "bold"),
          bg='black', fg='white').place(relx=0.07, rely=0.4)

    bookInfo1 = Entry(mainFrame, font=('Courier'))
    bookInfo1.place(relx=0.3, rely=0.4, relwidth=0.6, relheight=0.08)

    submitBtn = Button(root, text="Return", bg="black", fg="white", font=('Courier', 10), command= returnn)
    submitBtn.place(relx=0.25, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="black", fg="white", font=('Courier', 10), command=root.destroy)
    quitBtn.place(relx=0.55, rely=0.85, relwidth=0.18, relheight=0.08)

    root.mainloop()


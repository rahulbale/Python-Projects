from tkinter import *
from tkinter import messagebox
import sqlite3



def viewBooks():

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
    Canvas1.config(bg="#e82f3a")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel1 = Label(headingFrame1, text="View Books", font=('Courier', 15, "bold"), bg='black', fg='white')
    headingLabel1.place(relwidth=1, relheight=1)

    mainFrame = Frame(root, bg='black')
    mainFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(mainFrame, text = "%-15s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'),
          bg = 'black', fg = 'white').place(relx = 0.07, rely = 0.1)

    Label(mainFrame, text = "----------------------------------------------------------------------------",
          bg = 'black', fg = 'white').place(relx = 0.06, rely = 0.2)



    try:
        conn = sqlite3.connect('libary_books.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM books")
        conn.commit()

        for i in cur:
            Label(mainFrame, text = "%-15s%-40s%-30s%-20s"% (i[0], i[1], i[2], i[3]),
                  bg = 'black', fg = 'white').place(relx = 0.07, rely = y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")


    quitBtn = Button(root, text="Quit", bg='black', fg='white', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)

    root.mainloop()


from tkinter import *
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('libary_books.db')

cur = conn.cursor()

bookTable = "books"
issueTable = "book_issued"

allbid = []

def issue():

    global status, check

    bid = issueBook1.get()
    issueto = issueBook2.get()

    try:
        cur.execute("SELECT bid FROM "+bookTable)
        conn.commit()
        for id in cur:
            allbid.append(id[0])

        id = int(bid)
        if id in allbid:
            cur.execute("SELECT status FROM  "+bookTable+" where bid = "+bid)
            conn.commit()
            for i in cur:
                check = i[0]
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showerror("Error", "Book ID not present")

    except:
        messagebox.showerror("Error", "Can't fetch Book IDs")

    try:
        issue_id = int(bid)
        if issue_id in allbid and status == True:
                cur.execute("INSERT OR IGNORE INTO  " + issueTable + " VALUES (:bid, :issueto)",
                        {
                            'bid': bid,
                            'issueto': issueto
                        }
                        )
                conn.commit()
                cur.execute("UPDATE " + bookTable + " set status = 'issued' where bid = "+bid)
                conn.commit()
                messagebox.showinfo('Success', "Book Issued Successfully")
                root.destroy()

        else:
                allbid.clear()
                messagebox.showinfo('Message', "Book Already Issued")
                root.destroy()
                return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")


    allbid.clear()


def issue_books():

    global issueBook1, issueBook2, issueBtn, quitBtn, root, mainFrame, lb1

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
    Canvas1.config(bg="#c36d7e")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    Label(headingFrame1, text="Issue Book", font=('Courier', 15, "bold"),
          bg='black', fg='white').place(relwidth=1, relheight=1)

    mainFrame = Frame(root, bg='black')
    mainFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(mainFrame, text="Book Id : ", font=('Courier', 12, "bold"), bg='black', fg='white')
    lb1.place(relx=0.07, rely=0.30)

    issueBook1 = Entry(mainFrame, font=('Courier'))
    issueBook1.place(relx=0.32, rely=0.30, relwidth=0.6, relheight=0.08)

    lb2 = Label(mainFrame, text="Issue To : ", font=('Courier', 12, "bold"), bg='black', fg='white')
    lb2.place(relx=0.07, rely=0.6)

    issueBook2 = Entry(mainFrame, font=('Courier'))
    issueBook2.place(relx=0.32, rely=0.6, relwidth=0.6, relheight=0.08)

    issueBtn = Button(root, text="Issue", bg="black", fg="white", font=('Courier', 10), command=issue)
    issueBtn.place(relx=0.25, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="black", fg="white", font=('Courier', 10), command=root.destroy)
    quitBtn.place(relx=0.55, rely=0.85, relwidth=0.18, relheight=0.08)


    root.mainloop()


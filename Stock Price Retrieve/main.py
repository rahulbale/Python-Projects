
from get_stock import *
from tkinter import *
from tkinter import messagebox


# urls= Indian Tech ['tata-motors-ltd', 'tech-mahindra', 'infosys', 'bajaj-auto']
# urls=  ['tesla-motors', 'apple-computer-inc', 'facebook-inc']

def callfun():
    try:
        stockname_ = stockname.get()    #Stock Company name
        filename_ = filename.get()
        count_ = valuecount.get()       #Past days count
        get_stock(stockname_, filename_, count_, txt)

    except:
        messagebox.showerror("Error", "Invalid Stock Name")
        root.destroy()
        gui()
        return

        


def adject(window):
    w = 600         # Width of the window size
    h = 600         # Height of the window size
    ws = window.winfo_screenwidth()         # Width of the screen
    hs = window.winfo_screenheight()        # Height of the screen
    x = (ws / 2) - (w / 2)                  # Calculate x and y coordinates for the Tk window
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))   # Set the dimensions of the screen and where it is placed

    window.resizable(width=False, height=False)     # Disable the resize option of window



def gui():     #Gui for the Project

    global stockname, filename, valuecount,root,txt

    root = Tk()
    root.title('Stock Retrieve')
    adject(root)

    headingFrame = Frame(root, bg = "#00cc00", bd = 12)
    headingFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
    headingLable = Label(headingFrame, text="Stock Retriever", font=('Courier', 25, "bold"), bg='black',
                          fg='white')
    headingLable.place(relwidth=1, relheight=1)


    mainFrame = Frame(root, bg = "black")
    mainFrame.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.4)


    lb1 = Label(mainFrame, text = "Stock Name : ", bg="black", fg="white", font=('Courier', 13, "bold"))
    lb1.place(relx=0.05, rely=0.1, relheight=0.1)

    stockname = Entry(mainFrame, font=('Courier', 13, "bold"))
    stockname.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.09)

    lb2 = Label(mainFrame, text="File Name : ", bg="black", fg="white", font=('Courier', 13, "bold"))
    lb2.place(relx=0.05, rely=0.3, relheight=0.1)

    filename = Entry(mainFrame, font=('Courier', 13, "bold"))
    filename.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.09)

    lb3 = Label(mainFrame, text="Total Days :", bg="black", fg="white", font=('Courier', 13, "bold"))
    lb3.place(relx=0.05, rely=0.5, relheight=0.1)

    valuecount = Entry(mainFrame, font=('Courier', 13, "bold"))
    valuecount.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.09)

    btn = Button(mainFrame, text='Fetch', font=('Courier', 12), command = callfun)
    btn.place(relx=0.5, rely=0.7, relwidth=0.25, relheight=0.15)

    bottomFrame = Frame(root, bg="black", bd=5)
    bottomFrame.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.20)
    txt = Text(root, width=50, height=4, wrap=WORD, font=('Courier', 12, "bold"))
    txt.place(relx=0.08, rely=0.78)

    root.mainloop()


gui()



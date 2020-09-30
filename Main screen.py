from tkinter import *
from tkinter import filedialog
from ledger import *
from PIL import ImageTk, Image
import datetime
import tkinter.font as tkfont

# def callback():
#   print ("called the callback!")

# def manage_billspay():
#    print ("")

# def input_expense():
#   print ("")

# def modify_expenses():
#   print ("")


# def input_income():
#   print ("")

def greenRed(amount):
    # add gradient for amount over 0 later
    redGreen = int(amount) > 0

    if redGreen:
        greenRed = "green3"
    else:
        greenRed = "red2"
    return greenRed

def Test_Module():
    print("test")

# get ledger file from user input

mainLedger = Account()

def open_Ledger():
    root.filename =\
        filedialog.askopenfilename(initialdir = r"C:\Users\Brandon\PycharmProjects\DesktopBudget\venv\Lib\site-packages"\
         , title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
# open ledger file and load ledger


root = Tk()
root.title ("Lightweight Desktop Budge Tool")

# displays the title image
path = (r"C:\Users\Brandon\PycharmProjects\DesktopBudget\venv\Lib\site-packages\desktop budget tool logo finished.png")
img = ImageTk.PhotoImage(Image.open(path))
titleFrame = Label(root, image=img)

# displays the summary frame
summaryBckd = greenRed(str(mainLedger.total_amount))
budgetSummaryFrame = Label(root, background=summaryBckd, borderwidth=5)

remainingBalance = Label(budgetSummaryFrame \
                         , text="Remaining Balance: " + str(mainLedger.total_amount) \
                         , bg=greenRed(mainLedger.total_amount)
                         , font=tkfont.Font(family="Helvetiva", size=18, weight="bold", slant="roman"))

#displays the ledger modification frame

ledgerMod = Frame(root, bd = 2, relief = RAISED, borderwidth = 2, padx = 3, pady = 3)

loadLedger = Button(ledgerMod, text = "load account", bd = 1, command = lambda: open_Ledger())
testButtong = Button(ledgerMod, text = "test button", command = Test_Module())


# displays the top of the ledger in a labelframe
# upcoming periodic expenses
upcomingExpenses = LabelFrame(root, text="Upcoming Expenses", bd = 5)
#periodic eentries must be ordered by date - once def is finished. until then, placeholders will be used.



upcomingGrid = [[]]



# insert label(grid) here?
# grid pulls the next five periodic expenses
periodicEntriesHead = []
n = 5
def generate_Upcoming_expenses():

    for entry in mainLedger.periodicEntries:
        if entry["date"].day > datetime.now().day:
            periodicEntriesHead.update(entry)
    # index entries in periodicEntriesHead to display in order of date.
    for entry in periodicEntriesHead:
        if (i > 0):
            label(upcomingExpenses, text=entry["name"]).grid(row=0, sticky=W)
            label(upcomingExpenses, text=entry["amount"]).grid(row=0, column=1)
            label(upcomingExpenses, text=entry["date"]).grid(row=0, column=2)
            i = i - 1

# displays the most recent expense items
# most recent expenses


#Geometry arrangement

titleFrame.grid(row=0, column=0)
budgetSummaryFrame.grid(row=1, column=0)
remainingBalance.grid(row = 1, column = 0)
ledgerMod.grid(row = 0, column = 1)
upcomingExpenses.grid(row=1, column=1)
for i in range (4):
    upcomingGrid.append(Label(upcomingExpenses, text = "name/label").grid(row = i, column = 0))
    upcomingGrid.append(Label(upcomingExpenses, text = "date").grid(row = i, column = 1))
    upcomingGrid.append(Label(upcomingExpenses, text = "to be taken from data").grid(row = i, column = 2))
    upcomingGrid.append(Label(upcomingExpenses, text = "remaining amount in account").grid(row = i, column = 3))


root.mainloop()

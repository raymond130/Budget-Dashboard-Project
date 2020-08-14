from tkinter import *
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


# get ledger file from user input
# open ledger file and load ledger

mainLedger = Account()

print (mainLedger.total_amount)
root = Tk()

# displays the title image
path = (r"C:\Users\Brandon\PycharmProjects\DesktopBudget\venv\Lib\site-packages\desktop budget tool logo finished.png")
img = ImageTk.PhotoImage(Image.open(path))
titleFrame = Label(root, image=img).grid(row=0, column=0)

# displays the summary frame
summaryBckd = greenRed(str(mainLedger.total_amount))
budgetSummaryFrame = Frame(root, background=summaryBckd, borderwidth=1).grid(row=1, column=0)

remainingBalance = Label(budgetSummaryFrame \
                         , text="Remaining free cash = " + str(mainLedger.total_amount) \
                         , bg=greenRed(mainLedger.total_amount)
                         , font=tkfont.Font(family="Helvetiva", size=36, weight="normal", slant="roman"))

# displays the top of the ledger in a labelframe
# upcoming periodic expenses
upcomingExpenses = LabelFrame(root, text="Upcoming Expenses").grid(row=2, column=0)
# insert label(grid) here?
# grid pulls the next five periodic expenses
periodicEntriesHead = head()
n = 5
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


root.mainloop()

from tkinter import *

# This has to go first because this creates a window
root = Tk()

# Functions
def calc():
    try:
        step1 = int(entryb.get()) / 100 * 10
        step2 = int(entryc.get()) + 40 
        step3 = int(entryd.get()) + 88
        step4 = round((step1 + step2 + step3) / 3)
        last = Label(root, text='Your score is: ' + str(step4)).grid(row=6, column=0)
    except ValueError:
        last = Label(root, text='Please enter valid numbers.').grid(row=6, column=0)

# Creating a label and positioning them
mylabela = Label(root, text='Apple Fitness Rings Calculator', fg='black', bg='yellow').grid(row=0, column=0)
mylabelb = Label(root, text='How many calories did you burn: ').grid(row=1, column=0)
mylabelc = Label(root, text='How many minutes were you active: ').grid(row=2, column=0)
mylabeld = Label(root, text='How many stand minutes did you collect: ').grid(row=3, column=0)

# Creating entry widgets
entryb = Entry(root, width=5)
entryb.grid(row=1, column=1)

entryc = Entry(root, width=5)
entryc.grid(row=2, column=1)

entryd = Entry(root, width=5)
entryd.grid(row=3, column=1)

# Creating a button widget
button1 = Button(root, text='Calculate', command=calc).grid(row=4, column=0)
button2 = Button(root, text='Reset').grid(row=5, column=0)

# Creating an event loop
root.mainloop()

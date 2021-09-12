# tkinter -standard Python interface to the Tk GUI(Graphical User Interface) toolkit 
# strftime() function is used to convert date and time objects to their string representation
# Install the fonts attached for the better UI (ds-digital.zip)

from tkinter import *
from tkinter.ttk import *
from time import strftime

# The below is for the UI / (title = Clock)
root = Tk()
root.title("CLock")


def time():
    time_string = strftime('%H:%M:%S %p') # Time format
    lable.config(text=time_string) # To set time to the lable
    lable.after(1000, time) # To call time function ever sec

lable = Label(root, font=("ds-digital",80), background="black", foreground="cyan") # 80 -> Font size
lable.pack(anchor='center')


time()

mainloop()
# tkinter -standard Python interface to the Tk GUI(Graphical User Interface) toolkit 
import tkinter as tk
from tkinter import*
from tkinter.ttk import*
running = False
#defining global variable 
hours, minutes, seconds = 0, 0, 0

# on start button click
def start():
    global running
    if not running:
        update()
        running = True

# on pause button click
def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

# on reset button click
def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text='00:00:00')

def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    stopwatch_label.config(text = hours_string + ':' + minutes_string + ':' + seconds_string)
    global update_time
    update_time = stopwatch_label.after(1000, update) # updates every sec (ie. 1000 milisec)

root = tk.Tk()
root.title("stopwatch") # window title
root.geometry("520x200") # size of the window
root.resizable(False,False) # cant minimize or maximize the window
root.configure(bg="black") # window background color will be black
stopwatch_label = tk.Label(text='00:00:00',font=('ds-digital',90,'bold'),fg = 'red' ,background='black')
stopwatch_label.pack()

style=Style()

style.configure("TButton",font=('arial',10,'bold'), borderwidth='5')
startBtn=Button(root,text="Start",command=start).place(x=126,y=150) # start button in position 170:10 ( ie. padding left, padding top)
stopBth=Button(root,text="Stop",command=pause).place(x=212,y=150) # stop button in position 280:10
stopBth=Button(root,text="Reset",command=reset).place(x=298,y=150) # stop button in position 280:10
# command will run start/pause/reset function 

root.mainloop()
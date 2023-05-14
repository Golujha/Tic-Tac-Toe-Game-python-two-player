from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Tic Tac TOE by GOLU JHA")

click = True
def checker(buttons):
    global click
    if buttons["text"] == " " and click:
        buttons["text"] = "x"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "o"
        click = True
    if(
        button_1["text"] == "x" and button_2["text"] == "x" and button_3["text"] == "x" or
        button_1["text"] == "x" and button_4["text"] == "x" and button_7["text"] == "x" or
        button_1["text"] == "x" and button_5["text"] == "x" and button_9["text"] == "x" or
        button_2["text"] == "x" and button_5["text"] == "x" and button_8["text"] == "x" or
        button_3["text"] == "x" and button_6["text"] == "x" and button_9["text"] == "x" or
        button_4["text"] == "x" and button_5["text"] == "x" and button_6["text"] == "x" or
        button_7["text"] == "x" and button_8["text"] == "x" and button_9["text"] == "x" or
        button_3["text"] == "x" and button_5["text"] == "x" and button_7["text"] == "x"
    ):
        tkinter.messagebox.showinfo("Winner x","Woow player X is the winner")
    elif(
        button_1["text"] == "o" and button_4["text"] == "o" and button_7["text"] == "o" or
        button_1["text"] == "o" and button_5["text"] == "o" and button_9["text"] == "o" or
        button_1["text"] == "o" and button_2["text"] == "o" and button_3["text"] == "o" or
        button_2["text"] == "o" and button_5["text"] == "o" and button_8["text"] == "o" or
        button_3["text"] == "o" and button_6["text"] == "o" and button_9["text"] == "o" or
        button_4["text"] == "o" and button_5["text"] == "o" and button_6["text"] == "o" or
        button_7["text"] == "o" and button_8["text"] == "o" and button_9["text"] == "o" or
        button_3["text"] == "o" and button_5["text"] == "o" and button_7["text"] == "o"
    ):
        tkinter.messagebox.showinfo("Winner o,","Woow player O is the winner")

buttons = StringVar()

button_1 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_1),bd=10)
button_1.grid(row=1,column=0, sticky=S+W+N+E)
button_2 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_2),bd=10)
button_2.grid(row=1,column=1, sticky=S+W+N+E)
button_3 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_3),bd=10)
button_3.grid(row=1,column=2, sticky=S+W+N+E)

button_4 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_4),bd=10)
button_4.grid(row=2,column=0, sticky=S+W+N+E)
button_5 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_5),bd=10)
button_5.grid(row=2,column=1, sticky=S+W+N+E)
button_6 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_6),bd=10)
button_6.grid(row=2,column=2, sticky=S+W+N+E)

button_7 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_7),bd=10)
button_7.grid(row=3,column=0, sticky=S+W+N+E)
button_8 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_8),bd=10)
button_8.grid(row=3,column=1, sticky=S+W+N+E)
button_9 = Button(root,text=" ",font=("Arial 30"),height=2, width=4, command=lambda:checker(button_9),bd=10)
button_9.grid(row=3,column=2, sticky=S+W+N+E)

mainloop()
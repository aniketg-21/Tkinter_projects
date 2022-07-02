from tkinter import *
import math


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = 'Error'
        scValue.set(value)
    elif text == "AC":
        scValue.set("")
    elif text == "←":
        try:
            d = scValue.get()
            d = d.replace(d[len(d)-1], "")
            scValue.set(d)
        except Exception as e:
            pass
    else:
        scValue.set(scValue.get() + text)
    screen.update()


root = Tk()
root.geometry("300x380")
root.resizable(0, 0)
root.title("My Calculator")

scValue = StringVar()
scValue.set("")
screen = Entry(root, textvar=scValue, font="TimesNewRoman 18")
screen.grid(ipadx=8, pady=10, padx=10)

f = Frame(root, bg="#FAEBD7", padx=8, pady=8)
myButtons = ['(', ')', '/', 'AC', '←', 'x²', 7, 8, 9, '*', 'x³', 4, 5, 6, '+', '√', 1, 2, 3, '-', '%', '.', 0, '=']
c = -1
r = 2
for i in range(len(myButtons)):
    b = Button(f, fg="red", bg="FloralWhite", height=1, width=2, text=f"{myButtons[i]}", font="Ariel 18")
    if (i % 5 == 0 and i != 0):
        r += 1
        c = 0
    else:
        c += 1
    if (myButtons[i] == '='):
        b.grid(row=r, column=c, columnspan=2, ipadx=30, padx=8, pady=8)
    else:
        b.grid(row=r, column=c, padx=6, pady=6)
    b.bind("<Button-1>", click)

f.grid()

root.mainloop()

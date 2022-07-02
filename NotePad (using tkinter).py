from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - My Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - My Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - My Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Aniket")


if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - My Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("400x500")

    # Add TextArea
    TextArea = Text(root, font="TimesNewRoman 18")
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    # Lets create a menubar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)
    # To open already existing file
    FileMenu.add_command(label="Open", command=openFile)
    # To save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_command(label="Save As", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quit)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    # Adding ScrollBar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()

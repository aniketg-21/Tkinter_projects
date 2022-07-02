import tkinter as tk, threading
from tkinter.messagebox import showinfo
import imageio
from PIL import Image, ImageTk
import time
from tkinter import colorchooser
import pygame


class MyGame:
    def __init__(self, root):
        pygame.init()
        self.master = root
        self.master.title("Tic-Tac-Toe")
        self.master.geometry("289x410")
        self.master.resizable(0, 0)
        self.master.wm_iconbitmap("myLogo.ico")
        self.master.configure(bg="chartreuse")
        self.values = []
        self.board = []
        self.fill = ""
        self.player_val = ""
        self.Music = [pygame.mixer.Sound('D:\\Programs\\JavaScript Programs\\Tic-Tac-Toe\\click.wav'),
                      pygame.mixer.Sound('D:\\Programs\\JavaScript Programs\\Tic-Tac-Toe\\Lets_Go-David_Renda.mp3')]

    def myMenu(self):
        MenuBar = tk.Menu(self.master)
        GameMenu = tk.Menu(MenuBar, tearoff=0)
        GameMenu.add_command(label="New Game", command=self.restart)
        ColorMenu = tk.Menu(GameMenu, tearoff=0)
        GameMenu.add_cascade(label="Change color", menu=ColorMenu)
        ColorMenu.add_command(label="Board", command=self.change_color_board)
        ColorMenu.add_command(label="Background", command=self.change_color_background)
        GameMenu.add_separator()
        GameMenu.add_command(label="Exit", command=quit)
        MenuBar.add_cascade(label="Game", menu=GameMenu)
        HelpMenu = tk.Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="help", command=self.help)
        HelpMenu.add_command(label="About", command=self.about)
        MenuBar.add_cascade(label="Help", menu=HelpMenu)
        self.master.config(menu=MenuBar)

    def change_color_board(self):
        res = colorchooser.askcolor()
        for i in range(9):
            self.board[i].configure(bg=res[1], activebackground=res[1])

    def change_color_background(self):
        res = colorchooser.askcolor()
        self.master.configure(bg=res[1])
        self.master.winfo_children()[1].configure(bg=res[1])
        self.master.winfo_children()[2].configure(bg=res[1])
        self.values[2].configure(bg=res[1])

    def help(self):
        showinfo("help", "Click on 'X' or 'O' to get started")

    def about(self):
        about_window = tk.Toplevel()
        about_window.wm_iconbitmap("myLogo.ico")
        about_window.title("About")
        about_window.geometry("400x400")
        tk.Label(about_window, text="Tic-Tac-Toe", font="Lucida 32 bold").pack(pady=8)
        img = ImageTk.PhotoImage(Image.open("about.png"))
        label = tk.Label(about_window, image=img)
        label.pack()
        about_window.mainloop()

    def game_board(self):
        self.myMenu()
        f1 = tk.Frame(self.master, width=300, height=300, background='chartreuse')
        self.my_Buttons(f1)
        f1.grid(row=0, column=0, padx=6, pady=6)

        f2 = tk.Frame(self.master, background='chartreuse')
        self.values.append(
            tk.Button(f2, text="X", font="Lucida 21 bold", activebackground="purple", bg="medium purple"))
        self.values[0].bind("<Button-1>", self.click) and self.values[0].grid(row=0, column=0, ipadx=45)
        self.values.append(
            tk.Button(f2, text="O", font="Lucida 21 bold", activebackground="purple", bg="medium purple"))
        self.values[1].bind("<Button-1>", self.click) and self.values[1].grid(row=0, column=1, ipadx=45)
        self.values.append(tk.Label(f2, text="Select One ↑", font="System 18 bold", bg="chartreuse"))
        self.values[2].grid(row=1, column=0, columnspan=2)
        f2.grid(row=1, column=0, padx=4)
        self.Music[1].play(-1)

    def my_Buttons(self, f2):
        btn_no = -1
        for i in range(3):
            for j in range(3):
                btn_no += 1
                self.board.append(tk.Button(f2, text=" ", width=3, height=1, font="Lucida 32 bold", bg='skyblue',
                                            activebackground="skyblue", command=lambda x=btn_no + 1: self.fillMe(x)))
                self.board[btn_no].grid(row=i, column=j, padx=2, pady=2)

    def click(self, event):
        self.Music[0].play()
        text = event.widget.cget("text")
        if text == "X":
            self.fill = "X"
            self.values[0].configure(bg="purple", state="normal")
            self.values[1].configure(bg="medium purple", state="disable")
        else:
            self.fill = "O"
            self.values[1].configure(bg="purple", state="normal")
            self.values[0].configure(bg="medium purple", state="disable")
        self.values[2].configure(text=self.fill + "'s Turn...")

    def fillMe(self, x):
        self.Music[0].play()
        if self.fill == "": return
        value = ""
        if self.isEmpty(x):
            self.board[x - 1].configure(text=self.fill)
            if self.isFull():
                self.get_Results(value)
            if self.pattern_Check():
                self.get_Results(value)
            if self.fill == "X":
                self.fill = "O"
            else:
                self.fill = "X"
            self.values[2].configure(text=self.fill + "'s Turn...")
        if self.pattern_Check():
            self.get_Results(value)

    def get_Results(self, value):
        for i in range(9):
            self.board[i]["state"] = "disable"
        if (self.fill == self.pattern_Check()) or (self.player_val == self.pattern_Check()):
            self.display_results(f"Player: {self.pattern_Check()} Win's", "win.gif")
        elif value == self.pattern_Check():
            self.display_results(f"Better Luck Next\nTime: 'CPU' wins", "lose.jpg")
        else:
            self.display_results("It's a Tie!!!", "tie.gif")

    def isFull(self):
        for i in range(9):
            if self.board[i].cget("text") == " ":
                return 0
        return 1

    def isEmpty(self, x):
        if self.board[x - 1].cget("text") == " ":
            return 1
        return 0

    def pattern_Check(self):
        win_values = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for c in self.values:
            for i in win_values:
                if (self.board[i[0]].cget("text") == self.board[i[1]].cget("text") == self.board[i[2]].cget("text") == f'{c.cget("text")}'):
                    return 1 and c.cget("text")

    def display_results(self, value, img):
        new_window = tk.Toplevel()
        new_window.wm_iconbitmap("myLogo.ico")
        new_window.geometry("300x390")
        new_window.resizable(0, 0)
        tk.Label(new_window, text=f'{value}', bg="chartreuse", font="System 22 bold").pack(fill=tk.X)
        b = tk.Button(new_window, text="Play again⇆", font="System 18 bold italic", bg="chartreuse", bd=0,
                      command=lambda w=new_window: self.play_again(w))
        b.pack(fill=tk.X, side=tk.BOTTOM)
        f = tk.Frame(new_window, padx=8, pady=8)
        myLabel = tk.Label(f)
        myLabel.pack()
        f.pack()

        self.play_video(img, myLabel)
        new_window.mainloop()

    def play_video(self, img, myLabel):
        video = imageio.get_reader(img)

        def stream(myLabel):
            for image in video.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                myLabel.configure(image=frame_image)
                myLabel.image = frame_image
                time.sleep(0.1)

        thread = threading.Thread(target=stream, args=(myLabel,))
        thread.daemon = 1
        thread.start()

    def play_again(self, w):
        w.destroy()
        self.restart()

    def restart(self):
        self.fill = ""
        for i in range(9):
            self.board[i].configure(text=" ", activebackground=self.board[i].cget("bg"), state="normal")
        self.values[0].configure(bg="medium purple", state="normal")
        self.values[1].configure(bg="medium purple", state="normal")
        self.values[2].configure(text="Select One ↑")


def main():
    root = tk.Tk()
    play = MyGame(root)
    play.game_board()
    root.mainloop()


if __name__ == '__main__':
    main()

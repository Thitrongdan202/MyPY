from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.lable = Label(master=self, text="Nhập")
        self.chieu_cao = Entry(master=self)
        self.button = Button(master=self, text="Click")
        self.geometry("350x150")

        self.lable.place(x=10, y=20)
        self.chieu_cao.place(x=60, y=20)

    def show(self):
        mainloop()

if __name__== '__main__':
    f = GUI()
    f.show()
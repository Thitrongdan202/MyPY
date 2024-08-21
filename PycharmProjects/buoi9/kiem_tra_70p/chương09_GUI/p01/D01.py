from tkinter import *
def button_clicked(even):
    print("Button clicked!")

def button_clicked2():
    print("Button clicked!")

gui = Tk()
gui.title("Demo gui")
gui.geometry("300x500")



bt = Button(master=gui, text="Nhấn", bg='red', command=button_clicked2)
bt.place(x= 20, y =50)
#bt.bind("<Button-1>", button_clicked)


gui.mainloop()


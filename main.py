from tkinter import *

window = Tk()
window.title("Spl folder")
window.geometry("300x300")

greeting = Label(text="Hello user",fg="black",bg="white")
btn = Button(text="click",fg="black",bg="white")
entry = Entry(fg="black",bg="white",width=50)
greeting.pack()
btn.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
l2 = Label(text="sample text",fg="black",bg="white")
l2.pack()
text = Text(fg="purple",bg="white")
text.pack()

window.mainloop()
from tkinter import*

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


e.insert(0, "Enter your Name: ")


def myclick():
    hello = "Hello" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


mybutton = Button(root, text="Enter your stock quote", command=myclick)


root.mainloop()

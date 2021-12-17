from tkinter import *

# TKinter module was converted from another language and the way the methods are implemented
# was the most efficient way to do so. 

def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{input.get()}")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#Update properties of a component we created
my_label.config(text="New Text")
# my_label.pack() # place component into window at center of screen from top to bottom
# my_label.place(x=100, y=200) # place widget at precise coordinate
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry (Input)
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)


 

window.mainloop()
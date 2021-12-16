from tkinter import *

# TKinter module was converted from another language and the way the methods are implemented
# was the most efficient way to do so. 

def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{input.get()}")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#Update properties of a component we created
my_label.config(text="New Text")
my_label.pack() # place component into window at center of screen


#Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry (Input)

input = Entry(width=10)
print(input.get())
input.pack()




window.mainloop()
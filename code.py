import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Python rocks!",
    foreground = "white",
    background = "black",
    width=10,
    height=10
    )
label.pack()

button = tk.Button(
    text = "Click me!",
    width = 25,
    height =5,
    bg ="blue",
    fg ="yellow",
    )

window.mainloop()

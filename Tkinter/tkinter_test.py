def my_first_gui():
    import tkinter as Tk

    # make root window (one per program)
    root = Tk.Tk()

    # make a label widget as a child to the root window
    # label can display either text or icon or image

    hello_widget = Tk.Label(root, text="Hello, world!")

    # pack method sizes widget and makes visible
    hello_widget.pack()

    # must enter main loop for window to appear
    root.mainloop()




if __name__ == "__main__":
    print("Hi")
    my_first_gui()
    pass

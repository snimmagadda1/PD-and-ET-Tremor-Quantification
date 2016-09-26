if __name__ == "__main__":
    from tkinter import *

    root = Tk()

    # tracks character pressed
    def key(event):
        print("pressed", repr(event.char))

    # Button one is left mouse button
    def callback(event):
        frame.focus_set()
        print("clicked at", event.x, event.y)

    # initialize frame widget (parent window)
    frame = Frame(root, width=100, height=100)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    frame.pack()

    root.mainloop()




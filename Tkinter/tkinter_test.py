if __name__ == "__main__":

    from tkinter import *


    class App:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()

            # make two button objects belonging to App

            # associate two functions with buttons
            self.hi_there = Button(frame, text="Hello", command=self.say_hi)
            self.hi_there.pack(side=LEFT)

            self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
            self.button.pack(side=LEFT)

            # define function
        def say_hi(self):
            print("Hello Friends")


    root = Tk()

    app = App(root)

    root.mainloop()
    root.destroy()  # optional; see description below
    pass

if __name__ == "__main__":
    from tkinter import *


    def callback():
        print("called the callback!")


    root = Tk()

    # create a menu
    menu = Menu(root)

    # add to root master
    root.config(menu=menu)

    # make the file entry in menu
    filemenu = Menu(menu)

    # make filemenu a cascade menu
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=callback)
    filemenu.add_command(label="Open...", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    # make the help entry in menu
    helpmenu = Menu(menu)

    # make help menu a cascade menu
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=callback)

    root.mainloop()
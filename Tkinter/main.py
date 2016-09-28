import tkinter as tk


# Class to make HelpMenu for a window
class HelpMenu:
    counter = 0

    def __init__(self, master):
        # make the menu, add to root
        menu = tk.Menu(master)
        master.config(menu=menu)

        file_menu = tk.Menu(menu)

        # function to execute options
        def callback():
            print("Execute Options")

        # function to print information about program
        def print_about():
            print("Print Licensing Info")

        # make filemenu a cascade menu
        menu.add_cascade(label="Options", menu=file_menu)
        file_menu.add_command(label="Preferences", command=callback)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # make the help entry in menu
        help_menu = tk.Menu(menu)

        # make help menu a cascade menu
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=print_about)


# Class to make main window
class MainWindow(tk.Tk):

    # initialize the main window
    def __init__(self, master):

        # set title of frame
        master.title("Park & Sons Co: Essen+ial Tremometer\u2122 Diagnostic Tool")

        # configure main window root to frame
        self.master = master
        self.frame = tk.Frame(self.master, width=768, height=576, bg=None, colormap="new")

        # how much to pad by (almost entire screen used)
        pad = 3

        # set geometry of window to be full screen
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))

        self.frame.pack()



if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()

    main = MainWindow(root)
    main_menu = HelpMenu(root)

    # start the GUI loop
    root.mainloop()
    #root.destroy()




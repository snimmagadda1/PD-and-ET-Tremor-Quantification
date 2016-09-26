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
class MainWindow:

    # function to change window size
    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)

        # resize window according to stored value
        self.master.geometry(self._geom)

        # store previous size in _geom variable for continuous reverts
        self._geom = geom

    # initialize the main window
    def __init__(self, master):

        # set title of frame
        master.title("Park & Sons Co: Essen+ial Tremometer\u2122 Diagnostic Tool")

        # configure main window root to frame
        self.master = master
        self.frame = tk.Frame(self.master, width=768, height=576, bg="", colormap="new")

        # how much to pad by (almost entire screen used)
        pad = 3

        # define resize shape
        self._geom = '800x800+0+0'

        # set geometry of window to be full screen
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))

        # bind the escape key to window resize event
        master.bind('<Escape>', self.toggle_geom)
        self.frame.pack()



if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    main = MainWindow(root)
    main_menu = HelpMenu(root)
    root.mainloop()
   # root.destroy()




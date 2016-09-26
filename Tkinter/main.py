# Class to make HelpMenu for a window
class HelpMenu:

    def __init__(self, master):
        # make the menu, add to root
        menu = tk.Menu(master)
        master.config(menu=menu)

        file_menu = tk.Menu(menu)

        def callback():
            print("Clicked!")

        def create_window():
            print("HI")


        # make filemenu a cascade menu
        menu.add_cascade(label="Go To", menu=file_menu)
        file_menu.add_command(label="Tremor Overview", command=callback)
        file_menu.add_command(label="Statistics", command=callback)
        file_menu.add_command(label="Graphs", command=callback)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # make the help entry in menu
        help_menu = tk.Menu(menu)

        # make help menu a cascade menu
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=callback)


# Class to make main window
class MainWindow:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)


if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    main = MainWindow(root)
    main_menu = HelpMenu(root)
    root.mainloop()
    pass



import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot
from matplotlib import style

import Tkinter as tk

import urllib
import json

import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None

from matplotlib import pyplot as plt
TITLE_FONT = ("Verdana", 24)
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

style.use("ggplot")

f = Figure()
a = f.add_subplot(111)

# global constants (default values)


def popupmsg(msg):
    """
    Make a popup window for a message
    :param msg: input message to display (string)
    :return:
    """
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def animate(i):
    """
    Function to draw graphics
    :param i:
    :return:
    """



# Main app class
class TremorApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Park & Sons Co: Essen+ial Tremometer\u2122 Diagnostic Tool")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

# ******************************************** MENU STUFF ************************************************************ #

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Export", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        setting1 = tk.Menu(menubar, tearoff=1)
        setting1.add_command(label="Start Page", command=lambda: self.show_frame(start_page))
        setting1.add_command(label="Graph Page", command=lambda: self.show_frame(graph_page))
        setting1.add_command(label="Patient Page", command=lambda: self.show_frame(updrs_page))
        menubar.add_cascade(label="Navigation", menu=setting1)

        setting2 = tk.Menu(menubar, tearoff=1)
        setting2.add_command(label="A", command=lambda: popupmsg("Not supported just yet!"))
        setting2.add_command(label="B", command=lambda: popupmsg("Not supported just yet!"))
        setting2.add_command(label="C", command=lambda: popupmsg("Not supported just yet!"))
        setting2.add_command(label="D", command=lambda: popupmsg("Not supported just yet!"))
        menubar.add_cascade(label="Display", menu=setting2)

        setting3 = tk.Menu(menubar, tearoff=1)
        setting3.add_command(label="A", command=lambda: popupmsg("Not supported just yet!"))
        setting3.add_command(label="B", command=lambda: popupmsg("Not supported just yet!"))
        menubar.add_cascade(label="Help", menu=setting3)

        tk.Tk.config(self, menu=menubar)

# ******************************************** MENU STUFF ************************************************************ #

        self.frames = {}
        # this is where new pages are added if needed
        for F in (start_page, graph_page,  updrs_page):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start_page)

    def show_frame(self, cont):
        """
        Function to show an new window
        :param cont: the frame to show
        :return:
        """
        frame = self.frames[cont]
        frame.tkraise()


class start_page(tk.Frame):

    def _login_button_clicked(self, controller):
        """Check credentials against login

        :return: NA
        """
        username = self.enter_name.get()
        password = self.enter_pwd.get()

        if username == "essential" and password == "tremor":
            print("YAY")
            controller.show_frame(graph_page)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""ALPHA Diagnostic Tool. For use with the Essential Tremometer\u2122
        accelerometer based tremor classification platform."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # User name and login
        name_label = tk.Label(self, text="Username")
        name_label.pack(side='top')

        self.enter_name = tk.Entry(self, justify='center')
        self.enter_name.insert(0, "...")
        self.enter_name.pack(side='top')
        username = self.enter_name.get()

        pwd_label = tk.Label(self, text="Password")
        pwd_label.pack(side='top')

        self.enter_pwd = tk.Entry(self, justify='center')
        self.enter_pwd.insert(0, "...")
        self.enter_pwd.pack(side='top')
        password = self.enter_pwd.get()

        login_button = tk.Button(self, text="Login", command=lambda: self._login_button_clicked(controller))
        login_button.pack()

        # background image
        background_pic = tk.PhotoImage(file="background_image.gif")
        panel = tk.Label(self, image=background_pic)
        panel.pack(side='top', fill='both', expand='yes')
        panel.image = background_pic



class graph_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



class updrs_page(tk.Frame):


    def __init__(self, parent, controller):

        def do_bluetooth():
            print("hi")

        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="Unified Parkinsons Disease Rating Scale", font=TITLE_FONT)
        #title.place(relx=0.5, rely=0.5, anchor='center')
        title.pack(side = 'top')

        # self.grid_columnconfigure(0, weight=1)

        name_label = tk.Label(self, text="Enter Patient Name", bg='gainsboro')
        name_label.pack(side='top')

        enter_name = tk.Entry(self, justify='center')
        enter_name.insert(0, "...")
        enter_name.pack(side='top')

        list_label = tk.Label(self, text="1. Intellectual Impairment", bg='red')
        list_label.pack(side='top')

        listbox = tk.Listbox(self)
        listbox.config(width=0)
        listbox.pack(side='top')

        for item in ["0 = None.", "1 = Mild.", "2 = Moderate memory loss", "3 = Severe memory loss",
                     "4 = Severe Memory Loss. Unable to make judgements"]:
            listbox.insert('end', item)

        bluetooth_butt = tk.Button(self, text="Bluetooth", command=do_bluetooth)
        bluetooth_butt.pack()


#################################### PROGRAM RUN #######################################################################
app = TremorApp()
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()
# for plotting and GUI
import matplotlib
import tkinter as tk
# allow to draw matploblib to canvas using TkAgg and zoom toolbar stuff
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
# for live graphs
import matplotlib.animation as animation
# for reading data from url
import urllib
import json
# for data manipulation
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

# define backend for graphics
matplotlib.use("TkAgg")

# define constants and styles
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")

# figure is global variable
f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)

# starting dataset is global variable
exchange = "BTC-e"
DatCounter = 9000
programName= "btce"


def changeExchange(toWhat, pn):
    """
    Change the exchange type that is displayed
    :param toWhat:
    :param pn:
    :return:
    """
    global exchange
    global DatCounter
    global programName

    exchange = toWhat
    programName =pn
    # update ASAP
    DatCounter = 9000






def popupmsg(msg):
    """
    Create a simple message popup window
    :param msg:
    :return:
    """
    popup = tk.Tk()

    def leavemini():
        """
        Exit a tk window instance
        :return:
        """
        popup.destroy()

    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=leavemini)
    B1.pack()
    popup.mainloop()


def animate_1(i):
    """
    Function to make live matplotlib graphs + Tkinter code using its backend
    :param i:
    :return:
    """
    # pull some example data
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x , y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList,yList)


def animate(i):
    """
    Create Visualizations of Data
    :param i:
    :return:
    """
    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    data = urllib.request.urlopen(dataLink)
    data = data.read().decode("utf-8")
    data = json.loads(data)

    data = data["btc_usd"]
    data = pd.DataFrame(data)

    buys = data[(data['type'] == "bid")]
    buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
    buyDates = (buys["datestamp"]).tolist()

    sells = data[(data['type'] == "ask")]
    sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
    sellDates = (sells["datestamp"]).tolist()

    a.clear()

    a.plot_date(buyDates, buys["price"], "#00A3E0", label="buys")
    a.plot_date(sellDates, sells["price"], "#183A54", label="sells")

    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=2, borderaxespad=0)

    title = "BTC-e BTCUSD Prices\nLast Price: " + str(data["price"][0])
    a.set_title(title)


# class for demo application
class SeaofBTCapp(tk.Tk):

    # this will always run when you initialize a class
    def __init__(self, *args, **kwargs):

        # initialize tkinter within our initialization function
        tk.Tk.__init__(self, *args, **kwargs)

        # frame is parent window
        container = tk.Frame(self)

        self.wm_title("Essential Tremometer\u2122 Alpha Skeleton")

        # pack shoves shit into the window without a lot of control
        container.pack(side="top", fill="both", expand=True)

        # set size of rows and cols
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # make top bar accessible
        menubar = tk.Menu(container)
        # make filemenu option add to menubar
        filemenu = tk.Menu(menubar, tearoff=0)

        # make function with placehold message (To Do)
        filemenu.add_command(label="Save settings", command=lambda:popupmsg('Not supported just yet!'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # make exchangeChoice option(s), add to menubar
        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="BTC-e",
                                   command=lambda:changeExchange("BTC-e", "btce"))
        exchangeChoice.add_command(label="Bitfinix",
                                   command=lambda: changeExchange("Bitfinix", "bitfinix"))
        exchangeChoice.add_command(label="Bitstamp",
                                   command=lambda: changeExchange("Bitstamp", "bitstamp"))
        exchangeChoice.add_command(label="Huobi",
                                   command=lambda: changeExchange("Huobi", "huobi"))

        menubar.add_cascade(label="Exchange", menu=exchangeChoice)



        # add to app
        tk.Tk.config(self, menu=menubar)



        # self.frames is empty dictionary
        self.frames = {}

        # to make new page and add to application:
        # make class that inherits tk.Frame and add to tuple below
        for F in (StartPage, PageOne, BTCE_Page):

            # make a frame that hasn't been created will stuff into frame dictionary above for switching windows
            frame = F(container, self)
            self.frames[F] = frame

            # put at location north south east west (alignment stretch equally)
            frame.grid(row=0, column=0, sticky="nsew")

        # show the start page frame
        self.show_frame(StartPage)

    def show_frame(self, cont):
        """
        Display a frame
        :param cont: Frame to display
        :return: Frame in GUI format
        """
        # get frame to display from frame of dictionaries
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        # parent class is SeaofBTC app
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="""ALPHA Application
        Use at your own risk. There is no promise of warranty
        """, font=LARGE_FONT)

        # pack the label into start window
        label.pack(pady=10, padx=10)

        # make simple button and add to start page. To pass arguments to functions, must use lambda: syntax
        button1 = tk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(BTCE_Page))
        button1.pack()

        button2 = tk.Button(self, text="Disagree",
                            command=quit)
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


# graph page
class BTCE_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # add toolbar to canvas
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == "__main__":

    # initialize the application
    app = SeaofBTCapp()
    app.geometry("1280x720")

    # add animate function with update 1000 ms
    ani = animation.FuncAnimation(f, animate, interval=5000)

    # run the tkinter application
    app.mainloop()
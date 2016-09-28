import tkinter as tk

# define constants
LARGE_FONT = ("Verdana", 12)


# class for demo application
class SeaofBTCapp(tk.Tk):

    # this will always run when you initialize a class
    def __init__(self, *args, **kwargs):

        # initialize tkinter within our initialization function
        tk.Tk.__init__(self, *args, **kwargs)

        # frame is parent window
        container = tk.Frame(self)

        # pack shoves shit into the window without a lot of control
        container.pack(side="top", fill="both", expand=True)

        # set size of rows and cols
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # self.frames is empty dictionary
        self.frames = {}

        # to make new page and add to application:
        # make class that inherits tk.Frame and add to tuple below
        for F in (StartPage, PageOne, PageTwo):

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
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)

        # pack the label into start window
        label.pack(pady=10, padx=10)

        # make simple button and add to start page. To pass arguments to functions, must use lambda: syntax
        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visig Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()



if __name__ == "__main__":

    # initialize the application
    app = SeaofBTCapp()

    # run the tkinter application
    app.mainloop()
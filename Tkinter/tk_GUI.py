import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import tkinter as tk
import sys
import threading
import time
import queue
import pandas as pd


# import statements for user written functions
from data_analysis.data_display import display_acceleration, display_displacement

# add other folders to path for imports
sys.path.insert(0, '/Users/Sai/Box Sync/Home Folder snn7/Private/Misc/BME 464'
                   '/BME_464/Project/tremor_quant/data_receive')
sys.path.insert(0, '/Users/Sai/Box Sync/Home Folder snn7/Private/Misc/BME 464/'
                   'BME_464/Project/tremor_quant/data_analysis')


pd.options.mode.chained_assignment = None

TITLE_FONT = ("Verdana", 24)
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

style.use("ggplot")

# declare main plot and geometry here
f = plt.Figure()
a = f.add_subplot(111)


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


class ThreadedClient(threading.Thread):
    def __init__(self, queue, fcn):
        threading.Thread.__init__(self)
        self.queue = queue
        self.fcn = fcn
    def run(self):
        time.sleep(1)
        self.queue.put(self.fcn())

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

        ######################
        #  Threading definitions
        thread_queue = queue.Queue()
        def bluetooth_acquire():
            import subprocess as sub
            sub.call('./blubutt.sh', shell=True)

        def spawnthread(fcn):
            thread = ThreadedClient(thread_queue, fcn)
            thread.start()
            #periodiccall(thread)

        def periodiccall(thread):
            if (thread.is_alive()):
                parent.after(100, lambda: periodiccall(thread))
        #######################

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        start_button = tk.Button(self, text="Start Measurement", command=lambda: spawnthread(bluetooth_acquire))
        start_button.pack()

        plot_button = tk.Button(self, text="Display Acceleration", command=lambda: display_acceleration(self, f, a))
        plot_button.pack()
        

        plot_button = tk.Button(self, text="Display Displacement", command=lambda: display_displacement(self, f, a))
        plot_button.pack()

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class updrs_page(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="Unified Parkinsons Disease Rating Scale", font=TITLE_FONT)
        title.place(relx=0.5, rely=0.5, anchor='center')
        title.grid(row=0, column=0, columnspan=2)

        speech_options = ["0 = Normal.",
                          "1 = Slight loss of expression, diction and/or volume.",
                          "2 = Monotone, slurred but understandable; moderately impaired.",
                          "3 = Marked impairment, difficult to understand.",
                          "4 = Unintelligible."]
        facial_options = ["0 = Normal.",
                          "1 = Minimal hypomimia, could be normal \"Poker Face\".",
                          "2 = Slight but definitely abnormal diminution of facial expression.",
                          "3 = Moderate hypomimia; lips parted some of the time.",
                          "4 = Masked or fixed facies with severe or complete loss of facial expression; lips parted 1/4 inch or more."]
        rigidity_options = ["0 = Absent.",
                            "1 = Slight or detectable only when activated by mirror or other movements.",
                            "2 = Mild to moderate.",
                            "3 = Marked, but full range of motion easily achieved.",
                            "4 = Severe, range of motion achieved with difficulty."]
        hand_options = ["0 = Normal.",
                        "1 = Mild slowing and/or reduction in amplitude.",
                        "2 = Moderately impaired. Definite and early fatiguing. May have occasional arrests in movement.",
                        "3 = Severely impaired. Frequent hesitation in initiating movements or arrests in ongoing movement.",
                        "4 = Can barely perform the task."]

        fingertaps_options = hand_options
        rapidalternate_options = hand_options
        legagility_options = hand_options
        chair_options = ["0 = Normal",
                         "1 = Slow; or may need more than one attempt.",
                         "2 = Pushes self up from arms of seat.",
                         "3 = Tends to fall back and may have to try ore than one time, but can get up without help.",
                         "4 = Unable to arise without help."]
        posture_options = ["0 = Normal erect.",
                           "1 = Not quite erect, slightly stooped in posture; could be normal for an older person.",
                           "2 = Moderately stooped in posture, definitely abnormal; can be slightly leaning to one side.",
                           "3 = Severely stooped posture with kyphosis; can be moderately leaning to one side.",
                           "4 = Marked flexion with extreme abnormality of posture."]
        gait_options = ["0 = Normal.",
                        "1 = Walks slowly, may shuffle with short steps, but no festination (hastening steps) or propulsion.",
                        "2 = Walks with difficulty, but requires little or no assistance; may have some festination, short steps, or propulsion.",
                        "3 = Severe disturbance of gait, requiring assistance.",
                        "4 = Cannot walk at all, even with assistance."]
        posturalstability_options = ["0 = Normal.",
                                     "1 = Retropulsion, but recovers unaided.",
                                     "2 = Absence of postural response; would fall if not caught by examiner.",
                                     "3 = Very unstable, tends to lose balance spontaneously.",
                                     "4 = Unable to stand without assistance."]
        bodykinesia_options = ["0 = None.",
                               "1 = Minimal slowness, giving movement a deliberate character; could be normal for some persons. Possibly reduced amplitude.",
                               "2 = Mild degree of slowness and poverty of movement which is definitely abnormal. Alternatively some reduced amplitude.",
                               "3 = Moderate slowness, poverty or small amplitude of movement.",
                               "4 = Marked slowness, poverty or small amplitude of movement."]

        all_options = [speech_options,
                       facial_options,
                       rigidity_options,
                       hand_options,
                       fingertaps_options,
                       rapidalternate_options,
                       legagility_options,
                       chair_options,
                       posture_options,
                       gait_options,
                       posturalstability_options,
                       bodykinesia_options]
        all_titles = ["Speech",
                      "Facial Expression",
                      "Rigidity",
                      "Finger Taps",
                      "Hand Movements",
                      "Rapid Alternating Movement of Hands",
                      "Leg Agility",
                      "Arising from Chair",
                      "Posture",
                      "Gait",
                      "Postural Stability",
                      "Body Bradykinesia and Hypokinesia"]
        all_vars = []
        rownum = 1
        num_columns = 4

        for i in range(0, len(all_options), num_columns):
            for c in range(num_columns):
                # Label
                label = tk.Label(self, text=all_titles[i+c])
                label.grid(row=rownum, column=c, sticky="W")

                # Menu
                var = tk.StringVar()
                var.set(all_options[i][0]) # set defaults
                all_vars.append(var)

                menuargs = (self, var, *all_options[i+c])
                menu = tk.OptionMenu(*menuargs)
                menu.grid(row=rownum+1, column=c, sticky="W")

            rownum += 2



#################################### PROGRAM RUN #######################################################################
def main():
    app = TremorApp()
    app.geometry("1280x720")
    gani = animation.FuncAnimation(f, animate, interval=5000)
    app.mainloop()

if __name__ == '__main__':
    main()
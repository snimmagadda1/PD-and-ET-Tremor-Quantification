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
from data_analysis.data_display import display_acceleration, display_displacement, display_psd

# add other folders to path for imports
sys.path.insert(0, '/Users/Sai/Box Sync/Home Folder snn7/Private/Misc/BME 464'
                   '/BME_464/Project/tremor_quant/data_receive')
sys.path.insert(0, '/Users/Sai/Box Sync/Home Folder snn7/Private/Misc/BME 464/'
                   'BME_464/Project/tremor_quant/data_analysis')


pd.options.mode.chained_assignment = None

TITLE_FONT = ("Verdana", 24)
LARGE_FONT = ("Verdana", 18)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

UPDRS_LABEL_FONT = ("Verdana", 14, "bold")

MAIN_COLOR = "#5DBCD2"

style.use("ggplot")
plt.rcParams['axes.facecolor']='w'

# declare main plot and geometry here and characteristics
f = plt.Figure()
f.patch.set_facecolor('#5DBCD2')
f2= plt.Figure()
f2.patch.set_facecolor('#5DBCD2')
a = f.add_subplot(111)
a.grid(which='major', linestyle='--', color='#5DBCD2')
a1 = f2.add_subplot(241)
a2 = f2.add_subplot(242)
a3 = f2.add_subplot(243)
a4 = f2.add_subplot(244)
a5 = f2.add_subplot(245)
a6 = f2.add_subplot(246)
a7 = f2.add_subplot(247)
a8 = f2.add_subplot(248)



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
        setting1.add_command(label="Patient Page", command=lambda: self.show_frame(updrs_motor_page))
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
        for F in (start_page, graph_page,  updrs_motor_page, psd_graph_page, updrs_dailyliving_page, updrs_mentation_page):
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
        accelerometer based tremor classification platform."""))
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

        def title_frame(parent):
                self.title_f = tk.Frame(parent, width=1280, height=50, bg=MAIN_COLOR)

                title = tk.Label(self.title_f, text="Graphs: Overall Signal", font=TITLE_FONT,
                                 bg=MAIN_COLOR, fg="white")
                title.place(relx=0.5, rely=0.5, anchor='center')
                self.title_f.pack()
                return self

        def border_frame(parent):
                self.border_f = tk.Frame(parent, width=1280, height=5, bg="black")
                self.border_f.pack()
                return self


        # make button frame
        title_frame_widget = title_frame(self)
        border_frame_widget = border_frame(self)

        topframe = tk.Frame(self)
        topframe.pack(side=tk.TOP)

        start_button = tk.Button(topframe, text="Start Measurement",
                                 command=lambda: spawnthread(bluetooth_acquire))
        start_button.pack(side=tk.LEFT)

        plot_accel_button = tk.Button(topframe, text="Display Acceleration",
                                command=lambda: display_acceleration(self, f, a))
        plot_accel_button.pack(side=tk.LEFT)

        plot_displacement_button = tk.Button(topframe, text="Display Displacement",
                                      command=lambda: display_displacement(self, f, a))
        plot_displacement_button.pack(side=tk.LEFT)

        change_plot_page_button = tk.Button(topframe, text="To Individual Measurement Page",
                                             command=lambda: controller.show_frame(psd_graph_page))
        change_plot_page_button.pack(side=tk.BOTTOM)

        # pack plot canvas
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class psd_graph_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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

        def title_frame(parent):
                self.title_f = tk.Frame(parent, width=1280, height=50, bg=MAIN_COLOR)

                title = tk.Label(self.title_f, text="Graphs: Individual Signals", font=TITLE_FONT,
                                 bg=MAIN_COLOR, fg="white")
                title.place(relx=0.5, rely=0.5, anchor='center')
                self.title_f.pack()
                return self

        def border_frame(parent):
                self.border_f = tk.Frame(parent, width=1280, height=5, bg="black")
                self.border_f.pack()
                return self


        # make button frame
        title_frame_widget = title_frame(self)
        border_frame_widget = border_frame(self)


        topframe = tk.Frame(self)
        topframe.pack(side=tk.TOP)

        start_button = tk.Button(topframe, text="Start Measurement",
                                 command=lambda: spawnthread(bluetooth_acquire))
        start_button.pack(side=tk.LEFT)

        plot_psd_button = tk.Button(topframe, text="Calculate PSD",
                                 command=lambda:display_psd(self, f2, a1, a2, a3, a4, a5, a6, a7, a8))
        plot_psd_button.pack(side=tk.LEFT)

        change_plot_page_button = tk.Button(topframe, text="To Overall Measurement Page",
                                             command=lambda: controller.show_frame(graph_page))
        change_plot_page_button.pack(side=tk.BOTTOM)

        # pack plot canvas
        canvas = FigureCanvasTkAgg(f2, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



class updrs_motor_page(tk.Frame):
    rigidity_options = ["0 = Absent.",
                        "1 = Slight or detectable only when activated by mirror or other movements.",
                        "2 = Mild to moderate.",
                        "3 = Marked, but full range of motion easily achieved.",
                        "4 = Severe, range of motion achieved with difficulty."]

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

    movement_options = ["0 = Normal.",
                    "1 = Mild slowing and/or reduction in amplitude.",
                    "2 = Moderately impaired. Definite and early fatiguing. May have occasional arrests in movement.",
                    "3 = Severely impaired. Frequent hesitation in initiating movements or arrests in ongoing movement.",
                    "4 = Can barely perform the task."]

    arising_options = ["0 = Normal",
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
    poststability_options = ["0 = Normal.",
                                 "1 = Retropulsion, but recovers unaided.",
                                 "2 = Absence of postural response; would fall if not caught by examiner.",
                                 "3 = Very unstable, tends to lose balance spontaneously.",
                                 "4 = Unable to stand without assistance."]
    kinesia_options = ["0 = None.",
                           "1 = Minimal slowness, giving movement a deliberate character; could be normal for some persons. Possibly reduced amplitude.",
                           "2 = Mild degree of slowness and poverty of movement which is definitely abnormal. Alternatively some reduced amplitude.",
                           "3 = Moderate slowness, poverty or small amplitude of movement.",
                           "4 = Marked slowness, poverty or small amplitude of movement."]

    all_options = [speech_options,
                   facial_options,
                   rigidity_options,
                   movement_options,
                   movement_options,
                   movement_options,
                   movement_options,
                   arising_options,
                   posture_options,
                   gait_options,
                   poststability_options,
                   kinesia_options]

    all_labels = ["Speech",
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

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.grid()

        title_frame = tk.Frame(self, width=1280, height=50, bg=MAIN_COLOR)
        self.title_frame(self, title_frame)
        title_frame.grid(row=0, column=0, columnspan=2)

        border_frame = tk.Frame(self, width=1280, height=5, bg="black")
        border_frame.grid(row=1, column=0, columnspan=2)

        navigation_frame = tk.Frame(self, width=1280, height=100)
        self.navigation_frame(self, navigation_frame, controller)
        navigation_frame.grid(row=2, column=0, columnspan=2)

        i = 0
        for r in range(3, 15, 2):
            # Labels

            label1 = tk.Label(self, text=self.all_labels[i], font=UPDRS_LABEL_FONT)
            label1.grid(row=r, column=0)
            label2 = tk.Label(self, text=self.all_labels[i + 1], font=UPDRS_LABEL_FONT)
            label2.grid(row=r, column=1)

            # Variables

            var1 = tk.StringVar()
            var1.set(self.all_options[i][0])
            self.all_vars.append(var1)
            var2 = tk.StringVar()
            var2.set(self.all_options[i + 1][0])
            self.all_vars.append(var2)

            # Menus

            args1 = (self, var1, *self.all_options[i])
            menu1 = tk.OptionMenu(*args1)
            menu1.grid(row=r + 1, column=0, padx=50, pady=20)

            args2 = (self, var2, *self.all_options[i + 1])
            menu2 = tk.OptionMenu(*args2)
            menu2.grid(row=r + 1, column=1, padx=50, pady=20)

            i += 1

    def title_frame(self, parent, frame):
        title = tk.Label(frame, text="Unified Parkinson\'s Disease Rating Scale - Motor Exam", font=TITLE_FONT,
                         bg=MAIN_COLOR, fg="white", padx=308, pady=8)
        title.grid()

    def navigation_frame(self, parent, frame, controller):
        motor_exam_butt = tk.Button(frame, text="Motor Exam", command=lambda: controller.show_frame(updrs_motor_page))
        motor_exam_butt.grid(row=0, column=0)

        daily_living_butt = tk.Button(frame, text="Activities of Daily Living", command=lambda: controller.show_frame(updrs_dailyliving_page))
        daily_living_butt.grid(row=0, column=1)

        mentation_butt = tk.Button(frame, text="Mentation, Behavior, and Mood",
                                   command=lambda: controller.show_frame(updrs_mentation_page))
        mentation_butt.grid(row=0, column=2)

class updrs_dailyliving_page(tk.Frame):

    speech_options = ["0 = Normal.",
                      "1 = Mildly affected, no difficulty being understood.",
                      "2 = Moderately affected, may be asked to repeat",
                      "3 = Severely affected, frequently asked to repeat",
                      "4 = Unintelligible most of time"]
    salivation_options = ["0 = Normal",
                          "1 = Slight but definite excess of saliva in mouth; may have nighttime drooling.",
                          "2 = Moderately excessive saliva with some drooling.",
                          "3 = Marked excess of saliva with some drooling.",
                          "4 = Marked drooling, requires constant tissue or handkerchief."]
    swallowing_options = ["0 = Normal.",
                          "1 = Rare choking.",
                          "2 = Occasional choking.",
                          "3 = Requires soft food.",
                          "4 = Requires NG tube or gastrotomy feeding."]
    handwriting_options = ["0 = Normal.",
                           "1 = Slightly slow or small.",
                           "2 = Moderately slow or small; all words are legible.",
                           "3 = Severely affected; not all words are legible.",
                           "4 = The majority of words are not legible."]
    food_options = ["0 = Normal.",
                    "1 = Somewhat slow and clumsy, but no help needed.",
                    "2 = Can cut most foods, although clumsy and slow; some help needed.",
                    "3 = Food must be cut by someone, but can still feed slowly.",
                    "4 = Needs to be fed."]
    dressing_options = ["0 = Normal.",
                        "1 = Somewhat slow, but no help needed.",
                        "2 = Occasional assistance buttoning, getting arms in sleeves.",
                        "3 = Considerable help required, but can do some things alone.",
                        "4 = Helpless."]
    hygiene_options = ["0 = Normal.",
                       "1 = Somewhat slow, but no help needed.",
                       "2 = Needs help to shower or bathe; or very slow in hygienic care.",
                       "3 = Requires assistance for washing, brushing teeth, combing har, going to bathroom.",
                       "4 = Foley catheter or other mechanical aids."]
    turning_options = ["0 = Normal.",
                       "1 = Somewhat slow and clumsy, but no help needed.",
                       "2 = Can turn alone or adjust sheets, but with great difficulty.",
                       "3 = Can initiate, but not turn or adjust sheets alone.",
                       "4 = Helpless."]
    falling_options = ["0 = None.",
                       "1 = Rare falling.",
                       "2 = Occasionally falls, less than once per day.",
                       "3 = Falls an average of once daily.",
                       "4 = Falls more than once daily."]
    freezing_options = ["0 = None.",
                        "1 = Rare freezing when walking; may have start hesitation.",
                        "2 = Occasional freezing when walking.",
                        "3 = Frequent freezing. Occasionally falls from freezing.",
                        "4 = Frequent falls from freezing."]
    walking_options = ["0 = Normal.",
                       "1 = Mild difficulty. May not swing arms or may tend to drag leg.",
                       "2 = Moderate difficulty, but requires little or no assistance.",
                       "3 = Severe disturbance of walking, requiring assistance.",
                       "4 = Cannot walk at all, even with assistance."]
    sensory_options = ["0 = None.",
                       "1 = Occasionally has numbness, tingling, or mild aching."
                       "2 = Frequently has numbness, tingling, or aching; not distressing.",
                       "3 = Frequent painful sensations.",
                       "4 = Excruciating pain."]

    all_options = [speech_options,
                   salivation_options,
                   swallowing_options,
                   handwriting_options,
                   food_options,
                   dressing_options,
                   hygiene_options,
                   turning_options,
                   falling_options,
                   freezing_options,
                   walking_options,
                   sensory_options]

    all_labels = ["Speech",
                  "Salivation",
                  "Swallowing",
                  "Handwriting",
                  "Cutting Food and Handling Utensils",
                  "Dressing",
                  "Hygiene",
                  "Turning in Bed and Adjusting Bed Clothes",
                  "Falling (Unrelated to Freezing)",
                  "Freezing when Walking",
                  "Walking",
                  "Sensory Complaints Related to Parkinsonism"]
    all_vars = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid()

        title_frame = tk.Frame(self, width=1280, height=50, bg=MAIN_COLOR)
        self.title_frame(self, title_frame)
        title_frame.grid(row=0, column=0, columnspan=2)

        border_frame = tk.Frame(self, width=1280, height=5, bg="black")
        border_frame.grid(row=1, column=0, columnspan=2)

        navigation_frame = tk.Frame(self, width=1280, height=100)
        self.navigation_frame(self, navigation_frame, controller)
        navigation_frame.grid(row=2, column=0, columnspan=2)

        i = 0
        for r in range(3, 17, 2):
            #Labels

            label1 = tk.Label(self, text=self.all_labels[i], font=UPDRS_LABEL_FONT)
            label1.grid(row=r, column=0)
            label2 = tk.Label(self, text=self.all_labels[i+1], font=UPDRS_LABEL_FONT)
            label2.grid(row=r, column=1)

            #Variables

            var1 = tk.StringVar()
            var1.set(self.all_options[i][0])
            self.all_vars.append(var1)
            var2 = tk.StringVar()
            var2.set(self.all_options[i+1][0])
            self.all_vars.append(var2)

            #Menus

            args1 = (self, var1, *self.all_options[i])
            menu1 = tk.OptionMenu(*args1)
            menu1.grid(row=r+1, column=0, padx=50, pady=20)

            args2 = (self, var2, *self.all_options[i+1])
            menu2 = tk.OptionMenu(*args2)
            menu2.grid(row=r + 1, column=1, padx=50, pady=20)

            i += 1



    def title_frame(self, parent, frame):
        title = tk.Label(frame, text="Unified Parkinson\'s Disease Rating Scale - Activities of Daily Living", font=TITLE_FONT,
                         bg=MAIN_COLOR, fg="white", padx=236, pady=8)
        title.grid()

    def navigation_frame(self, parent, frame, controller):
        motor_exam_butt = tk.Button(frame, text="Motor Exam", command=lambda: controller.show_frame(updrs_motor_page))
        motor_exam_butt.grid(row=0, column=0)

        daily_living_butt = tk.Button(frame, text="Activities of Daily Living",
                                      command=lambda: controller.show_frame(updrs_dailyliving_page))
        daily_living_butt.grid(row=0, column=1)
        mentation_butt = tk.Button(frame, text="Mentation, Behavior, and Mood",
                                   command=lambda: controller.show_frame(updrs_mentation_page))
        mentation_butt.grid(row=0, column=2)



class updrs_mentation_page(tk.Frame):

    intellectual_options = ["0 = None.",
                            "1 = Mild. Consistent forgetfulness with partial recollection of events and no other difficulties.",
                            "2 = Moderate memory loss, with disorientation and moderate difficulty handling complex problems.",
                            "3 = Severe memory loss with disorientation for time and often to place. Severe impairment in handling problems.",
                            "4 = Severe memory loss with orientation preserved to person only. Unable to make judgements or solve problems."]
    thought_options = ["0 = None.",
                       "1 = Vivid dreaming.",
                       "2 = \"Benign\" hallucinations with insight retained.",
                       "3 = Occasional to frequent hallucinations or delusions; without insight; could interfere with daily activities.",
                       "4 = Persistent hallucinations, delusions, or florrid psychosis. Not able to care for self."]
    depression_options = ["0 = None.",
                          "1 = Periods of sadness or guilt greater than normal, never sustained for days or weeks.",
                          "2 = Sustained depression (1 week or more).",
                          "3 = Sustained depression with vegetative symptoms (insomnia, anorexia, weight loss, loss of interest).",
                          "4 = Sustained depression with vegetative symptoms and suicidal thoughts or intent."]
    motivation_options = ["0 = Normal.",
                          "1 = Less assertive than usual; more passive.",
                          "2 = Loss of initiative or disinterest in elective (nonroutine) activities.",
                          "3 = Loss of initiative or disinterest in day to day (routine) activities.",
                          "4 = Withdrawn, complete loss of motivation."]

    all_options = [intellectual_options,
                   thought_options,
                   depression_options,
                   motivation_options]
    all_labels = ["Intellectual Impairment",
                  "Thought Disorder",
                  "Depression",
                  "Motivation/Initiative"]
    all_vars = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid()

        title_frame = tk.Frame(self, width=1280, height=50, bg=MAIN_COLOR)
        self.title_frame(self, title_frame)
        title_frame.grid(row=0, column=0)

        border_frame = tk.Frame(self, width=1280, height=5, bg="black")
        border_frame.grid(row=1, column=0)

        navigation_frame = tk.Frame(self, width=1280, height=100)
        self.navigation_frame(self, navigation_frame, controller)
        navigation_frame.grid(row=2, column=0)

        i = 0
        for r in range(3, 11, 2):
            # Labels

            label1 = tk.Label(self, text=self.all_labels[i], font=UPDRS_LABEL_FONT)
            label1.grid(row=r, column=0)

            # Variables

            var1 = tk.StringVar()
            var1.set(self.all_options[i][0])
            self.all_vars.append(var1)

            # Menus

            args1 = (self, var1, *self.all_options[i])
            menu1 = tk.OptionMenu(*args1)
            menu1.grid(row=r + 1, column=0, padx=50, pady=20)

            i += 1

    def title_frame(self, parent, frame):
        title = tk.Label(frame, text="Unified Parkinson\'s Disease Rating Scale - Mentation, Behavior, and Mood",
                         font=TITLE_FONT,
                         bg=MAIN_COLOR, fg="white", padx=192, pady=8)
        title.grid()

    def navigation_frame(self, parent, frame, controller):
        motor_exam_butt = tk.Button(frame, text="Motor Exam",
                                    command=lambda: controller.show_frame(updrs_motor_page))
        motor_exam_butt.grid(row=0, column=0)

        daily_living_butt = tk.Button(frame, text="Activities of Daily Living",
                                      command=lambda: controller.show_frame(updrs_dailyliving_page))
        daily_living_butt.grid(row=0, column=1)

        mentation_butt = tk.Button(frame, text="Mentation, Behavior, and Mood",
                                   command=lambda: controller.show_frame(updrs_mentation_page))
        mentation_butt.grid(row=0, column=2)


#################################### PROGRAM RUN #######################################################################
def main():
    app = TremorApp()
    app.geometry("1280x720")
    ani = animation.FuncAnimation(f, animate, interval=5000)
    app.mainloop()

if __name__ == '__main__':
    main()
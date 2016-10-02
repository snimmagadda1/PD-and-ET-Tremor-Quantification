BME Capstone Design Project

Essential Tremometer 


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
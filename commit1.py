import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class OpenCartMonitor(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("OpenCart Monitor & Dashboard")
        self.geometry("1200x600")

        self.grid = tk.Frame(self)
        self.grid.pack(expand=True, fill=tk.BOTH)

        self.create_widgets()
        self.populate_opencart_data()
        self.populate_dashboard()

    
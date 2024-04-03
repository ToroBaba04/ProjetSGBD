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

    def create_widgets(self):
        # Entetes
        header_label = tk.Label(self.grid, text="OpenCart Monitoring Dashboard", font=("Helvetica", 16, "bold"), fg="white", bg="blue")
        header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="ew")

        # Labels de données OpenCart
        self.label_orders = tk.Label(self.grid, text="Total Orders: ", font=("Helvetica", 12, "bold"), fg="white", bg="green")
        self.label_orders.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.label_new_users = tk.Label(self.grid, text="New Users: ", font=("Helvetica", 12, "bold"), fg="white", bg="orange")
        self.label_new_users.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.label_total_visits = tk.Label(self.grid, text="Total Visits: ", font=("Helvetica", 12, "bold"), fg="white", bg="purple")
        self.label_total_visits.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.label_conversion_rate = tk.Label(self.grid, text="Conversion Rate: ", font=("Helvetica", 12, "bold"), fg="white", bg="cyan")
        self.label_conversion_rate.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.label_server_errors = tk.Label(self.grid, text="Server Errors: ", font=("Helvetica", 12, "bold"), fg="white", bg="red")
        self.label_server_errors.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Cartes du Tableau de Bord
        self.charts_frame = tk.Frame(self.grid)
        self.charts_frame.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")

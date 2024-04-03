import tkinter as tk
import mysql.connector
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

    def populate_opencart_data(self):
        # Connexion a la BDD OpenCart
        connection = mysql.connector.connect(
            host="localhost",
            user="babadi",
            password="laisserpasser",
            database="baba"
        )
        cursor = connection.cursor()

        # Récupération des données depuis la BDD
        cursor.execute("SELECT COUNT(*) FROM oc_order;")
        total_orders = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM oc_customer WHERE date_added >= '2024-01-01 00:00:00' AND date_added <= '2024-03-31 23:59:59'")
        new_users = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM oc_customer_online WHERE date_added >= '2024-01-01 00:00:00' AND date_added <= '2024-03-31 23:59:59'")
        total_visits = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM oc_order_history WHERE order_status_id = 0 AND date_added >= '2024-01-01 00:00:00' AND date_added <= '2024-03-31 23:59:59'")
        server_errors = cursor.fetchone()[0]

        # Fermeture de la connexion à la BDD
        cursor.close()
        connection.close()

        # Mise a jour des labels
        self.label_orders.config(text=f"Total Orders: {total_orders}")
        self.label_new_users.config(text=f"New Users: {new_users}")
        self.label_total_visits.config(text=f"Total Visits: {total_visits}")
        if total_visits > 0:
            conversion_rate = total_orders / total_visits
        else:
            conversion_rate = 0
        self.label_conversion_rate.config(text=f"Conversion Rate: {conversion_rate:.2f}%")
        self.label_server_errors.config(text=f"Server Errors: {server_errors}")

    
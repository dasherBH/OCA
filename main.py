import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OvercurrentCoordinationAssistant:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Overcurrent Coordination Assistant | Developed By Mostafa Neisi (mostafaneisi@yahoo.com)")

        # Create four setting sections
        self.upstream_relay_section = self.create_section("Upstream Relay", 0)
        self.outgoing_relay_section = self.create_section("Out-going Relay", 1)
        self.incoming_relay_section = self.create_section("Incoming Relay", 2)
        self.fault_current_section = self.create_section("Fault Current", 3, False)

        self.calculate_button = tk.Button(self.window, text="Calculate Settings", command=self.calculate)
        self.calculate_button.grid(row=1, column=5, sticky="e", padx=10, pady=10)

        # Create a frame for the graph
        self.graph_frame = tk.Frame(self.window, width=700, height=700)
        self.graph_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10)

        # Create a figure for the graph
        self.figure = plt.figure(figsize=(7, 7))
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Upstream_Relay   1st_TRIP    OUT-going_Relay    Incoming_Relay')

        # Create a canvas for the graph
        self.graph_canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.graph_canvas.get_tk_widget().pack()


    def create_section(self, title, row, add_controls=True):

        if add_controls:
            section_frame = tk.LabelFrame(self.window, text=title)
            section_frame.grid(row=row, column=0, padx=10, pady=10)

            # Add settings controls to the section
            tk.Label(section_frame, text="CURVE").grid(row=0, column=0, padx=10, pady=5)
            curve_values = ["LONG TIME V.I.", "LONG TIME INV", "ICE N.INV", "ICE V.INV", "ICE INV", "ICE E.INV", "ICE SHORT TIME", "ICE LONG TIME"]
            curve_dropdown = ttk.Combobox(section_frame, values=curve_values)
            curve_dropdown.grid(row=0, column=1, padx=10, pady=5)
            curve_dropdown.current(0)

            # Add Pick-up IDMT Stage widget
            tk.Label(section_frame, text="Pick-up IDMT Stage").grid(row=1, column=1, padx=10, pady=5)
            idmt_on_off = tk.Checkbutton(section_frame)
            idmt_on_off.grid(row=1, column=0, padx=10, pady=5)
            idmt_number_frame = tk.Frame(section_frame)
            idmt_number_frame.grid(row=1, column=2, padx=1, pady=5)
            tk.Entry(idmt_number_frame, width=5).grid(row=1, column=1, padx=1, pady=5)
            tk.Label(idmt_number_frame, text="Primary (A)\n450.00").grid(row=1, column=3, padx=5, pady=5)
            tk.Label(idmt_number_frame, text="Secondary (A)\n0.90").grid(row=1, column=4, padx=5, pady=5)

            # Add Time Multiplier widget
            tk.Label(section_frame, text="Time Multiplier").grid(row=2, column=1, padx=10, pady=5)
            idmt_number_frame = tk.Frame(section_frame)
            idmt_number_frame.grid(row=2, column=2, padx=1, pady=5)
            tk.Entry(idmt_number_frame, width=5).grid(row=2, column=1, padx=5, pady=5)

            # Add Min Op.Del.Time widget
            tk.Label(section_frame, text="Min Op.Del.Time").grid(row=3, column=1, padx=10, pady=5)
            idmt_number_frame = tk.Frame(section_frame)
            idmt_number_frame.grid(row=3, column=2, padx=1, pady=5)
            tk.Entry(idmt_number_frame, width=5).grid(row=3, column=1, padx=5, pady=5)

            # Add Pick-up DT Stage widget
            tk.Label(section_frame, text="Pick-up DT Stage").grid(row=4, column=1, padx=10, pady=5)
            idmt_on_off = tk.Checkbutton(section_frame)
            idmt_on_off.grid(row=4, column=0, padx=10, pady=5)
            idmt_number_frame = tk.Frame(section_frame)
            idmt_number_frame.grid(row=4, column=2, padx=1, pady=5)
            tk.Entry(idmt_number_frame, width=5).grid(row=4, column=1, padx=1, pady=5)
            tk.Label(idmt_number_frame, text="Primary (A)\n2250.00").grid(row=4, column=3, padx=5, pady=5)
            tk.Label(idmt_number_frame, text="Secondary (A)\n4.5").grid(row=4, column=4, padx=5, pady=5)

            # Add Op. Del. Time widget
            tk.Label(section_frame, text="Op. Del. Time").grid(row=5, column=1, padx=10, pady=5)
            idmt_number_frame = tk.Frame(section_frame)
            idmt_number_frame.grid(row=5, column=2, padx=1, pady=5)
            tk.Entry(idmt_number_frame, width=5).grid(row=5, column=1, padx=5, pady=5)

            tk.Label(section_frame, text="CT Prim. curr.").grid(row=6, column=0, padx=10, pady=5)
            curve_values = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
            curve_dropdown = ttk.Combobox(section_frame, values=curve_values)
            curve_dropdown.grid(row=6, column=1, padx=5, pady=5)
            curve_dropdown.current(0)

            tk.Label(section_frame, text="CT Sec. curr.").grid(row=6, column=2, padx=10, pady=5)
            curve_values = [1, 500]
            curve_dropdown = ttk.Combobox(section_frame, values=curve_values)
            curve_dropdown.grid(row=6, column=3, padx=5, pady=5)
            curve_dropdown.current(0)


            return section_frame

        section_frame = tk.LabelFrame(self.window, text=title)
        section_frame.grid(row=row, column=0, padx=10, pady=10)

        # Add Pick-up IDMT Stage widget
        idmt_number_frame = tk.Frame(section_frame)
        idmt_number_frame.grid(row=1, column=2, padx=10, pady=5)
        tk.Entry(idmt_number_frame, width=5).grid(row=0, column=0, padx=5, pady=5)



    def calculate(self):
        
        pass

        
    def run(self):
        self.window.mainloop()

app = OvercurrentCoordinationAssistant()
app.run()

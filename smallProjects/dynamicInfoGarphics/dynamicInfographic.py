import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkinter import font
from matplotlib.lines import lineStyles
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MathFunctionPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Function Plotter")
        self.root.configure(bg="#1d1d2c")
        self.defaultFont = font.nametofont("TkDefaultFont") 
  
        # Overriding default-font with custom settings 
        # i.e changing font-family, size and weight 
        self.defaultFont.configure(family="Mononoki Nerd Font", 
                                   size=16, 
                                   weight=font.BOLD) 


        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widget for function input
        ttk.Label(self.root, text="Math Function:").grid(row=0, column=0, padx=5, pady=5)
        self.function_entry = ttk.Entry(self.root, font=("Mononoki 16"))
        self.function_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to plot the function
        ttk.Button(self.root, text="Plot Function", command=self.plot_function).grid(row=0, column=2, padx=5, pady=5)

        # Frame for plotting
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Matplotlib Figure
        self.figure = Figure(figsize=(5, 4), dpi=100, facecolor='#f7f4e9')
        self.plot = self.figure.add_subplot(1, 1, 1)

        # Set background color of the plot
        self.plot.set_facecolor('#f7f4e9')

        # Canvas to display the plot
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def plot_function(self):
        function_str = self.function_entry.get()

        try:
            x = np.linspace(-10, 10, 400)
            y = eval(function_str, {"__builtins__": None}, {'x': x, 'np': np})

            # Clear the previous plot
            self.plot.clear()

            # Plot the function with the desired color
            self.plot.plot(x, y, color = '#3cbcc3')  # Set color to #1d1d2c
            self.plot.set_xlabel('X')
            self.plot.set_ylabel('Y')
            self.plot.set_title(f'Function Plot: {function_str}')

            # Add grid
            self.plot.grid(True, color='#1d1d2c', alpha=0.5, linestyle = '--')

            # Redraw the canvas
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", f"Invalid function. {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathFunctionPlotter(root)
    root.mainloop()


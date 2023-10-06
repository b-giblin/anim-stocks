import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf

# Function to fetch stock price data
def fetch_stock_data(symbol): 
    data = yf.download(symbol, period='1y')['Close'] 
    return data

# Function to create and display a bar chart animation
def animate_bar_chart(data):
    fig, ax = plt.subplots()
    bar = ax.bar([], [])

    def update(i):
        ax.clear()
        ax.bar(data.index[:i+1], data[:i+1])
        ax.set_ylim(0, max(data))

    ani = FuncAnimation(fig, update, frames=len(data), interval=200, repeat=False)
    plt.show()

# Function to create and display a line plot animation
def animate_line_plot(data):
    fig, ax = plt.subplots()
    line, = ax.plot([], [])

    def update(i):
        ax.clear()
        ax.plot(data.index[:i+1], data[:i+1])
        ax.set_ylim(0, max(data))

    ani = FuncAnimation(fig, update, frames=len(data), interval=200, repeat=False)
    plt.show()

# Function to create and display a scatter plot animation
def animate_scatter_plot(data):
    fig, ax = plt.subplots()
    scatter = ax.scatter([], [])

    def update(i):
        ax.clear()
        ax.scatter(data.index[:i+1], data[:i+1])
        ax.set_ylim(0, max(data))

    ani = FuncAnimation(fig, update, frames=len(data), interval=200, repeat=False)
    plt.show()

# Create GUI
root = tk.Tk()

# Function to handle button click event
def handle_button_click():
    symbol = entry.get()
    data = fetch_stock_data(symbol)

    if var.get() == 1:
        animate_bar_chart(data)
    elif var.get() == 2:
        animate_line_plot(data)
    elif var.get() == 3:
        animate_scatter_plot(data)

# Add entry field for stock symbol input
label = tk.Label(root, text="Symbol:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Add radio buttons for visualization options
var = tk.IntVar()
bar_button = tk.Radiobutton(root, text="Bar Chart", variable=var, value=1)
bar_button.pack()


# Add radio buttons for visualization options
line_button = tk.Radiobutton(root, text="Line Plot", variable=var, value=2)
line_button.pack()

scatter_button = tk.Radiobutton(root, text="Scatter Plot", variable=var, value=3)
scatter_button.pack()

# Add button to initiate data visualization
button = tk.Button(root, text="Visualize", command=handle_button_click)
button.pack()

# Run the GUI
root.mainloop()

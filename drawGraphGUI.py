import matplotlib.pyplot as plt  # for plotting graphs
from numpy import *              # for arrays
import math
import tkinter
import tkinter.messagebox


def drawCartesianGraph(function="x", lower_limit=-1, upper_limit=1):
    """ Plots a cartesian graph of the function you pass to it. 
    lower_limit and upper_limit specify the region over which to draw the graph.

    Args:
        function (str, optional): A string representing the mathematical function to be graphed. Defaults to "x".
        lower_limit (int, optional): The lowest x value from which we'll draw the graph. Defaults to -1.
        upper_limit (int, optional): The highest x value to which we'll draw the graph. Defaults to 1.

    Returns:
        None
    """

    if lower_limit >= upper_limit:
        return None

    # generate a range of values corresponding to the specified range
    x = arange(lower_limit, upper_limit, (upper_limit - lower_limit) / 10000)

    # use the given function to evaluate y = f(x)
    y = eval(function)

    # plot and show the graph
    plt.plot(x, y)
    plt.title("Cartesian Graph of f(x) = " + function)
    plt.show()


def drawPolarGraph(function="x", lower_limit=-1, upper_limit=1):
    """ Plots a polar graph of the function you pass to it. lower_limit 
    and upper_limit specify the region over which to draw the graph.

    Args:
        function (str, optional): A string representing the mathematical function to be graphed. Defaults to "x".
        lower_limit (int, optional): The lowest x value from which we'll draw the graph. Defaults to -1.
        upper_limit (int, optional): The highest x value to which we'll draw the graph. Defaults to 1.

    Returns:
        None
    """

    if lower_limit >= upper_limit:
        return None

    # generate a range of values corresponding to the specified range
    θ = arange(lower_limit, upper_limit, (upper_limit - lower_limit)/10000)

    function = function.replace("x", "θ")

    # use the given function to evaluate r = f(θ)
    r = eval(function)

    # convert polar coordinates to cartesian coordinates
    x = r * cos(θ)
    y = r * sin(θ)

    # plot and show the graph
    plt.plot(x, y)
    plt.title("Polar Graph of f(θ) = " + function)
    plt.show()


class GraphDrawer:
    def __init__(self):
        window = tkinter.Tk()
        window.title("Draw Graphs")

        # for some reason, tkinter doesn't recognise relative paths, so
        # if you  want the app icon to be visible, you have to use an
        # absolute path to icon.ico in the current folder as below:

        # window.iconbitmap(
        #     "C:\\Programming\\pyCode\\drawGraph\\icon.ico"
        # )

        self.function = tkinter.StringVar()
        self.lower_limit = tkinter.StringVar()
        self.upper_limit = tkinter.StringVar()
        self.graph_type = tkinter.IntVar()

        func_label = tkinter.Label(window, text="Enter function f(x):")
        func_label.grid(row=0, column=0)
        func_entry = tkinter.Entry(window, textvariable=self.function)
        func_entry.grid(row=0, column=1)

        func_label = tkinter.Label(window, text="Enter starting value:")
        func_label.grid(row=1, column=0)
        func_entry = tkinter.Entry(window, textvariable=self.lower_limit)
        func_entry.grid(row=1, column=1)

        func_label = tkinter.Label(window, text="Enter ending value:")
        func_label.grid(row=2, column=0)
        func_entry = tkinter.Entry(window, textvariable=self.upper_limit)
        func_entry.grid(row=2, column=1)

        cartesian_rb = tkinter.Radiobutton(
            window, text="Cartesian Graph", variable=self.graph_type, value=1)
        cartesian_rb.grid(row=3, column=0)
        polar_rb = tkinter.Radiobutton(
            window, text="Polar graph",  variable=self.graph_type, value=2)
        polar_rb.grid(row=3, column=1)

        button = tkinter.Button(
            window, text="Draw graph", command=self.draw_graphs)
        button.grid(row=4, column=1)

        window.mainloop()

    def draw_graphs(self):
        """ Draws graph using the input values from the user

        Returns:
            None
        """
        try:
            upper_limit = self.upper_limit.get()
            lower_limit = self.lower_limit.get()
            expr = self.function.get()
            graph_type = self.graph_type.get()

            if (expr == ""):
                tkinter.messagebox.showerror("Error", "\nFunction is empty")
                return None

            try:
                start = float(lower_limit)
            except ValueError:
                if lower_limit == "":
                    tkinter.messagebox.showerror(
                        "Error", "\nStarting value is empty")
                else:
                    tkinter.messagebox.showerror(
                        "Error", "\nInvalid starting value: " + str(lower_limit))
                return None

            try:
                end = float(upper_limit)
            except ValueError:
                if upper_limit == "":
                    tkinter.messagebox.showerror(
                        "Error", "\nUpper limit is empty")
                else:
                    tkinter.messagebox.showerror(
                        "Error", "\nInvalid ending value: " + str(upper_limit))
                return None

            if graph_type == 0:
                tkinter.messagebox.showerror(
                    "Error", "\nNo graph type selected")
                return None
            elif graph_type == 1:
                drawCartesianGraph(expr, start, end)
            elif graph_type == 2:
                drawPolarGraph(expr, start, end)
        except Exception as exception:
            tkinter.messagebox.showerror("Error", str(exception))


GraphDrawer()

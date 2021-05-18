import matplotlib.pyplot as plt  # for plotting graphs
from numpy import *              # for arrays
import math


def drawCartesianGraph(function="x", lower_limit=-1, upper_limit=1):
    """
    Plots a cartesian graph of the function you pass to it. lower_limit 
    and upper_limit specify the region over which to draw the graph.
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
    """
    Plots a polar graph of the function you pass to it. lower_limit 
    and upper_limit specify the region over which to draw the graph.
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


expr = input("Enter the function to graph: \n\n    f(x) = ")
start = eval(input("\nEnter the starting value for the range: "))
end = eval(input("Enter the ending value for the range: "))
drawCartesianGraph(expr, start, end)
drawPolarGraph(expr, start, end)

#! /usr/bin/env python3

# make a script that plots data and makes a regression plot for each of the three species
from scipy import stats
import pandas as pd 
import matplotlib.pyplot as plt 
import sys

def read_data(data):
    '''
    DESCRIPTION
    ------
    A simple function to read in a csv file convert it to a pandas dataframe and store it as an object.
    ------
    INPUT
    ------
    data = a str with the path to a csv file you want to input
    ------
    OUTPUT
    ------
    A stored pandas dataframe
    '''
    df = pd.read_csv(data)

    return df

def plot_variables(df, column1, column2, output = 'output'):
    '''
    DESCRIPTION
    ------
    This function creates a scatter plot for two variables
    ------
    INPUT
    ------
    df = a pandas dataframe that can be read in from a csv file using the RegPlot.read_data('csvfile') argument
    column1 = a column of int that you want to plot
    column2 = a column of int that you want to plot and regress against column1
    output = a str containing the desired name for an output file, without the file extension. Default = output
    ------
    OUTPUT
    ------
    A .png file containing a scatter plot of the data    
    '''

    x = df[column1]
    y = df[column2]
    plt.scatter(x, y, label = 'Data')
    plt.xlabel(column2)
    plt.ylabel(column1)
    plt.legend()
    plt.savefig(str(output)+'-data.png')

def plot_reg(df, column1, column2, output = 'output'):
    '''
    DESCRIPTION
    ------
    This function creates a regression plot for any two variables
    ------
    INPUT
    ------
    df = a pandas dataframe that can be read in from a csv file using the RegPlot.read_data('csvfile') argument
    column1 = a column of int that you want to plot
    column2 = a column of int that you want to plot and regress against column1
    output = a str containing the desired name for an output file, without the file extension. Default = output
    ------
    OUTPUT
    ------
    A .png file containing a scatter plot of the data with a regression line through the plot
    '''
    x = df[column1]
    y = df[column2]
    # print(x,y)
    regression = stats.linregress(x,y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.legend()
    plt.savefig(str(output)+'-reg.png')

def plot_all(df, column1, column2, groups):
    '''
    ------
    DESCRIPTION
    ------
    Use this function to create a plot of variable data and regression of two variables, sorting by categories in a column.
    ------
    INPUT
    ------
    df = a pandas dataframe that can be read in from a csv file using the RegPlot.read_data('csvfile') argument
    column1 = a column of int that you want to plot
    column2 = a column of int that you want to plot and regress against column1
    groups = categorical data of type str that will be used to create the different plots
    ------
    OUTPUT
    ------
    For each variable of categorical data there will be a variable plot and a linear regression plot output as a .png file
    '''
    unique_values = df[groups].unique()
    # print(unique_values)
    for i in unique_values:
        print("starting new plot")
        species_df = df[df[groups] == i]
        # print(i)
        # print(species_df)
        print("making variable plot for", i)
        plt.clf()
        plot_variables(species_df, column1, column2, i)
        plt.clf()
        print("making regression plot for", i)
        plot_reg(species_df, column1, column2, i)

         

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Expecting python file name + four arguments: .csv file, column1, column2, grouping column (e.g., column with species names). You provided", len(sys.argv)-1, "arguments.")
    else:
        data = sys.argv[1]
        column1 = sys.argv[2]
        column2 = sys.argv[3]
        groups = sys.argv[4]
        df = read_data(data)
        plot_all(df, column1, column2, groups)
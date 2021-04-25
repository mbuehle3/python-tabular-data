#! /usr/bin/env python3

# make a script that plots data and makes a regression plot for each of the three species
from scipy import stats
import pandas as pd 
import matplotlib.pyplot as plt 

def read_data(data):
    '''
    '''
    df = pd.read_csv(data)

    return df

def plot_variables(df, column1, column2, output = 'output'):

    x = df[column1]
    y = df[column2]
    plt.scatter(x, y, label = 'Data')
    plt.xlabel(column2)
    plt.ylabel(column1)
    plt.legend()
    plt.savefig(str(output)+'-data.png')

def plot_reg(df, column1, column2, output = 'output'):
    '''
    '''
    x = df[column1]
    y = df[column2]
    print(x,y)
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
    '''
    unique_values = df[groups].unique()
    print(unique_values)
    for i in unique_values:
        print("starting new plot")
        species_df = df[df[groups] == i]
        print(i)
        print(species_df)
        print("making variable plot for", i)
        plt.clf()
        plot_variables(species_df, column1, column2, i)
        plt.clf()
        print("making regression plot for", i)
        plot_reg(species_df, column1, column2, i)
    print(species_df)

         

if __name__ == '__main__':
    pass
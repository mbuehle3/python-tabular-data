import pandas as pd
# if using packages make sure that you are using the write python on the computer
# there is the usr/bin/python3
# and there is ~/mbuehle3/miniconda/bin/python
# the second will have modules installed with conda


# load in the data using pandas

dataframe = pd.read_csv("iris.csv")
print(type(dataframe))
print(dataframe)

# look at the single columns in the data using pandas

# using the 'dot' syntax
print(dataframe.sepal_length_cm)

# using a dictionary like syntax

print(dataframe["sepal_length_cm"])

# to look at rows use the 'iloc' (index location) command
# looking at the first five rows 
print(dataframe.iloc[0:5])

# to get a value for a specific cell

print(dataframe.iloc[0,0])

# to get values for the first few cells in a column

print(dataframe.iloc[0:3, 0])
# could also use

# filter the data to retain only the long boi flowers
# export to a dataframe called long_flowers
long_flowers = dataframe[dataframe.petal_length_cm > 5.9]
print(long_flowers)

# get data for a single species of iris

versicolor = dataframe[dataframe.species == "Iris_versicolor"]
print(versicolor)


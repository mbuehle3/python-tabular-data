import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("iris.csv")
plt.scatter(dataframe.petal_length_cm, dataframe.sepal_length_cm)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("petal_v_sepal_length.png")
quit()
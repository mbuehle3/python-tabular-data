from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("iris.csv")
x = dataframe.petal_length_cm
y = dataframe.sepal_length_cm

# perform a regression on our two variables

regression = stats.linregress(x,y)
slope = regression.slope
intercept = regression.intercept

plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress.png")
quit()
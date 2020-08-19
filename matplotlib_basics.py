from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
data = iris.data
column_names = iris.feature_names
column_names
df = pd.DataFrame(data, columns = column_names)

import matplotlib.pyplot as plt
#set the plot figures and size
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})

#scatterplot
df.plot(kind = 'scatter', x = 'sepal length (cm)', y= 'sepal width (cm)')

#histogram
df['sepal length (cm)'].plot(kind = 'hist', title = 'Rating')

#boxplot
df['sepal length (cm)'].plot(kind = 'box', title = 'Rating')

### Convert NumPy array to a Pandas Frame
import pandas as pd

## create data frame
sample_info = [['New York', 10, 'this'], ['Philadelphia', 4 , 'that'], ['Texas', 8, 'the other']]

sample_df = pd.DataFrame(sample_info, columns = ['Place', 'Amount', 'Type'],index = ['A', 'B', 'C'])
sample_df

#print column
sample_df['Place']

#position indexing - starts at 0
sample_df.iloc[0]

## iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data
column_names = iris.feature_names
column_names
#length
len(data)

#slicing and indexing
data[:2] #two rows
data[2:5]

#convert to pandas DataFrame
df = pd.DataFrame(data, columns = column_names)
df.head()
df.tail()
df.describe()
df.loc[140] #locate one specific
df.loc[140:] #locate subsequent rows

#summarize mean values
df.groupby(['sepal width (cm)']).mean()

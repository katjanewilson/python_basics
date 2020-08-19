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

#duplicates
df.shape
df.drop_duplicates

#rename columsn
df2 = df.rename({'petal width (cm)': 'Width of Petals'})
print(df2)

#check null values
df2.isnull()
df2.isnull().sum()

#drop missing values
df2.dropna(axis =1)

#imputation

#seelct a paticular columns
Width = df2['Width of Petals']
Width.head()
Width_mean = Width.mean()
Width_mean
#fill in the missing values with the mean
df2.fillna(Width_mean, inplace = True)

#describe all values
df2.describe()

#count row totals
df2['Width of Petals'].value_counts().head(30)

#correlation
df2.corr()

#conditional selection
df2[df2['Width of Petals'] >= 2.3]

#complex conditional seection
df2[(df2['sepal length (cm)'] == 6.3) | (df2['sepal length (cm)'] == 6.4) ]

#create a sequence of conditions

# df2[
#   ((df2['sepal length (cm)'] > 7 )
#   & (df2['Width of Petals'] <3))
# ]

##functions


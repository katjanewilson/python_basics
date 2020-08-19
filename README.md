
## Python Basics

Prep for CIS 545
* [CIS](https://sites.google.com/seas.upenn.edu/cis545/home)


## Numpy Basics

```
#create 1D numpy array from a list
array_1d = np.array([1, 2, 3, 4, 5])

print (array_1d)

list_1 = [11, 22, 33, 44, 55]
array_l1 = np.array(list_1)

print(array_l1)

print ("NumPy version - " + np.version.version)
print(array_1d.shape)
type(array_1d)
plain_range = range(4,12)
list(plain_range)
interval_range = range(1, 15, 2)
list(interval_range)
list(range(15, 1, -2))

```

## Pandas Basics
```

#convert to pandas DataFrame
df = pd.DataFrame(data, columns = column_names)
df.head()
df.tail()
df.describe()
df.loc[140] #locate one specific
df.loc[140:] #locate subsequent rows

#summarize mean values
df.groupby(['sepal width (cm)']).mean()

```


## Connecting R and Python

```
library(reticulate)

```

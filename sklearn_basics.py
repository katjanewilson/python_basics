## load data
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

#load dataset

from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
data = iris.data
column_names = iris.feature_names
column_names
df = pd.DataFrame(data, columns = column_names)
df

#training and testing
X = df['sepal length (cm)'].values.reshape(-1,1)
y = df['sepal width (cm)'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm
#intercept
print(regressor.intercept_)
#slope
print(regressor.coef_)

#testing
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df

#evaluation
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

### for multiple regression

X = df[['sepal width (cm)', 'sepal length (cm)']].values













##example with Boston housing data set

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston

boston = load_boston()
boston
##put this into a dataframe
df_x = pd.DataFrame(boston.data, columns= boston.feature_names)
df_y = pd.DataFrame(boston.target)

df_x.describe() ##

reg = linear_model.LinearRegression()
#split into training and testing data

x_train,x_test,y_train,y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=4) #splits it into .8 and .2

reg.fit(x_train,y_train)
reg.coef_ ##this gives us the regression weights, and this is linear regression so each coefficient has a weight

##now predict
a= reg.predict(x_test)
a[0] ##this gives a prediction

y_test[0] #there is some error
a[1]
y_test ##s

###mean square error
np.mean((a-y_test) **2)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

#examine to dataframe structure
print(df.head())
print(df.columns)

#construct a df that groups the total production of honey by year
production_per_year = df.groupby('year').totalprod.sum().reset_index()


#restoring columns in the dataset
x = production_per_year.year
y = production_per_year.totalprod

#reshaing the column year into the right format. 2D arrary
x=x.values.reshape(-1,1)

#creating a scatterplot for y
plt.scatter(x,y)
#plt.show()        #made it as comment since plt.show() is used later in the code

#creating a linear regression mondel from scikit-learn
lr_model = LinearRegression()
lr_model.fit(x,y)
slope = lr_model.coef_
intercept = lr_model.intercept_
y_predict = lr_model.predict(x)

#scatterplot for y_predcit 
plt.scatter(x,y_predict)
plt.show()

#So, it looks like the production of honey has been in decline, according to this linear model. 
#Let’s predict what the year 2050 may look like in terms of honey production.

#creating a Numpy array for 2013-2050 and reshaping it for scikit-learn
X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)

#using linear model to predict the values in 2013-2050
future_predict = lr_model.predict(X_future)

#plot the future predict on a different plot
plt.plot(X_future, future_predict)
plt.show()

#as we can see from the plot, its in the negatives
#meaning that as this rate, our production will be 0 at 2040, unless we get a new set of data stating otherwise.
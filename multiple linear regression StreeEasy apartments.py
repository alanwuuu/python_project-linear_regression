#StreetEasy Dataset
#multiple independent variables linear regression model

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#create dataframe 
StreetEasy = pd.read_csv('https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/streeteasy.csv')
df = pd.DataFrame(StreetEasy)


#creating x and y dfs 
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = df[['rent']]

#train_text_split 80/20
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

#creating the multiple linear regression model
mlr = LinearRegression()
mlr.fit(x_train,y_train)
y_predict = mlr.predict(x_test)   #returns all the apartments' estimated rent in the 20%

#example: John want to estimate how much his apartment should be
#so has the his values for each column stored in j
j = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 1]]    #made the data into a 2D for formatting purpose
j_predict = mlr.predict(j)
#print(j_predict)
#therefore, $2172 should a guide line for John to value his apartment

#now, we will use a 2D scatter plot to visiualize the actual rent vs the predicted rent
plt.scatter(y_test,y_predict,alpha=.5)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")
plt.show()

#it might be helpful for us to know the coeffcient of our mlr equation
coef_list = mlr.coef_
#print(coef_list)

#we can see the correaltion between the rent and each variable in our mlr equation 
#we will use scatter plot to determine the positive/negative linear relations between the two
temp_x = x['size_sqft']     #view different correlations by change the column, the value inside of the []
plt.scatter(temp_x,y,alpha=.5)
plt.show()

#since now we have our mlr
#we will test our model's accuracy using Residual Analysis
#NOTE: R² is the percentage variation in y explained by all the x variables together.
#For example, say we are trying to predict rent based on the size_sqft and the bedrooms in the apartment and the R² for our model is 0.72 — that means that all the x variables (square feet and number of bedrooms) together explain 72% variation in y (rent).
#Now let’s say we add another x variable, building’s age, to our model. By adding this third relevant x variable, the R² is expected to go up. Let say the new R² is 0.95. 
#This means that square feet, number of bedrooms and age of the building together explain 95% of the variation in the rent.
#The best possible R² is 1.00 (and it can be negative because the model can be arbitrarily worse). Usually, a R² of 0.70 is considered good.
#BUT we will use .score() in sklearn_linear_model
r2_train = mlr.score(x_train,y_train)
r2_test = mlr.score(x_test,y_test)

#our r2_train and r2_test are used to see if the model has learned the coefficients correctly
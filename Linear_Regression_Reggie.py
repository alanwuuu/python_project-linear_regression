#Creator: Alan Wu
#Contact Info: alanwu379@gmail.com
#Senior studying Mathematics at CUNY Baruch


#Project: Linear Regression

# info:
    #Reggie is a mad scientist who has been hired by the local fast food joint to build their newest ball pit in the play area. 
    #He is working on researching the bounciness of different balls so as to optimize the pit. 
    #He is running an experiment to bounce different sizes of bouncy balls, and then fitting lines to the data points he records. 
    #He has heard of linear regression, but needs your help to implement a version of linear regression in Python.

# Note: 
    #Linear Regression is when you have a group of points on a graph, and you find a line that approximately resembles that group of points.
    #A good Linear Regression algorithm minimizes the _error_, or the distance from each point to the line. 
    #A line with the least error is the line that fits the data the best. We call this a line of best fit.

#-----------------------
#lets start with creating a function for finding y in a linear equation  
#where m is the slope of the line and b is the y-intercept of the line 

def linear_function(m, b, x):
  y = m*x + b
  return y

#lets test out our function to see if the output matches with our calculation bu hand (Remove the # below and both should return True)
#print(linear_function(1, 0, 7) == 7)
#print(linear_function(5, 10, 3) == 25)     

#-----------------------
#so the Scientist Reggie wants to try out different m values and b values for linear_function to see which line produces the least error
#so to calculate the error between a point and a line
    #We will create the function called: calculate_error(m,b,point)
        #Where m is the slope, b is the y-intercept, and the point that contains a pair of x and y
        #The function should return the distance between the line and the point

def calculate_error(m,b,point):
    x, y = point                   #once we have point, we will seperate the list into two distinct variables, x and y
    y_1 = linear_function(m,b,x)   #using the linear function to generate y-value of the line
    distance = abs(y-y_1)          #using the distance to measure the difference between y and y_1 
    return distance 

#the point (3, 3) should be 1 unit away from the line y = x - 1:
#remove the # to test out the result
#print(calculate_error(1, -1, (3, 3)))

#----------------------
#Reggie's datasets are sets of points
    #where x represents the size of the bouncy ball (in cm) and y represents the distance that it bounced (in m)
    #for example: (1,2) represents a 1 cm bouncy ball bounced 2 meters

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#So when we are given a set of data, we have no idea what the m and b we should use for our linear function
#We will start by finding out the total error for the dataset when we just input any m and b
#We will create a function called calculate_all_error with 3 arugements: m,b,datapoints

def calculate_all_error(m,b,datapoints):
    total_error = 0                              #we havent start the calculation yet, so there is no total error so far
    for point in datapoints:                     #at each iteration, point will be the most left element/point in the datapoints list
        point_error = calculate_error(m,b,point) #store the error for each point into point error
        total_error += point_error               #adding errors for each point/element in the datapoint/list
    return total_error                           #Note: return should be outside of the for loop, since you want the total error after the loop iterates through the whole list

#code testing#
    #every point in this dataset is 1 unit away from y = x - 1
    #so the total error should be 4:
    #remove # to test code. NOTE: in this testing, datapoints is reassigned a dataset
#datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
#print(calculate_all_error(1, -1, datapoints))

#----------------------
#so now we have all the tools we need to find out the best m and best b for our linear regression model that will minimizes the total error of our dataset
#so lets set boundaries for our m and b (this could change depending on our data set, but for now, we will use the following boundries)
    #let m be between -10 and 10 with as increment of 0.1
    #let b be between -20 and 20 with as increment of 0.1

possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]

smallest_error = float('inf')      #Used infinity because any error from the dataset will be smallet
                                   #So the first error found will be the smallest at the moment
                                   #We are dealing with decimals, so converted the type to float
best_m = 0                
best_b = 0                         #just giving them a value, which  will be replaced


for m in possible_ms:              #nested for loop for iterating through each m and b
    for b in possible_bs:          
        error = calculate_all_error(m,b,datapoints) #calculating the total error for dataset with given m and b
        if error < smallest_error:
            best_m = round(m,2)
            best_b = round(b,2)
            smallest_error = error
            smallest_error = round(smallest_error,2)
            
    
#print("Our linear function should have m as {} and b as {}. Which will give us a minimal error of {}.".format(best_m,best_b,smallest_error))

#There you have it, a linear regression model for Reggie
#Now, Reggie wants to predict the bounce height of a ball that is 6 cm 
#lets test out our hard work!!

#remove # to see result
#print("The ball will bounce this high {}m!".format(linear_function(best_m,best_b,6)))

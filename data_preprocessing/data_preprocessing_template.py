#importing Headers
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
from sklearn.impute import SimpleImputer


#logging
#logging.basicConfig(level=logging.INFO)

#importing the dataset
dataset = pd.read_csv('Data.csv')

print(type(dataset))

# extracting and storing the independent values and the dependent values separately using index locator
X = dataset.iloc[:, :-1].values
Y= dataset.iloc[:, -1].values

print("The data values for independent variables are \n", X)
print("The data values for independent variables are \n", Y)

#to specify what is to be done with missing values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

#to connect the imputer with the matrix of features
imputer.fit(X[:, 1:3])

#to finally transform the missing values with the mean values and update the independent values matrix
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)



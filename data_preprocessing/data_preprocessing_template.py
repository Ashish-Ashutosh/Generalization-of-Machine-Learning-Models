#importing Headers
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging

#logging
logging.basicConfig(level=logging.INFO)

#importing the dataset
dataset = pd.read_csv('Data.csv')

# extracting and storing the independent values and the dependent values separately using index locator
X = dataset.iloc[:, :-1].values
Y= dataset.iloc[:, -1].values

logging.info("The data values for independent variables are \n", X)
logging.info("The data values for independent variables are \n", Y)



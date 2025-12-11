#Importing libraries
#python library for numerical and scientific computing. pandas is built on top of numpy
import numpy as np 
#importing pandas
import pandas as pd


series = pd.Series(data = [78, 92, 36, 64, 89])  
series
series.values
series.index
series[1]

data = pd.Series(data = [700000, 800000, 1600000, 1800000, 30000000], index = ['Swift', 'Jazz', 'Civic', 'Altis', 'Gallardo'])
data
data['Swift']
data['Jazz': 'Gallardo']

#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
car_price

#Creating a car price series with a dictionary
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
# Creating the car manufacturer series with a dictionary
car_man_dict = {'Swift' : 'Maruti',
                  'Jazz'   : 'Honda',
                  'Civic'  : 'Honda',
                  'Altis'  : 'Toyota',
                   'Gallardo' : 'Lamborghini'}
car_man = pd.Series(car_man_dict)
print(car_price)
print(car_man)
cars = pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man})
cars
cars['Price']
#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
car_price
#Creating a DataFrame from car_price Series
pd.DataFrame(car_price, columns=['Car Price'])

data = [{'Name': 'Subodh', 'Marks': 28},
        {'Name': 'Ram', 'Marks': 27}, 
        {'Name': 'Abdul', 'Marks': 26}, 
        {'Name': 'John', 'Marks': 28}]
pd.DataFrame(data)

pd.DataFrame([{'Subodh':20, 'Ram':25},
              {'Abdul':29, 'John':24}], 
              index = ['Mathematics', 'Physics'])

#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
car_man_dict = {'Swift' : 'Maruti',
                  'Jazz'   : 'Honda',
                  'Civic'  : 'Honda',
                  'Altis'  : 'Toyota',
                   'Gallardo' : 'Lamborghini'}
car_man = pd.Series(car_man_dict)
cars = pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man})
cars

data_json = pd.read_json('example.json',)
data_json



marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
marks_df
marks_df['Total'] = marks_df['Chemistry'] + marks_df['Physics'] + marks_df['Mathematics'] + marks_df['English']
marks_df
marks_df.drop(columns = 'Total', inplace = True)


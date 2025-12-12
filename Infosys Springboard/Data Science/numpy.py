import numpy as np

item_list = ['Bread', 'Milk', 'Eggs', 'Butter', 'Cocoa']
student_marks = [78, 47, 96, 55, 34]
hetero_list =  [ 1,2,3.0, ‘text’, True, 3+2j ]

student_marks = [78, 47, 96, 55, 34]
for i in range(len(student_marks)):
    student_marks[i]+=5
print(student_marks)

student_marks_arr = np.array([78, 92, 36, 64, 89])
print(np.sum(student_marks_arr))
additional_marks = [2, 2, 5, 10, 1]
student_marks_arr += additional_marks
student_marks_arr
student_marks_arr = np.array([78, 92, 36, 64, 89])
student_marks_arr = np.add(student_marks_arr, additional_marks)
student_marks_arr



#creating an array of cars
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
#accessing the second car from the array
cars[1]

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
car_hp_arr

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing car names
car_hp_arr[0]

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing horsepower
car_hp_arr[1]

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing second car - 0 represents 1st row and 1 represents 2nd element of the row
car_hp_arr[0,1]


#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing name of last car using negative indexing
car_hp_arr[0,-1]


#creating an array of cars
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
#accessing a subset of cars from the array
cars[1:4]
#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])
car_hp_acc_arr
#Accessing name and horsepower 
car_hp_acc_arr[0:2]
#Accessing name and horsepower of last two cars 
car_hp_acc_arr[0:2, 3:5]
#Accessing name, horsepower and acceleration of first three cars
car_hp_acc_arr[0:3, 0:3]


#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#mean horsepower
print("Mean horsepower = ",np.mean(horsepower_arr))


#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#median horsepower
print("Median horsepower = ",np.median(horsepower_arr))

print("Minimum horsepower: ", np.min(horsepower_arr))
print("Maximum horsepower: ", np.max(horsepower_arr))
print("Index of Minimum horsepower: ", np.argmin(horsepower_arr))
print("Index of Maximum horsepower: ", np.argmax(horsepower_arr))


#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
x = np.where(horsepower_arr >= 150)
print(x) # gives the indices 
# With the indices , we can find those values 
horsepower_arr[x]


#Importing path and skimage i/o library 
import os.path
from skimage.io import imread
from skimage import data_dir
#reading the astronaut image
img = imread(os.path.join(data_dir, 'astronaut.png'))

#Using matplotlib.pyplot to visualize the image 
import matplotlib.pyplot as plt
plt.imshow(img)

#Importing path and skimage i/o library 
import os.path
from skimage.io import imread
from skimage import data_dir
#reading the astronaut image
img = imread(os.path.join(data_dir, 'astronaut.png'))
#Slicing out the rocket 
img_slice = img.copy()
img_slice = img_slice[0:300,360:480]
plt.figure()
plt.imshow(img_slice)

img[0:300,360:480,:] = 0
plt.imshow(img)


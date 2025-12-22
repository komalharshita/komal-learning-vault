# Input
lst = [5, 10, 0, 200]
# Expected Output:
# [10, 15, 5, 205]  

# Input
lst = [1, 2, 3, 'text', True, 3+2j]
# Expected output:
# A pure homogeneous vector, all 6 elements converted into a single datatype. 

 # Input
lst = [56, 45, 12, 6] 
# Expected output:
# 16 

 
arr = np.array([2,5,6,8], dtype = int)
print(arr)
# [2 5 6 8]
print(type(arr))
# class 'numpy.ndarray'
print(np.result_type(arr))
# int32 
 
 
''' Creation of an array with step size 1.33 between 0 - 10 '''
print(np.arange(0, 10, 1.33, dtype = np.float64))
# [ 0.    1.33  2.66  3.99  5.32  6.65  7.98  9.31]
# arange() gives uncertain number of values based on steps
# Hence, we use linspace, which asks for total number of values 
''' Creation of an array with total 5 values between 0 - 160 '''
print(np.linspace(0, 160, 5, dtype = np.float64))
# [   0.   40.   80.  120.  160.] 

 
S_X = np.array([[2, 5, 6, 5],
               [4, 8, 6, 5]])
print(S_X)
# [[2 5 6 5]
#  [4 8 6 5]]
S_Y = np.array([[6, 7, 5, 9],
               [7, 5, 6, 4]])
print(S_Y)
# [[6 7 5 9]
#  [7 5 6 4]] 
 
 
print(S_Y - S_X)
# [[ 4  2 -1  4]
#  [ 3 -3  0 -1]] 
 

 
 ''' Method 1 '''
print(S_X < 2)
# [[False False False False]
#  [False False False False]]
''' Method 2 '''
twos_mat = np.ones((2, 4)) * 2
print(np.less(S_Y, twos_mat))
# [[False False False False]
#  [False False False False]] 
 

 
import os.path
from skimage.io import imread
from skimage import data_dir
img = imread(os.path.join(data_dir, 'checker_bilevel.png'))
 
 
''' Image stored as numpy object (2D Matrix) '''
print(type(img))        # <class 'numpy.ndarray'>
''' Number of image dimensions '''
print(img.ndim)         # 2
''' Shape of the image (rows, columns) '''
print(img.shape)        # (10, 10)
''' Number of total elements in the image '''
print(img.size)         # 100 
''' Size of per element (in bytes) '''
print(img.itemsize)     # 1
''' Size of complete image (in bytes) '''
print(img.nbytes)       # 100
 
''' assuming you have read the image in variable img '''
# Transpose
img_t = img.T
# Reshape
img_reshape = img.reshape(5, 20)
# Sort
img_srt = img.copy()
img_srt.sort(axis = 0) 
# Compression
img_cmp = img.copy()
img_cmp = img_cmp.compress([True,False,True,0,1,1,1,0,0,1],axis = 0)
print(img_cmp.shape)
 
 
import matplotlib.pyplot as plt
plt.imshow(img, cmap = 'Greys') # Pass above used image names in place of 'img' to visualize
 

"""
Summary
The following table lists the commonly used methods and attributes involved in NumPy:

 
Method	                      Definition
array()	          Creation of a nd-array
arrange()	        Creation of a nd-array with step-size as one of the argument
linspace()	      Creation of a nd-array with number od values as one of the argument
reshape()	        Changing a nd-array into new-shape
copy()	          Creates of new nd-array without altering the original nd-array
hssplit()	        Splits a nd-array horizontally
vsplit()	        Splits a nd-array vertically
hstack()	        Merge a nd-array horizontally
vstack()	        Merge a nd-array into vertically
 

 

Attribute	                        Definition
shape	                        Returns the shape(number of rows and columns) of a nd-array
size	                        Returns the number of elements of a nd-array
T	                            Transpose of a nd-array

"""

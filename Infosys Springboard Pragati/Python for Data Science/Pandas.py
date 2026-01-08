import pandas as pd

# 1. Using list of dictionary
lst = [{"C1": 1, "C2": 2},
        {"C1": 5, "C2": 10, "C3": 20}]
# Observe NaN       
print(pd.DataFrame(lst, index = ["R1", "R2"]))
#     C1  C2    C3
# R1   1   2   NaN
# R2   5  10  20.0
# 2. Using dictionary
dc = {"C1": ["1", "3"],
        "C2": ["2","4"]}
print( pd.DataFrame(dc, index = ["R1", "R2"]) )
#    C1 C2
# R1  1  2
# R2  3  4
# 3. Using list
lst = [[52,32],[45,85]]
print(pd.DataFrame(lst, index = list('pq'), columns = list('ab')))
#     a   b
# p  52  32
# q  45  85
  
              
df = pd.DataFrame({'A': [10., 20.],
                    'B': "text",
                    'C': [2,60],
                    'D': 3+9j})
print(df)
#       A     B   C       D
# 0  10.0  text   2  (3+9j)
# 1  20.0  text  60  (3+9j)
print(df.dtypes)
# A       float64
# B        object
# C         int64
# D    complex128
# dtype: object 

print(df.info())
# < class 'pandas.core.frame.DataFrame' >
# RangeIndex: 2 entries, 0 to 1
# Data columns (total 4 columns):
# A    2 non-null float64
# B    2 non-null object
# C    2 non-null int64
# D    2 non-null complex128
# dtypes: complex128(1), float64(1), int64(1), object(1)
# memory usage: 160.0+ bytes 


print((df.index))   #index of rows
# RangeIndex(start=0, stop=2, step=1)
print(df.columns)   # index of columns
# Index(['A', 'B', 'C', 'D'], dtype='object')
print(df.values)    # display values of df
# [[10.0 'text' 2 (3+9j)]
#  [20.0 'text' 60 (3+9j)]]

df = pd.DataFrame([[11, 202],
                    [33, 44]],
                    index = list('AB'),
                    columns = list('CD'))
''' Writing to excel file '''
df.to_excel('test_file.xlsx', sheet_name = 'Sheet1')
''' Reading from excel file '''
print(pd.read_excel('test_file.xlsx', 'Sheet1')) 
 
df = pd.read_table('chat.txt') 
print(df.head(5)) 
          

''' Input '''
0  26/08/17, 12:36:23 PM: Friend1: *Richard M. St...                                        
1         *discovered the malfunction the hard way.*                                        
2                                        #Incredible                                        
''' Expected Output '''
0 26/08/17, 12:36:23 PM: Friend1: *Richard M. Stallman, a staff ... hard way.* #Incredible 
              
df = df.iloc[:,0].str.split('M:', 1, expand=True)
ts = df.iloc[:,0].copy()
ts = ts.reset_index(drop = True)
ts.columns = ['Timestamp']
df = df.iloc[:,1].str.split(':', 1, expand=True)
df = df.reset_index(drop = True)
df.columns = ['Name','Convo'] 
              
''' for unicode use -> r'12345\xa045555' '''
df['Name'][df['Name'].str.contains(r'12345 45555')] = ' Friend8'
df['Name'][df['Name'].str.contains(r'98765 12222')] = ' Friend9' 

df = df[df['Name'].str.contains(r'\d{2} \d{5} \d{5}') == False] 
              

df = df[df['Convo'].str.contains(r'image omitted') == False]
df = df[df['Convo'].str.contains(r'video omitted') == False]
df = df[df['Convo'].str.contains(r'GIF omitted') == False]
df = df.reset_index(drop = True) 
              

data1 = pd.DataFrame([[15, 12, -3],
                    [33, 54, 21],
                    [10, 32, 22]],
                    columns = list('ABC'))
data2 = pd.DataFrame([[10, 1, 3],
                    [33, -54, 2],
                    [10, 0.32, 2]],
                    columns = list('DEF'))
print(data1)
#     A   B   C
# 0  15  12  -3
# 1  33  54  21
# 2  10  32  22
print(data2)
#     D      E  F
# 0  10   1.00  3
# 1  33 -54.00  2
# 2  10   0.32  2
print(pd.concat( [data1,data2], axis = 1 ))
#     A   B   C   D      E  F
# 0  15  12  -3  10   1.00  3
# 1  33  54  21  33 -54.00  2
# 2  10  32  22  10   0.32  2
 

data1 = pd.DataFrame(np.random.randn(9).reshape(3,3),
                   columns = list('ABC'))
data2 = pd.DataFrame(np.arange(9).reshape(3,3),
                   columns = list('ABC'))
print(data1)     # Random values
#           A         B         C
# 0  1.957218  0.433266  1.214950
# 1 -0.143500 -0.092030 -0.823898
# 2  0.481486 -0.024111 -0.769195
print(data2)
#    A  B  C
# 0  0  1  2
# 1  3  4  5
# 2  6  7  8
print(pd.concat( [data1,data2], axis = 0 ))
#           A         B         C
# 0  1.957218  0.433266  1.214950
# 1 -0.143500 -0.092030 -0.823898
# 2  0.481486 -0.024111 -0.769195
# 0  0.000000  1.000000  2.000000
# 1  3.000000  4.000000  5.000000
# 2  6.000000  7.000000  8.000000 

df = pd.DataFrame([
            ['IND', 'Gold', 'Game1', '9.9'],
            ['IND', 'Bronze', 'Game2', '8'],
            ['USA', 'Silver', 'Game1', '9.5'],
            ['USA', 'Gold', 'Game2', '8.6'],
            ], columns = ['Country', 'Medal', 
                'Game', 'Score'],
                index = ['Year1', 'Year2','Year1', 'Year2'])
                  
print(df)  
#       Country   Medal   Game Score
# Year1     IND    Gold  Game1   9.9
# Year2     IND  Bronze  Game2     8
# Year1     USA  Silver  Game1   9.5
# Year2     USA    Gold  Game2   8.6 

# Listing all the features
print(df.pivot(index = 'Country', columns = 'Medal'))
#           Game                Score            
# Medal   Bronze   Gold Silver Bronze Gold Silver
# Country                                        
# IND      Game2  Game1   None      8  9.9   None
# USA       None  Game2  Game1   None  8.6    9.5
# Listing only Score feature
print(df.pivot(index = 'Country', columns = 'Medal',
               values = 'Score')) 
# Medal   Bronze Gold Silver
# Country                   
# IND          8  9.9   None
# USA       None  8.6    9.5 


df = pd.DataFrame([["Laptop", 1000],
                   ["Laptop", 2520],
                   ["Desktop", 3000],
                   ["Desktop", 400]], columns = ['Category','Sales'])
print(df)
#   Category  Sales
# 0   Laptop   1000
# 1   Laptop   2520
# 2  Desktop   3000
# 3  Desktop    400
print(df.groupby(['Category'], sort = False).sum())
#           Sales
# Category       
# Laptop     3520
# Desktop    3400 


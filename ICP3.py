import numpy as np
#a)
table = np.random.random(15)
table = table * 19 + 1
#reshape the array to 3x5
shapedTable = table.reshape(3, 5)
#print array shape
print(shapedTable.shape)
print(shapedTable)
#replace each max value in each row with 0
shapedTable[np.arange(len(shapedTable)), shapedTable.argmax(1)] = 0
print(shapedTable)
#create a 2 dimentional array of size 4x3 with 4 byte integer elements
arr = np.zeros((4, 3), dtype = np.int32)
print(arr.shape)
print(type(arr))
print(arr.dtype)

#b)
A = np.array([[3, -2],[1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

#c)
#compute the sum of the diagonal element of a given array
q3Array = np.array([[0, 1, 2], [3, 4, 5]])
print(q3Array)
trace = np.trace(q3Array)
print("sum: ", end = '')
print(trace)

#d)
newShapeArr = np.array([[1, 2], [3, 4], [5, 6]])
newShapeArr.reshape(2, 3)
print(newShapeArr)

#part B
import pandas as pd

#1 Read the provided CSV file ‘data.csv’.
data = ("C:\\Users\\anori\\Downloads\\data.csv")
df = pd.read_csv(data)
print(df)

#2 Show the basic statistical description about the data.

print(df.describe())

# print(table[10:25])
#3Check if the data has null values.

mean_calories = df["Calories"].mean()
mean_duration = df["Duration"].mean()
mean_pulse = df["Pulse"].mean()
mean_maxPulse = df["Maxpulse"].mean()
#3a. Replace the null values with the mean
df["Calories"].fillna(value = mean_calories, inplace = True)
df["Duration"].fillna(value = mean_duration, inplace = True)
df["Pulse"].fillna(value = mean_pulse, inplace = True)
df["Maxpulse"].fillna(value = mean_maxPulse, inplace = True)


#4 print Select at least two columns and aggregate the data using: min, max, count, mean.
#.agg function
result = df.groupby("Pulse").agg({"Duration" : ['mean', 'min', 'max']})
print(result)

#5 filter the dataframe to select the rows with calories >500 and pulse <100
filter_cal = df.loc[(df["Calories"] > 500) & (df["Calories"] < 1000)]
print(filter_cal)

#6 filter select rows with calories
filter_Cal_pulse = df.loc[(df["Calories"] > 500) & (df["Pulse"] < 100)]
print(filter_Cal_pulse)

#7create new df_modified with all data fields except for Maxpulse
# df_modified = df['Duration', 'Pulse', 'Calories'].copy()
df_modified = pd.DataFrame().assign(Duration = df["Duration"], Pulse = df["Pulse"], Calories = df["Calories"])
print(df_modified)
#8 delete Maxpulse from original df
del df["Maxpulse"]

#9 convert calories to int
df["Calories"] = df["Calories"].astype(int)
print(df)
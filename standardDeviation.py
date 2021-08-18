import pandas as pd
import math


df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

sum = 0

for g in data:
    sum = sum + g


number = len(data)

average = sum/number

#to calculate the difference of all heights from mean

differences = []
for u in data:
    differences.append(u - average)
 
squared_Differences = []
for s in differences:
    squared_Differences.append(s*s)

sum_squaredDifferences = 0
 
for t in squared_Differences: 
    sum - sum+t


variants = sum/number
standard_deviation = math.sqrt(variants)
print(standard_deviation)

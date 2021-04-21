#Import NumPy library
import numpy as np
import csv
#Instantiate an array of size 5 with random values of between 30,000 and 100,000
a = np.random.randint(30000, 100000, (5), dtype=int)
print(a)
user = input("Enter the percentage of raise: ")
print("Total payroll after " + user + "% raise... ")
#Typecast user to int
user = int(user)
user = user / 100
#Calculate raise
a = a + (a * user)
user = str(user)
print(a)

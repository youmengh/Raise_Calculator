#Import NumPy library
import numpy as np
import csv
csv_file = open('employee_salaries_1.csv')
csv_data = csv.reader(csv_file)
salaries = list(csv_data)
a = np.array(salaries).flatten().astype('int32')
# Instantiate an array of size 5 with random values of between 30,000 and 100,000
print("Current payroll:\n" + str(a))                        # prints the payroll
print("Pre-raise total:   $ " + str(np.sum(a)))             # prints the pre-raise payroll
user = input("Enter the percentage of raise: ")
print("Raise:   " + user + "%")
user = int(user)                                            # Typecast user to int
user = user / 100
a = a + (a * user)                                          # Calculate raise
print("Post-raise total:  $ " + str(np.sum(a)))
print("Post-raise payroll:\n" + str(a))

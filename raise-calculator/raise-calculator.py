# import libraries
import numpy as np
import csv

print("\nWelcome to Raise Calculator")
print("\nBefore proceeding:")
print("1.\tEnsure that your employees' compensations are stored in one singular column")
print("\tas shown in the example file \"employees_pay.csv\".")
print("2.\tSave compensations file under the name \"employees_pay.csv\"")
print("\tand store it in the same directory as \"raise-calculator.py\".")

again = input("\nEnter \"yes\" to begin or any other character to quit: ").strip().lower()


def run():
    # read and parse employees_pay.csv
    csv_file = open('employees_pay.csv')
    csv_data = csv.reader(csv_file)

    compensations = list(csv_data)  # list of compensations (payroll)
    a = np.array(compensations).flatten().astype('float64')  # turn list to array of compensations

    print("Current payroll:\n" + str(a))  # print the array of payroll
    print("\nTotal compensation: $" + str(np.sum(a)) + "\n")  # print the total cost of compensations prior to raise

    user = input("Enter the desired percentage raise: ")  # prompt user to enter the desired raise
    print("Raise: " + user + "%")

    # typecast raise percentage to float and convert percentage for calculation
    user = float(user) / 100
    a = a + (a * user)  # calculate post-raise payroll

    # print results
    print("\nPost-raise payroll:\n" + str(a))
    print("\nTotal compensation: $" + str(np.sum(a)))

    # save results
    post_raise = np.reshape(a, (-1, 1))  # convert to 2D array with 1 column write to csv
    # write to csv using new 2D array
    # save results to employees_pay_raise.csv
    with open('employees_pay_post_raise.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(post_raise)

    print("\nRaise calculated...\nResults are saved to the following file: \"employees_pay_post_raise.csv\"")


# loop program
while again == "yes":
    run()
    again = input("\nEnter \"yes\" to begin or any other character to quit: ").strip().lower()


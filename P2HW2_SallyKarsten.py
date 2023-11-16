#Karsten Sally
#11/16/23
#Getting sun and average using mathematical expressions

from statistics import mean

#Get imput form user
Module1 = float(input("Enter grade for Module 1:"))
Module2 = float(input("Enter grade for Module 2:"))
Module3 = float(input("Enter grade for Module 3:"))
Module4 = float(input("Enter grade for Module 4:"))
Module5 = float(input("Enter grade for Module 5:"))
Module6 = float(input("Enter grade for Module 6:"))

#Create an empty list
num_list =[]

#Add value to to list
num_list.append(Module1)
num_list.append(Module2)
num_list.append(Module3)
num_list.append(Module4)
num_list.append(Module5)
num_list.append(Module6)

#Print list to ensure values are listed
print(num_list)

#Call method on the list to get sum and average
list_sum = sum(num_list)
list_avg = mean(num_list)
list_max = max(num_list)
list_min = min(num_list)

#add value to the list
print("--------Results--------")
print(f"Lowest Grade {list_min:.2f}")
print(f"Highest Grade {list_max:.2f}")
print(f"Sum of grades {list_sum:.2f}")
print(f"Average {list_avg:.2f}")

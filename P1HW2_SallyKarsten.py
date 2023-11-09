#Karsten Sally
#11/9/23
#Using strings and Integers to perform math

budget = int(input("Enter a Budget:"))

destination = (input("Enter travel Destination:"))

gas = int(input("How much do you think you will spend on gas?"))

accomodation = int(input("Approximately, how much will you need for accmodation/ hotel?"))

food =int(input("Last, how much do you need for food?"))

print("--------Travel Expenses--------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accomodation:", accomodation)
print("Food:", food)
print("Remaining Balance:", (budget - gas - accomodation - food))


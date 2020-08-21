cars = 100 # integer assignment
space_in_a_car = 4.0 # float assignment
drivers = 30 # integer assignment
passengers = 90 # integer assignment
cars_not_driven = cars - drivers    # Integer value assign to an integer
cars_driven = drivers   # Integer Assignment
carpool_capacity = cars_driven * space_in_a_car     # integer multiply with float and assign  
average_passengers_per_car = passengers / cars_driven # integer divide and gives float


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


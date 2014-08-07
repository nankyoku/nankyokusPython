# Exercise 4: Variables And Names

# The following line sets the value of cars to be 100. 
cars = 100

# The following line sets the value of space_in_a_car to be 4.0.
space_in_a_car = 4.0

# The following line sets the value of drivers to be 30.
drivers = 30

# The following line sets the value of passengers to be 90.
passengers = 90

# The following line sets the value of cars_not_driven to be equal to the value of cars minus  the value of drivers.
cars_not_driven = cars - drivers

# The following line sets the value of cars_driven to be equal to the value of drivers. 
cars_driven = drivers

# The following line sets the value of carpool_capacity to be equal to the value of cars_driven times the value of space_in_a_car.
carpool_capacity = cars_driven * space_in_a_car

# The following line sets the value of average_passengers_per_car to be equal to the value of passengers divided by the value of cars.
average_passengers_per_car = passengers / cars

# The following line prints some phrases and the number of cars available.
print "There are", cars, "cars available." 

# The following line prints some phrases and the number of drivers available. 
print "There are only", drivers, "drivers available."

# The following line prints some phrases and the number of cars not driven. 
print "There will be", cars_not_driven, "empty cars today."

# The following line prints some phrases and the total carpool capacity. 
print "We can transport", carpool_capacity, "people today."

# The following line prints some phrases and the number of passengers that we have. 
print "We have", passengers, "to carpool today."

# The following line prints some phrases and the average passengers per car. 
print "We need to put about", average_passengers_per_car, "in each car."

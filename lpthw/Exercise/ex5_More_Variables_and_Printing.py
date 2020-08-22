name = 'Abhishek Baliyan'
age = 26
height = 5.7
weight = 57
weight_in_pounds = weight * 2.20
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} foot tall.")
print(f"He's {weight} kg or {weight_in_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending on the food.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If i add {age}, {height} and {weight} I got {total}.")
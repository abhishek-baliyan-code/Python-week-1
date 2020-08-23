from sys import argv
script, first, second, third = argv
name = input("Your Name: ")

print(f"Hello, {name}.")
print("{}, You have 4 argv.".format(name))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("your third variable is:", third)
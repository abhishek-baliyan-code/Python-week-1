formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Mujay kuch karna hai",
    "Mujay kuch karna hai",
    "Martay dam tak karna hai",
    "Kartay rahna hai"
))
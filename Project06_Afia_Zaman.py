# Afia Zaman

# Take user input for size and sand character
sand_size = int(input("Please enter the size of the hourglass (1-5): "))

# Check and validate user input
while sand_size < 1 or sand_size > 5:
    print(f"Invalid input. Please try again: {sand_size}")
    sand_size = int(input("Please enter the size of the hourglass (1-5): "))
sand_char = input("Please enter the character for the hourglass: ")

# Print the top part of the hourglass
for x in range(sand_size, 0, -1):
    for y in range(sand_size - x):
        print(" ", end="")
    for y in range((x * 2) - 1):
        print(sand_char, end="")
    print()

# Print the bottom part of the hourglass
for x in range(2, sand_size + 1):
    for y in range(sand_size - x):
        print(" ", end="")
    for y in range((x * 2) - 1):
        print(sand_char, end="")
    print()

print()
print("create a butterfly pattern:")

# Print the top part of the butterfly
for x in range(sand_size):
    for y in range(x + 1):
        print(sand_char, end="")
    for y in range(sand_size * 2 - x * 2):
        print(" ", end="")
    for y in range(x + 1):
        print(sand_char, end="")
    print()

# Print the bottom part of the butterfly
for x in range(sand_size - 2, -1, -1):
    for y in range(x + 1):
        print(sand_char, end="")
    for y in range(sand_size * 2 - x * 2):
        print(" ", end="")
    for y in range(x + 1):
        print(sand_char, end="")
    print()

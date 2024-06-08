length = int(input("Length of the Row/Column: "))

# Lower triangular pattern
print("Lower triangular pattern:")
for row in range(length):
    for column in range(row + 1):
        print("* ", end="")
    print("\n")

# Upper triangular pattern
print("Upper triangular pattern:")
for row in range(length):
    for column in range(length - row):
        print("* ", end="")
    print("\n")

# Pyramid pattern
print("Pyramid pattern:")
for row in range(length):
    # Print leading spaces
    for column in range(length - row - 1):
        print(" ", end="")
    # Print stars
    for column in range(2 * row + 1):
        print("*", end="")
    print("\n")

#05_double_it
# Program to double a number until it is 100 or greater

# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Loop to double the number until it is 100 or greater
while curr_value < 100:
    curr_value = curr_value * 2  # Double the current value
    print(curr_value, end=" ")  # Print the doubled value on the same line

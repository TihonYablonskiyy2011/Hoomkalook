# Given three numbers
a = 10
b = 5
c = 8
 
# Find the smallest number using conditions
if a <= b and a <= c:
    smallest = a
elif b <= a and a <= c:
    smallest = b
else:
    smallest = c
 
# Print the result
print("Smallest number:", smallest)
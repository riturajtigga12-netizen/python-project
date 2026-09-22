# 1D Array in Python

# Create an array using a list
arr = [10, 20, 30, 40, 50]

# Display the array
print("Array:", arr)

# Access elements
print("First element:", arr[0])
print("Third element:", arr[2])

# Add an element
arr.append(60)
print("After adding:", arr)

# Change an element
arr[1] = 25
print("After updating:", arr)

# Delete an element
arr.remove(30)
print("After deleting:", arr)

# Display all elements using a loop
print("Array elements:")
for i in arr:
    print(i)
import random

# Generate 20 random marks between 0 and 100
marks = [random.randint(0, 100) for _ in range(20)]

# Create three separate lists based on the conditions
low_marks = [mark for mark in marks if mark <= 30]
mid_marks = [mark for mark in marks if 31 <= mark <= 69]
high_marks = [mark for mark in marks if mark >= 70]

# Display the original marks and the categorized lists
print("Original marks of 20 students:")
print(marks)

print("\nMarks <= 30:")
print(low_marks)

print("\nMarks between 31 and 69:")
print(mid_marks)

print("\nMarks >= 70:")
print(high_marks)

# Function to calculate the trace of a matrix
def calculate_trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# Input the size of the square matrix
n = int(input("Enter the size of the square matrix (n x n): "))

# Input the matrix elements
print(f"Enter the elements of the {n}x{n} matrix row by row (space-separated):")
matrix = []
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    if len(row) != n:
        print(f"Error: You must enter exactly {n} elements for this row.")
        exit()
    matrix.append(row)

# Display the matrix
print("\nThe entered matrix is:")
for row in matrix:
    print(row)

# Calculate and print the trace of the matrix
trace = calculate_trace(matrix)
print(f"\nThe trace of the matrix is: {trace}")

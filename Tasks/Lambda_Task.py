
# Function to convert numeric grade to letter grade
def To_Letter(Grade):
    if Grade >= 90:
        return "A"
    elif Grade >= 80:
        return "B"
    elif Grade >= 70:
        return "C"
    elif Grade >= 60:
        return "D"
    else:
        return "F"

# Input: List of grades (numerical)
Grades = [95, 85, 74, 63, 55, 88, 92, 70]
# Use map to apply 'To_Letter' function to each grade in the list
# The lambda here simply calls 'To_Letter' for each item
Letter_Grade = list(map(lambda G :To_Letter(G),Grades))

print("Numerical Grades:", Grades)
print("Letter Grades:", Letter_Grade)
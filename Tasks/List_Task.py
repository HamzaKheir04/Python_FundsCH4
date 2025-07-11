                                                    # List Example: Managing a to-do list
# Create a to-do list (mutable: can be updated)
ToDo = ["Checking","Finish Tasks", "Submitting"]  # Initial tasks
print("Original To-Do List:", ToDo)

# Adding tasks
ToDo.append("Communicate With The Team")  # Add a new task
print("\nAfter adding task by use 'append':", ToDo)
ToDo.insert(2, "See and Check The Emails")  # Insert a task at a specific position
print("\nAfter adding task by use 'insert':", ToDo)

# Sorting the list alphabetically
ToDo.sort()  # Sort the tasks in alphabetical order
print("After sorting alphabetically:", ToDo)

# Reversing the list
ToDo.reverse()  # Reverse the order of the list
print("After reversing the list:", ToDo)

# Removing tasks
ToDo.pop(0)  # Remove the first task using its index
print("\nAfter removing task by use 'pop':", ToDo)
ToDo.remove("See and Check The Emails")  # Remove a task by its value
print("\nAfter removing task by use 'remove':", ToDo)

# Deleting a range of tasks using `del`
del ToDo[1]  # Remove tasks index 1 
print("\nAfter deleting tasks ( index 1 ) :", ToDo)


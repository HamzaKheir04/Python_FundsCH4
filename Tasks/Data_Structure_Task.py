# Task1 : 
# Define a list of 6 items 
# and print the (number of items inside the list), (second element), (second last element) 
# and use slicing to print out (the second element until the third one).
List = [1,2,3,4,5,6]
print(f"The Number OF Item In The List : {len(List)} ",
      f"The Second Element : {List[1]} ",
      f"The Second Last Emement : {List[-2]}",
      f"the Second Element Until The Third One : {List[1:3]}"  #index 3 not Engaged 
      ,sep="\n")

#**************************************************************************************************************
# Task 2 :
# Define a list of numbers [1,2,3] 
# and then use append method to add 4 
# and use insert to add 5 at position 1 expected output [1,5,2,3,4]

Number = [1,2,3]
Number.append(4)
print(f"List After Append : {Number}")
Number.insert(1,5)
print(f"List After Insert : {Number}")

#**************************************************************************************************************

# Task 3 :
# You have the following nested list: nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


#1.  Access the number 5 from the nested list and assign it to a variable named number, print the variable number.
#2.  Append number 10 to the last list inside nested_list, Print the updated nested_list.

Listt = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Numberr = Listt[1][1]
print(f"The Number : {Numberr}")
Listt[2].append(10)
print(f"List After Append : {Listt}")


#**************************************************************************************************************

# Task 4 : 
# Create a tuple and print the last element

Tuple = (1,2,3,4,5,6)
print(f"The Last Element In The Tuple : {Tuple[-1]}")


#**************************************************************************************************************

#Task 5 : 

#    Create and Add Elements to a Set
#*   Create an empty set named my_set
#*   Add the elements 1, 2, and 3 to my_set
#*   Print the updated set

My_Set = set()
My_Set.add(1)
My_Set.add(2)
My_Set.add(3)
print(f"The Updated Set : {My_Set}")


#**************************************************************************************************************

#Task 6 :

#    Check element in a Set
#*   Create set named my_set with the elements 1, 2, 3, and 4
#*   Check if the element 2 is in my_set and print the result
#*   Check if the element 5 is in my_set and print the result
my_set ={1,2,3,4}
if 2 in my_set :
    print(2,", In The List :)")
else :  
    print(2," Not in the List :( ")  
if 5 in my_set :    
     print(5,", In The List :)")
else: 
    print(5,", Not in the List :( ")    

#**************************************************************************************************************
#Task 7 : 
"""""
* create 2 sets A , B
 --> A {'red' , 'blue' , 'green'}
 --> B {'red', 'pink' , 'yellow'}

 and apply the folowing

 * Apply union and print the result

 * Apply intersection and print the result

 * Apply difference and pring the result

 * Apply union and save the value on B set

 * delete all sets

"""
Set_A = {'red' , 'blue' , 'green'}
Set_B = {'red', 'pink' , 'yellow'}
print(f"The Union Between set A & B : {Set_A.union(Set_B)}",
      f"The intersection Between set A & B : {Set_A.intersection(Set_B)}",
      f"The difference Between set A & B : {Set_A.difference(Set_B)}",sep="\n")
Set_B = Set_A.union(Set_B)
del Set_A
del Set_B

#**************************************************************************************************************
#Task 8 :
# - Create a dictionary named student store his name, course , age with thier associated values
# - Use update function to edit the age, add another item (phone_number)
# - Delete the course key

Student = {"Name" :"Hamza", "Course" : "AI","Age" : 20}

Student.update({"Age" : 21,"Phone_Number" : "079"})

Student.pop("Course")

print(Student)




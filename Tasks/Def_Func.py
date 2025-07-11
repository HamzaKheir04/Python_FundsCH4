"""
                                                    Define a function to calculate total sales
This function calculates the total sales.
Parameters:
- book_price (float)  : The price of a single book.
- quantity_sold (int) : The number of books sold.

"""
def Sale(Price,Quantity):
    return(Price * Quantity)

print("Welcome To Our BookStore :) ")

Price = float(input("Enter the Price of The book : "))

Quantity = int(input("Enter the Number of books : "))

print(f"The Total Cost : {Sale(Price,Quantity):.2f}$")
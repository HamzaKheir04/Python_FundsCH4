"""
                                                    A cake Order Program
Process a cake order with optional details.

Parameters:
 - size (str) : The size of the cake (e.g., small, medium, large).
 - *Details   : Additional details about the cake (e.g., flavors or layers).
 - **Optional : Optional details for the order (e.g., drinks, delivery info, captain reward).
"""
def Cake_Order(Size , *Details,**Optional) :

    print(f"Order Details : ",
          f"- The Size Of The Cake : {Size}",sep="\n")
    if Details :
        print(f"- Some Details : ")
        for i,details in enumerate(Details):
            print(f"{i+1}- {details}")

    if Optional:
        i=1
        print(f"- Optional Details : ")
        for   options,Value in (Optional.items()):
            print(f"{i}- {options} : {Value}")
            i+=1



# Example usage of the function
Cake_Order("Medium", "Vanilla flavor", "Four layers", drinks="Mango Juice, Lemonade", delivery="Home Address: 123 Sweet Lane", captain_reward="10 USD")



    
    
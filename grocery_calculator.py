# Write a program that asks the user to input their grocery list
# and then tells them the price. You can make the following two
# assumptions:
# - the only available groceries are:
#       - bread: $3
#       - eggs: $6
#       - milk: $4
#       - butter: $2
# - users must enter one item at a time, even if they are buying
#   multiple
#       - e.g. if the user is buying three loaves of bread, they
#         will have to input 'bread' 3 times.
#
# If the user inputs something that is not one of the four options
# above, the program should print "The store doesn't have that" and
# then prompt the user for more input.
#
# When the user inputs an empty line (i.e. hits enter without typing
# anything), the program should print the total cost of their groceries.
#
# For example:
# Input grocery item:
# >> bread
# Input next grocery item:
# >> milk
# Input next grocery item
# >>
# Your total grocery bill is $7

def grocery_calculator():
   grocery_prices = {
       'bread': 3,
       'eggs': 6,
       'milk': 4,
       'butter': 2
    }
   total_cost = 0 
   while True:
        new_item = input("Input grocery item: ")
        item = new_item.lower()
        if item != '':
            item_cost = grocery_prices.get(item,0)
            if item_cost == 0:
                print("The store doesn't have that.")
            else:
                total_cost += item_cost
        else:
            print(f"Your total grocery bill is ${total_cost}")
            break

if __name__ == "__main__":
    grocery_calculator()
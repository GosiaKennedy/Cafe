#program calculates the total stock worth in the cafe

# creates menu list
menu = ["cake", "coffee", "tea", "panini"] 

# creates stock dictionary storing stock value for each item on the menu and price dictionary storing the price for each item on the menu
stock = {"cake": 10,
          "coffee": 5, 
          "tea": 5, 
          "panini": 6
          }
price = {"cake": 3, 
         "coffee": 2, 
         "tea": 1, 
         "panini": 5
         }

# set initial total stock value to 0
total_stock = 0

# loop through both dictionaries to obtain the value of each item and the total stock value
for item in price: 
    item_value = (stock[item]*price[item])
    total_stock = total_stock + item_value
print(f"The total stock worth of the cafe is £{total_stock}." )




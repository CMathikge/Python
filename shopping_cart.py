#Creat a shopping pragramme that will ask the uswer for food product and the price of the product
#Have an exit clause if the user wishes to stop adding more things to their cart
#At the end show the food items and the total cost all those product

foods =[]
prices=[]
total= 0

while True:
    food = input("Enter the food to buy or press q to quit: ")
    if food.lower() == 'q':
       break
    else:
        price = float(input(f"Enter the price fo the product{food}: R"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for food in foods:
        print (food, end=" ")
    
for price in prices:
        total = total + price 
    
print("\n")
    
print(f"Your total is: R{total}")
#https://theculturetrip.com/south-america/peru/articles/13-films-you-must-see-before-visiting-peru/
#1__________________________________________
print("Name: Dick Smith\n\nAddress: 120E, 87th Street, \n\t New York 10128.\nPhone: +440-995-5900\nMy College major is Object Oriented Programming System (OOPS)\n")

#2__________________________________________
sales = input("Insert projected ammount of sales: ")
sales = float(sales)
print(sales)

#3__________________________________________
mealCost = input("\nInsert the total cost of the meal: ")
mealCost = float(mealCost)
tip = round(mealCost * 0.15, 2)
salesTax = round(mealCost * 0.07, 2)
total = round(mealCost + tip + salesTax, 2)
print("Meal Cost: " + str(mealCost) + "\nTip: " + str(tip) + "\nSales Tax: " + str(salesTax) + "\nTotal: " + str(total))



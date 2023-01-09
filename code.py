#main function
def main():
    # welcome message
    print("\n\nWelcome to Arnold's Amazing Eats II\n\n")
    print("An online portal service for ordering yummy food at your door steps\n\n")

    # getting personal details as input
    print("Please enter your personal details\n\n")
    firstName = input("\nEnter your first name:\n")
    lastName = input("\nEnter your last name:\n")
    deliveryAddress = input("\nEnter your full delivery address (if not applicable leave it blank)\n")
    city = input("\nEnter your city\n")
    province = input("\nEnter your province\n")
    postalCode = input("\nEnter your postal code\n")
    splInstr = input("\nEnter special instructions for deliveries from this address\n")
    phone = int(input("\nEnter your phone number\n"))
    confirm = 'n' # predefining confirm variable so that while loop runs for first time
    quantity = 0

    # confirmation promt
    # loop will run until Y or y is entered
    while(confirm == 'n' or confirm == 'N'):

        # printing the selected options
        print("\nPlease select a meal from the following\n")
        print("\n1) Pizza\n")
        print("\n2) Pasta\n")
        choice = int(input("\nPlease enter your choice (1 or 2):\n"))
        quantity = int(input("\nPlease enter the quantity of selected meal\n"))
        if choice == 1:
            meal = "Pizza"
        elif choice == 2:
            meal = "Pasta"
        print("\n\nMeal: ", meal)
        print("\nQuantity: ", quantity)
        print("\n\nPlease confirm the order\n")
        confirm = input("\nEnter 'y' or 'Y' for Yes else enter 'n' or 'N' for no\n")

        # prices for both the meals
        price1 = 10
        price2 = 7
    
    # checking selected meal and setting the price in mealPrice variable accordingly 
    if(meal == "Pizza"):
        mealTotal = totalSum(price1, quantity)
        mealPrice = price1
    else:
        mealTotal = totalSum(price2, quantity)
        mealPrice = price2
    
    # calling dicount() function and storing result in totalDiscout variable
    totalDiscount = discount(mealTotal)

    # calculating price after discount
    finalTotal = mealTotal - (mealTotal*(totalDiscount/100))

    # calling printDetails() function to print the details
    printDetails(mealPrice, mealTotal, quantity, totalDiscount, finalTotal)

    # predefining isStudent variable so that while loop runs for the first time
    isStudent = 'z'

    # asking user if he is student or not
    # loop will run until user enters n or N or Y or y
    while isStudent != 'n' and isStudent != 'N' and isStudent != 'y' and isStudent != 'Y':
        isStudent = input("Are you a student? y or Y for yes, n or N for no:\n")
    
    # checking if user has entered no or yes and the storing it in student variable
    if isStudent == 'n' or isStudent == 'N':
        student = 'no'
    elif isStudent == 'y' or isStudent == 'Y':
        student = 'yes'

    # if user is student calculating price after student discount and tax
    # else calculating price only after tax
    if student == 'yes':

        #student discount
        studentTotal = (finalTotal - (finalTotal*0.1))

        #HST
        finalPrice = studentTotal + (studentTotal*0.13)
    
    else:

        #HST
        studentTotal = finalTotal
        finalPrice = studentTotal + (studentTotal*0.13)
    
    # printing reciept
    print("\n\n\t\tReciept\t\t\n")

    # printing personal information
    print(firstName + " " + lastName)
    print("\n" + deliveryAddress)
    print("\n" + city +", "+ province + ", " + postalCode)
    print("\n" + splInstr + "\n\n")

    # printing bill information
    print("\tItem \tItem\n")
    print("Order\tAmt\tPrice\tTotal\n")
    print("------\t------\t------\t---------\n")
    print(meal + "\t" + str(quantity) + "\t$" + str(mealPrice) + "\t$" + str(mealTotal) + "\n")

    #printing student discount if user is student
    if student == 'yes':
        print("10% student saving\t" + "-$" + str(mealTotal*(totalDiscount/100)) + "\n")

    # sub total
    print("\tSub Total\t$",finalTotal)

    # tax
    print("\n\tTax (13%)\t$" + str(round(studentTotal*0.13, 2)))
    print("\n\t\t\t---------\n")

    # final price
    print("\t\tTOTAL\t$" + str(round(finalPrice, 2)))
    print("\n")
    




# totalSum function with price and quantity as params
# this function will calculate total amount i.e. price * quantity
def totalSum(price, quantity):
    return price * quantity

# discount function with total as param
# this function will return discount according to some conditions
def discount(total):
    if total < 100:
        discountP = 5
    elif total > 100 and total < 500:
        discountP = 10
    else:
        discountP = 15
    return discountP

# printDetails function with price, total, quantity, discount, finalPrice as params
# this function will print the selected menu with price, quantity and discount and also print total amount
def printDetails(price, total, quantity, discount, finalPrice):
    print("\nItem\tPrice\tQuantity\tSubtotal\n")
    print("Item 1\t$" + str(price) + "\t* " + str(quantity) + "\t = $" + str(total))
    print("\n-----------------------------------\n")
    discountCost = total * (discount/100)
    print("Discount " + str(discount) + "% -$" + str(round(discountCost, 2)))
    print("\n-----------------------------------\n")
    print("GRAND TOTAL $" + str(round(finalPrice, 2)))


if _name=="main_":
    main()

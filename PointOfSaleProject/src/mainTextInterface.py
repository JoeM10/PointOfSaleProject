from datetime import datetime
import types.item as item

def main():
    currentTime = datetime.now()
    formattedCurrentTime = currentTime.strftime("%H:%M %d/%m/%Y")
    print("Welcome! The current time is: " + formattedCurrentTime)

    storeInventory = []

    initialize(storeInventory)

    while True:
        textInterface(storeInventory)

def initialize(storeInventory):
    inventoryFile = open("inventory.txt", "r")
    for line in inventoryFile:
        if "#" in line:
            continue
        splitLine = line.split(",")
        itemName = splitLine[0]
        itemCost = splitLine[1]
        itemQuantity = splitLine[2]

        itemToAdd = item.item(itemName, itemCost, itemQuantity)
        storeInventory.append(itemToAdd)

def textInterface(storeInventory):
    print("What would you like to do today?")
    #View inventory
    print("1. View inventory")
    #Update inventory
    print("2. Update inventory")
    #Sell items
    print("3. Sell items")
    #Set prices
    print("4. Set prices")
    #Money on hand
    print("5. Money on hand")
    #Deposit money
    print("6. Deposit money")
    #Total money earned
    print("7. Total money earned")
    #Save and close program
    print("8. Save and close program")

    userInput = int(input(""))
    
    if userInput == 1:
        print("Inventory")
        for product in storeInventory:
            print(product.getItemName(),
                product.getItemCost(), 
                product.getItemQuantity())

#    elif userInput == 2:
#        print("Update inventory")

#    elif userInput == 3:

#    elif userInput == 4:

#    elif userInput == 5:

#    elif userInput == 6:

#    elif userInput == 7:

    elif userInput == 8:
        exit()


#    else:
#        print("That is not a valid option. Please try again.")
#        continue

main()

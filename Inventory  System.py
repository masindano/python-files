'''
Masindano Masila
BSCIT-05-0133/2024
'''

#create an empty dictionary to store inventory items and their quantities
inventory = {}

#Loop too allow the user too enter multiple items
while True:
    # Ask user fo item name
    item = input("Enter item name(or 'exit' to stop): ")

    #stop the loop if user types 'exit'
    if item == "exit":
        break

    #Ask user for quantity of the item
    quantity = int(input("Enter quantity: "))

    #Add the item to inventory or update its quantity if ot already exists
    inventory[item] = inventory.get(item, 0) + quantity
#Ask the user to search for a specific item
    search = input("Enter item name to search: ")

#Display the quantity of the searched  item or a message if not found
    print("Quantity: ", inventory.get(search, "Item not found!!"))

#calculate and display the total quantity of all items in the inventory
    print("Total quantity of all items: ", sum(inventory.values()))
    

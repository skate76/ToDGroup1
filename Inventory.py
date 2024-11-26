

class Inventory:

    inventorylst = []

    def __init__(self, itemName, itemQnty):
        self.itemName = itemName
        self.itemQnty = itemQnty
        Inventory.inventorylst.append(self) # this will add the item to the long standing list of inventory items

    def display_inventory(self):
        for item in Inventory.inventorylst:
            print(f"Item: {item.itemName},Quantity:{item.itemQnty}")

    def update_inventory(self,itemName):# this is to directly change and set the amount, eg after restocking changing from 2 eggs to 12
        for item in Inventory.inventorylst:
            if item.itemName == itemName:
                qnty = input("Enter new quantity for the item: ")
                item.itemQnty = qnty

                
    def updateInvAuto(self,itemName,itemQuan):

        for item in Inventory.inventorylst:
            if item.itemName == itemName:
                
                item.itemQnty = item.itemQnty - itemQuan # so this will subtract the amout of a particular ingredient that would be used to fill an order from the existing amount; therfore updating/keeping track of amount of ingredients left
                 

    
   
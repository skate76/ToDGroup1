#from Recipe import Recipe
import random

class Order:

   orderslst=[]

    def __init__(self, custName, custNum,dessert,allergy):
        self.custName = custName
        self.custNum = custNum
        self.orderNum = None # will be unique to each order, acts as an identifier
        self.dessert = dessert
        #self.orderDetails[] = #Recipe.findRecipe(dessert)
        self.allergy = allergy # should be serperated my commas; if none then NONE would be writen down instead 
        self.status = "Pending" # This is always the default status when a order is made 
        orderConfirm()

    def orderConfirm(self):

        #for item in orderDetails:
            #itemname and itemquan should be taken from  the order  details 
            # then it will call updateInvAuto that will take the name and quan as parameters
            # that function will then subtract the quan from the existing quan of the item given
        updateInventory()
        self.orderNum = random.randint(1, 1000)
        Order.orderslst.append(self.custName,self.orderNum,self.dessert)
        print("Order has been Confirmed!")


   # takes the desserts name and searches the recipes and then find the recipe for that dessert and stores


    def updateInventory(self): # this will use each ingredient in order details and will subtract from the amount of inventory in stock 
        #if its unable to subtract then produce a error
    

    def manage_orderStatus(self,selected):
      #will activate once a order is choosen.will allow the user to change the status of the order to "started" or "completed"
    def manage_orderStatus(self):
        """Prompt the user to select a new status for the order."""
        status_options = ["Pending", "Processing", "Shipped", "Delivered", "Canceled"]
        print("Please choose a new status for this order:")
        
        # Display status options
        for idx, status in enumerate(status_options, 1):
            print(f"{idx}. {status}")

        # Get user's choice
        try:
            choice = int(input("Enter the number corresponding to the desired status: "))
            if 1 <= choice <= len(status_options):
                self.status = status_options[choice - 1]  # Update the order status
                print(f"Order status updated to: {self.status}")
            else:
                print("Invalid choice. Please select a valid status option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a status option.")
        
    
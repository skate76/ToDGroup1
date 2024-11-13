import getpass
import os

Cusernames = ["customer123"]
Cpasswords = ["customer123"]

Eusernames = ["employee123"]
Epasswords = ["employee123"]

Ousernames = ["KTAIT123"]
Opasswords = ["KTAIT123"]

inventory = [["cakes", 10],["cookies",10]]

def login():
    while True:
        print("Welcome! Please log in.")
        username = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password")
        if ((username in Eusernames) and (password in Epasswords)):
            emp_menu()
        elif ((username in Cusernames) and (password in Cpasswords)):
            cus_menu()
        elif ((username in Ousernames) and (password in Opasswords)):
            admin_menu()
        else:
            print("INVALID PASSWORD")
            print('')
            print("please try again")
            os.system('cls')
            login()

            
        


def admin_menu():
    while True:
        
        print("1. Add/Update Inventory")
        print("2. Generate Reports")
        print("3. Manage Staff")
        print("4. Exit")
        choice = int(input("Please Select A Function:"))
    
        if choice == 1:
            print ("Add/Update Inventory")
            os.system('cls')
            inventory_mgmt()
        elif choice == 2:
            print("Manage Staff")
            os.system('cls')
            staff_mgmt()
        elif choice == 3:
            print("Generate Reports")
            os.system('cls')
            generate_reports()
        elif choice == 4:
            print("Exiting......")
            os.system('cls')
            break 
        else:
            print("Invalid Choice. Please enter a number from 1 - 4")
            os.system('cls')
            admin_menu()
        
        
def cus_menu():
    while True:
        print("1. Make an Order")
        print("2. Display Inventory")
        print("3. Exit")
     

        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Make an Order")
            os.system('cls')
            make_order()
        elif choice == 2:
            print("Display Inventory")
            os.system('cls')
            display()
            
        elif choice == 3:
            print("Exiting....")
            os.system('cls')
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 3")
            os.system('cls')
            cus_menu()
        


def emp_menu():
    while True:
        print("1. Add/Update Inventory")
        print("2. Check in/Check out")
        print("3. Exit")
    
        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Add/Update Inventory")
            os.system('cls')
            inventory_mgmt()
        
        elif choice == 2:
            print("Check in/Check out")
            os.system('cls')
            chekin_menu()
            os.system('cls')
        elif choice == 3:
            print("Exiting....")
            os.system('cls')
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 3")
            os.system('cls')
            emp_menu()




def inventory_mgmt():
    while True:
        print("Welcome to the Inventory Manager")
        print('')
        print("1. Display inventory")
        print("2. Add New inventory")
        print("3. Update inventory")
        print("4. Remove inventory")
        print("5. Go Back")


        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Display")
            os.system('cls')
            display()
            break
        elif choice == 2:
            print("Add Inventory")
            os.system('cls')
            add_inventory()
        elif choice == 3:
            print("Update Inventory")
            os.system('cls')
            update_inventory()
        elif choice == 4:
            print("Remove Inventory")
            os.system('cls')
            remove_inventory()
        elif choice == 5:
            print("Exiting....")
            os.system('cls')
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 5")
            os.system('cls')
            inventory_mgmt()
        

        
    

def add_inventory():
    print("Welcome to the Inventory Manager")

def update_inventory():
    print("Welcome to the Inventory Manager")

def remove_inventory():
    print("Welcome to the Inventory Manager")

def display():
    print("")
    for i in inventory:
        print (i)
        print('')


def chekin_menu():
    while True:
        print("1. Checkin")
        print("2. Checkout")
        print("3. Exit")
     

        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Check in")
            os.system('cls')
            checkin()
        elif choice == 2:
            print("Checkout")
            os.system('cls')
            checkout()
            
        elif choice == 3:
            print("Exiting....")
            os.system('cls')
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 3")
            os.system('cls')
            chekin_menu()

def checkin():
    print("Welcome to the Inventory Manager")

def checkout():
    print("Welcome to the Inventory Manager")




def staff_mgmt():
    while True:
        print("Welcome to the Staff Manager")
        print('')
        print("1. Add Staff")
        print("2. Update Staff")
        print("3. Remove Staff")
        print("4. Go Back")


        choice = int(input("Please Select A Function:"))
        if choice == 1:
            os.system('cls')
            add_staff()
        elif choice == 2:
            os.system('cls')
            update_staff()
        elif choice == 3:
            os.system('cls')
            remove_staff()
        elif choice == 4:
            print("Exiting....")
            os.system('cls')
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 5")
            os.system('cls')
            inventory_mgmt()

def add_staff():
    print("Welcome to the Inventory Manager")

def remove_staff():
    print("Welcome to the Inventory Manager")

def update_staff():
    print("Welcome to the Inventory Manager")



def generate_reports():
    print("Welcome to the Inventory Manager")




def make_order():
    print("Welcome to the Inventory Manager")


login()
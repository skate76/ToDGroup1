import getpass

Cusernames = ["customer123"]
Cpasswords = ["customer123"]

Eusernames = ["employee123"]
Epasswords = ["employee123"]

Ousernames = ["KTAIT123"]
Opasswords = ["KTAIT123"]

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
            break
        


def admin_menu():
    while True:
        
        print("1. Add/Update Inventory")
        print("2. Generate Reports")
        print("3. Manage Staff")
        print("4. Exit")
        choice = int(input("Please Select A Function:"))
    
        if choice == 1:
            print ("Add/Update Inventory")
        elif choice == 2:
            print("Manage Staff")
        elif choice == 3:
            print("Generate Reports")
        elif choice == 4:
            print("Exit")
            break 
        else:
            print("Invalid Choice. Please enter a number from 1 - 3")
        
        
def cus_menu():
    while True:
        print("1. Make an Order")
        print("2. Display Inventory")
        print("3. Exit")
     

        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Make an Order")
        elif choice == 2:
            print("Display Inventory")
        elif choice == 3:
            print("Exit")
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 2")
        


def emp_menu():
    while True:
        print("1. Add/Update Inventory")
        print("2. Check in/Check out")
        print("3. Exit")
    
        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Add/Update Inventory")
        elif choice == 2:
            print("Check in/Check out")
        elif choice == 3:
            print("Exit")
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 5")



def inventory_mgmt():
    print("Welcome to the Inventory Manager")

def add_inventory():
    print("Welcome to the Inventory Manager")

def update_inventory():
    print("Welcome to the Inventory Manager")

def remove_inventory():
    print("Welcome to the Inventory Manager")

def display():
    print("Welcome to the Inventory Manager")

def checkin():
    print("Welcome to the Inventory Manager")

def checkout():
    print("Welcome to the Inventory Manager")




def staff_mgmt():
    print("Welcome to the Staff Manager")

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
import datetime
class Employee:
  employee_list = []
  
  @classmethod
  def employee_initialization():
    # Add your ID number, position and password if you want 
    Employee(1, "Justin Moo", "Manager", "employee1", "password1")
    Employee(2, "Katelyn Tait", "Cashier", "employee2", "password2")
    Employee(3, "Nasya Burrell", "Cashier", "employee3", "password3")
    Employee(4, "Tishawn Whyte", "Cashier", "employee4", "password4")
    Employee(5, "Johnathon Bennet", "Cashier", "employee5", "password5")
    Employee(6, "Dominic Adams", "Cashier", "employee6", "password6")

  
   #Functions for checking in and out employees 
  def check_in(self):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.check_in_datatime = current_datetime
    print(f"{self.employee_name} checked in at {current_datatime}.")

  def check_out(self):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
    printf(f"{self.employee_name} checked out at {current_datatime}.")
    
  #function to add employee data 
  @classmethod
  def add_employee(cls):
    print("Enter employee details:")
    try: 
      employee_id = int(input("Enter Employee ID: "))
      employee_name = input("Enter employee name: ")
      employee_position = input("Enter employee position: ")
      username = input("Enter username: ")
      password = input ("Enter password: ")
      phone_number = input ("Enter email address: ")
      email = input ("Enter phone number: ")
      status = input ("Enter status (Active / Inactive, default is Active): ") or "Active"

      new_employee = Employee(employee_id, employee_name, employee_position, username, password, status)
      print(f" Employee {employee_name} added successfully!")
    except ValueError:
      print("Invalid input. Please neter a valid ID and ensure all fields are filled correctlty.")

  
  #Display the list of employees 
  def display_employees(cls): 
    if cls.employee)_list:
      print("Employee List: ")
      for employee in cls.employee_list:
        print(f"ID: {employee.employee_id}, Name: {employee.employee_name}, Position: {employee.position} Phone: {employee.phone_number}, Email: {employee.email}")
    else:
      print("No employees found.")


  #Function to update employee contact details 
  def update_employee_contact(cls, employee_id)
  
  def __init__(self, employee_id, employee_name, employee_position, employee_username, employee_password, status = "Active"): 
    self.employee_id = employee_id
    self.employee_name = employee_name
    self.position = employee_position
    self.username = employee_username
    self.password = employee_password
    self.status = status
    self.phonenumber = phone_number
    self.email = email
    
    Employee.employee_list.append(self)

  

    
  
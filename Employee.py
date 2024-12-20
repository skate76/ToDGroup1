import datetime

class Employee:
    employee_list = []

    def __init__(self, employee_id, employee_name, employee_position, employee_username, employee_password, employee_phonenumber, employee_email, employee_payrate, status="Active"):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.position = employee_position
        self.username = employee_username
        self.password = employee_password
        self.phonenumber = employee_phonenumber
        self.email = employee_email
        self.attendance_r = []
        self.payrate = employee_payrate
        self.status = status

        Employee.employee_list.append(self)

    @classmethod
    def employee_initialization(cls):
        # Add your ID number, position, password, etc.
        Employee(1, "Justin Moo", "Manager", "employee1", "password1", "123-456-7890", "justin@example.com", 20.00)
        Employee(2, "Katelyn Tait", "Cashier", "employee2", "password2", "123-456-7891", "katelyn@example.com", 20.00)
        Employee(3, "Nasya Burrell", "Cashier", "employee3", "password3", "123-456-7891", "nasya@example.com", 20.00)
        Employee(4, "Tishawn Whyte", "Cashier", "employee4", "password4", "123-456-7891", "tishawn@example.com", 20.00)
        Employee(5, "Johnathon Bennet", "Cashier", "employee5", "password5", "123-456-7892", "johnathon@example.com", 20.00)
        Employee(6, "Dominic Adams", "Cashier", "employee6", "password6", "123-456-7893", "dominic@example.com", 20.00)

    # Functions for checking in and out employees
    def check_in(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.check_in_datetime = current_time
        print(f"{self.employee_name} checked in at {current_time}.")

    def check_out(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{self.employee_name} checked out at {current_time}.")

    # Function to add employee data
    @classmethod
    def add_employee(cls):
        print("Enter employee details:")
        try:
            employee_id = int(input("Enter Employee ID: "))
            employee_name = input("Enter employee name: ")
            employee_position = input("Enter employee position: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            payrate = float(input("Enter pay rate: "))
            status = input("Enter status (Active / Inactive, default is Active): ") or "Active"

            new_employee = Employee(employee_id, employee_name, employee_position, username, password, phone_number, email, payrate, status)
            print(f"Employee {employee_name} added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid ID, pay rate, and ensure all fields are filled correctly.")

    # Display the list of employees
    @classmethod
    def display_employees(cls):
        if cls.employee_list:
            print("Employee List: ")
            for employee in cls.employee_list:
                print(f"ID: {employee.employee_id}, Name: {employee.employee_name}, Position: {employee.position}, "
                      f"Phone: {employee.phonenumber}, Email: {employee.email}, Pay Rate: {employee.payrate}, "
                      f"Status: {employee.status}")
        else:
            print("No employees found.")

    # Function to update employee contact details
    @classmethod
    def update_employee_contact(cls, employee_id):
        employee = cls.employee_finder(employee_id)
        if employee:
            print(f"Updating contact details for {employee.employee_name}:")
            new_phone = input(f"Enter new phone number (Current: {employee.phonenumber}): ")
            new_email = input(f"Enter new email (Current: {employee.email}): ")
            employee.phonenumber = new_phone
            employee.email = new_email
            print(f"Contact details for {employee.employee_name} updated successfully!")
        else:
            print("Employee not found.")

    # Locates an employee by using their ID number, this will help with updating details
    @classmethod
    def employee_finder(cls, employee_id):
        for employee in cls.employee_list:
            if employee.employee_id == employee_id:
                return employee
        return None

    # View attendance of employees
    @classmethod
    def attendance_viewer(cls, employee_id):
        employee = cls.employee_finder(employee_id)
        if employee:
            print(f"Attendance records for {employee.employee_name}:")
            if employee.attendance_r:
                for idx, record in enumerate(employee.attendance_r, 1):
                    check_in, check_out = record
                    print(f"Day {idx}: Checked in at {check_in} | Checked out at {check_out if check_out else 'Not checked out yet'}")
            else:
                print("No attendance records found.")
        else:
            print("Employee not found.")

# Example usage
Employee.employee_initialization()
Employee.add_employee()  # Will ask for employee details and add new employee
Employee.display_employees()  # Displays all employees

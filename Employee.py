class Employee:
    employee_list = []  # List to store employee instances

    def __init__(self, empID, empName, role, username, password, status="Active"):
        self.empID = empID
        self.empName = empName
        self.role = role
        self.username = username
        self.password = password
        self.status = status
        Employee.employee_list.append(self)  # Add employee to the list

    def login(self, username, password):
        """Employee login method."""
        if self.username == username and self.password == password:
            print(f"Welcome {self.empName}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def clock_in(self, time):
        """Clock in the employee."""
        print(f"{self.empName} clocked in at {time}.")

    def clock_out(self, time):
        """Clock out the employee."""
        print(f"{self.empName} clocked out at {time}.")

    def update_order_status(self, order, status):
        """Allow employee to update order status."""
        order.status = status
        print(f"Order status updated to {status}.")

    @classmethod
    def find_employee_by_id(cls, empID):
        """Find employee by their ID."""
        for emp in cls.employee_list:
            if emp.empID == empID:
                return emp
        return None


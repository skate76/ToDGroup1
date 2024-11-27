import datetime
class Employee:
  employee_list = []
  
  def check_in(self)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.check_in_datatime = current_datetime
    printf(f"{self.employee_name} checked in at {current_datatime}.")

  def check_out(self)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
    printf(f"{self.employee_name} checked out at {current_datatime}.")
  
  
  def __init__(self, employee_id, employee_name, employee_role, employee_username, employee_password, status = "Active"): 
    self.employee_id = employee_id
    self.employee_name = employee_name
    self.role = employee_role
    self.username = employee_username
    self.password = employee_password
    self.status = status
    Employee.employee_list.append(self)

  

    
  

import pandas as pd
class EMS:
    def __init__(self):
        self.d = {
            101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
            102: {'name': 'Ravi', 'age': 32, 'department': 'Finance', 'salary': 62000},
            103:{'name': 'Anita', 'age': 29, 'department': 'Marketing', 'salary': 58000},
           104:{'name': 'Vikram', 'age': 35, 'department': 'IT', 'salary': 75000},
           105:{'name': 'Meera', 'age': 26, 'department': 'Sales', 'salary': 49000},
           106:{'name': 'Kiran', 'age': 31, 'department': 'Operations', 'salary': 67000}}

    def main_menu(self):
        while True:
            print("\nMENU")
            print("1. Add Employee \n2. View All Employees \n3. Search for Employee \n4. Exit")
            a = int(input("Enter your menu (1 to 4): "))
            if a == 1:
                self.add_employee()
            elif a == 2:
                self.view_employee()
            elif a == 3:
                self.search_employee()
            elif a==4:
                 print("Thank you")
                 break
            else:
                print("Invalid input")
                

    def add_employee(self):
        emp_id = int(input("Enter your employee ID: "))
        if emp_id in self.d:
            print("This ID already exists")
            return
        else:
          name = input("Enter your name: ")
          age = int(input("Enter your age: "))
          department = input("Enter your department: ")
          salary = int(input("Enter your salary: "))
          self.d[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}
          print("Added successfully")

    def view_employee(self):
        if not self.d:
            print("No employees found")
        else:
            df = pd.DataFrame(self.d).T
            print(df)

    def search_employee(self):
        emp_id = int(input("Enter the Employee ID: "))
        if emp_id in self.d:
            print(self.d[emp_id])
        else:
            print("Employee ID not found")

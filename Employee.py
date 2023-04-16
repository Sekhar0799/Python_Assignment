import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name} ({self.dob}) from {self.city}, {self.state}. Height: {self.height} cm."


with open('C:\Users/sekha\OneDrive\Documents\Python Scripts\Edyoda\Employee.json') as f:
    data = json.load(f)

employee_list = []
for emp in data['employees']:
    employee = Employee(emp['name'], emp['dob'], emp['height'], emp['city'], emp['state'])
    employee_list.append(employee)

for emp in employee_list:
    print(emp)


# 2 Patient record management

# set up class
class patients:
    def __init__(self, name, age, latest_admission_date, medical_history):
        self.name = name
        self.age = age
        self.latest_admission_date = latest_admission_date
        self.medical_history = medical_history

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Latest Admission Date: {self.latest_admission_date}, Medical History: {self.medical_history}")



# example
patient1 = patients("Harry", 20, "2025-04-08", "Health")
patient1.print_details()
    
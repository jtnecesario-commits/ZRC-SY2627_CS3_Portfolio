class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            print("Bill amount cannot be negative. PLEASE.")

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
patients = [
    Patient("Juan Dela Cruz", 15000), # JUANHAND, or wtv the name was
    SeniorPatient("B", 1000),
    PhilHealthPatient("A", 25000)]

for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Original Bill: P", patient.get_bill_amount())
    print("Final Bill: P", patient.calculate_bill())
    print("Thank you for trusting us with your life. Arigathankyou! ")
    print("-" * 30)
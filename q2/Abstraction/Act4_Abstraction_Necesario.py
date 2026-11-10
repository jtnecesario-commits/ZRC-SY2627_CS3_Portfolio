
from abc import ABC, abstractmethod

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

    def display_patient_type(self):
        print("Patient Type: Regular Patient.")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

patients = [
    Patient("Juan Dela Cruz", 15000),
    SeniorPatient("Hillary Legaspi", 1000),
    PhilHealthPatient("Yrvic Barrium", 25000)
]

for patient in patients:
    print("Patient Name:", patient.get_name())
    patient.display_patient_type()
    print("Original Bill: P", patient.get_bill_amount())
    print("Final Bill: P", patient.calculate_bill())
    print("Thank you for trusting us with your life. Arigathankyou!")
    print("-" * 30)

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):

    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH : Neutral")

class TempSensor(Sensor):

    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5C")

print("Lab Inventory System")

ph_sensor = PHSensor()
temp_sensor = TempSensor()

ph_sensor.get_reading()
temp_sensor.get_reading()

print()
print("-" * 30)
print("acidic or not your the perfect ph level for me ;)")

try:
    my_sensor = Sensor()
except TypeError as e:
    print("\nTask 5 - Break it Test:")
    print(type(e).__name__ + ":", e)
# sir to be honest, I didnt know how to do/ make the break it test so i asked google and it gave me this and
# figured out how to make it with heavy help from google.
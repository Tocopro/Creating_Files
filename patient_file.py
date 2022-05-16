
from datetime import datetime

# patient name, age, and gender intake information


def intake_id():
    name, age, gender = main()
    print(name, age, gender)
    time_stamp = datetime.today()
    print(time_stamp.strftime("Date: %b %d %Y  Time: %H:%M:%S"))

    with open("C:\\Users\\NEAK\\Downloads\\Patient file.txt", "a", encoding='utf-8') as patient_file:
        patient_file.write(time_stamp.strftime("Date: %b %d %Y   Time: %H:%M:%S \n"))
        patient_file.write("Name: " + name + "\n")
        patient_file.write("Age: " + age + "\n")
        patient_file.write("Gender: " + gender + "\n")
        patient_file.close()


def main():
    name = str(input("Enter the Patients Name: "))
    age = str(input("Enter the Patients Age: "))
    gender = str(input("Enter the Patients Gender: "))
    return name, age, gender


intake_id()

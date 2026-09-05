# write a python program that accepts a std's personal and academic details 
std_name=input("Enter student name :")
std_usn=input("Enter student usn:")
branch=input("Enter branch of the student:")
semester=int(input("Semester:"))
s1=int(input("Enter marks of subject 1:"))
s2=int(input("Enter marks of subject 2:"))
s3=int(input("Enter marks of subject 3:"))
avg=(s1+s2+s3)/3
total_marks =(s1+s2+s3)
print("Average mark :",avg)
print("Total marks obtained:",total_marks)

# perform the operations

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
add=a+b
sub=a-b
div=a/b
mul=a*b
mod=a%b
floor=a//b
expo=a**b
print("Addition=",add ,"\nSubtraction:",sub,"\nMultiplication:",mul,"\nDivision:",div,
      "\nMultiplication:",mul,"\nModulus:",mod,"\nFloor division:",floor,"\nExponant:",expo)

#Area of circle 
radius = float(input("Enter radius of the circle: "))
area = 3.14159 * radius * radius
print("Area of the circle =", area)

#Electricity bill geerator:

print("===== UNIT CONVERTER =====")
print("1. Kilometres to Metres")
print("2. Metres to Kilometres")
print("3. Kilograms to Grams")
print("4. Grams to Kilograms")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
    result = value * 1000
    print("Result =", result, "metres")

elif choice == 2:
    result = value / 1000
    print("Result =", result, "kilometres")

elif choice == 3:
    result = value * 1000
    print("Result =", result, "grams")

elif choice == 4:
    result = value / 1000
    print("Result =", result, "kilograms")

elif choice == 5:
    result = (value * 9 / 5) + 32
    print("Result =", result, "°F")

elif choice == 6:
    result = (value - 32) * 5 / 9
    print("Result =", result, "°C")

else:
    print("Invalid choice")

# Write a python program to create a simple contact book using list & dictionaries. The 

contacts=[]
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == 2:
        if not contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(contacts):
                print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    elif choice == 3:
        search_name = input("Enter the name to search: ")
        found_contacts = [contact for contact in contacts if contact['name'].lower() == search_name.lower()]
        if not found_contacts:
            print("No contacts found with that name.")
        else:
            for contact in found_contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    elif choice == 4:
        print("Exiting the contact book.")
        break

    else:
        print("Invalid choice. Please try again.")

#number guessing game
import random

number = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


#prime number program 
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

# factorial program 
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =", factorial)

#Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i))

#OTP generator 
import random
import string
import smtplib
from email.mime.text import MIMEText
import time

class OTPGenerator:
    def __init__(self, length=6, validity_seconds=300):
        self.length = length
        self.validity_seconds = validity_seconds
        self.otp_store = {}  # {user_id: (otp, expiry_time)}

    def generate_otp(self, user_id):
        otp = ''.join(random.choices(string.digits, k=self.length))
        expiry = time.time() + self.validity_seconds
        self.otp_store[user_id] = (otp, expiry)
        return otp

    def verify_otp(self, user_id, otp_input):
        if user_id not in self.otp_store:
            return False, "No OTP generated for this user."
        otp, expiry = self.otp_store[user_id]
        if time.time() > expiry:
            del self.otp_store[user_id]
            return False, "OTP expired."
        if otp_input == otp:
            del self.otp_store[user_id]  # one-time use
            return True, "OTP verified successfully."
        return False, "Incorrect OTP."

    def send_otp_email(self, sender_email, sender_password, receiver_email, otp):
        msg = MIMEText(f"Your OTP is: {otp}. It is valid for {self.validity_seconds // 60} minutes.")
        msg["Subject"] = "Your One-Time Password (OTP)"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)


# Example usage
if __name__ == "__main__":
    gen = OTPGenerator(length=6, validity_seconds=120)

    user = "user123"
    otp = gen.generate_otp(user)
    print(f"Generated OTP for {user}: {otp}")

    # Simulate verification
    entered = input("Enter OTP: ")
    success, message = gen.verify_otp(user, entered)
    print(message)

# student grading automation program
class GradingSystem:
    def __init__(self, grade_scale=None):
        # Default grade scale (percentage -> letter grade)
        self.grade_scale = grade_scale or {
            90: "A", 80: "B", 70: "C", 60: "D", 0: "F"
        }

    def calculate_percentage(self, marks_obtained, total_marks):
        return round((marks_obtained / total_marks) * 100, 2)

    def get_letter_grade(self, percentage):
        for threshold in sorted(self.grade_scale.keys(), reverse=True):
            if percentage >= threshold:
                return self.grade_scale[threshold]
        return "F"

    def grade_student(self, name, scores: dict):
        """scores = {'subject': (marks_obtained, total_marks)}"""
        total_obtained = sum(m[0] for m in scores.values())
        total_possible = sum(m[1] for m in scores.values())
        percentage = self.calculate_percentage(total_obtained, total_possible)
        letter = self.get_letter_grade(percentage)

        subject_results = {
            subject: {
                "marks": f"{obtained}/{total}",
                "percentage": self.calculate_percentage(obtained, total),
                "grade": self.get_letter_grade(self.calculate_percentage(obtained, total))
            }
            for subject, (obtained, total) in scores.items()
        }

        return {
            "name": name,
            "subjects": subject_results,
            "overall_percentage": percentage,
            "overall_grade": letter
        }

    def grade_class(self, students: dict):
        """students = {'name': {'subject': (marks_obtained, total_marks)}}"""
        return [self.grade_student(name, scores) for name, scores in students.items()]


# Example usage
if __name__ == "__main__":
    grader = GradingSystem()

    students = {
        "Alice": {"Math": (88, 100), "Science": (92, 100), "English": (76, 100)},
        "Bob": {"Math": (55, 100), "Science": (60, 100), "English": (48, 100)},
    }

    results = grader.grade_class(students)

    for r in results:
        print(f"\nStudent: {r['name']}")
        for subject, detail in r["subjects"].items():
            print(f"  {subject}: {detail['marks']} ({detail['percentage']}%) - Grade {detail['grade']}")
        print(f"  Overall: {r['overall_percentage']}% - Grade {r['overall_grade']}")









































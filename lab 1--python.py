'''# write a python program that accepts a std's personal and academic details 
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
    print("Invalid choice")'''


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










































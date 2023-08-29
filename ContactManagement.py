contacts = {}  # Dictionary to store contacts

def add_contact():
    name = input("Enter the contact's name: ")
    number = input("Enter the contact's phone number: ")
    contacts[name] = number
    print("Contact added successfully!")

def update_contact():
    name = input("Enter the contact's name: ")
    if name in contacts:
        number = input("Enter the new phone number: ")
        contacts[name] = number
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the contact's name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def view_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name} - Phone Number: {number}")
    else:
        print("No contacts found.")

def phone_app():
    while True:
        print("\n--- Welcome Contact Phone Application *_* ---\n")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Exit")

        choice = input("Enter your choice ( Form 1 To 5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            view_contacts()
        elif choice == "5":
            print("Exiting the phone application.\n Thanks For Using Our App *_*")
            break
        else:
            print("Invalid choice. Please try again *_*")

phone_app()
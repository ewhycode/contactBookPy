#import `json` module to handle data storage
import json

#an empty dictionary to store contacts
contacts = {}

def add_contact():
    """
    Adds a new contact to the contact book.
    """
    # Get user input for name and contact number
    name = input("Enter name: ")
    contact_number = input("Enter contact number: ")

    # Check if contact number is already in use
    if contact_number in contacts.values():
        print("Contact number already exists.")
    else:
        # Add contact to dictionary
        contacts[name] = contact_number
        print("Contact added successfully.")

def view_contacts():
    """
    Displays all contacts in the contact book.
    """
    if not contacts:
        print("No contacts available.")
    else:
        # Iterate over contacts and print them
        for name, contact_number in contacts.items():
            print(f"{name}: {contact_number}")

def delete_contact():
    """
    Deletes a contact from the contact book.
    """
    # Get user input for name of contact to delete
    name = input("Enter name of contact to delete: ")

    # Check if contact exists
    if name in contacts:
        # Delete contact from dictionary
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def save_contacts():
    """
    Saves contacts to a JSON file.
    """
    # Open file in write mode
    with open("contacts.json", "w") as file:
        # Write contacts to file using JSON
        json.dump(contacts, file)
    print("Contacts saved successfully.")

def load_contacts():
    """
    Loads contacts from a JSON file.
    """
    try:
        # Open file in read mode
        with open("contacts.json", "r") as file:
            # Load contacts from file using JSON
            global contacts
            contacts = json.load(file)
    except FileNotFoundError:
        print("No saved contacts found.")

def main():
    # Load saved contacts
    load_contacts()

    while True:
        # Display menu
        print("\nContact Book Menu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contact")
        print("4. Save contacts")
        print("5. Quit")

        # Get user input for menu choice
        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            save_contacts()
        elif choice == "5":
            # Save contacts before quitting
            save_contacts()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# A mini Contact Book by Manan Sati
import os
import sys

print("A mini Contact Book by Manan")

if not os.path.exists("contacts.txt"):
    open("contacts.txt", "a").close()

while True:
    try:
        options = int(input("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit\n"))
        os.system('clear')
    except ValueError:
        print("Invalid Input, please try again!")
        continue

    if options == 5:
        sys.exit()

    elif options == 1:  
        name = input("Enter Contact Name: ").strip()
        try:
            phnum = int(input("Enter Phone Number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        new_contact = f"{name} - {phnum}\n"
        with open("contacts.txt", "a") as file:
            file.write(new_contact)
        
        print("New contact added!\n")
        input("Press Enter to continue...")

    elif options == 2: 
        with open("contacts.txt", "r") as file:
            content = file.read()
            print(content if content else "No contacts found!")
        
        input("Press Enter to continue...")

    elif options == 3: 
        search_name = input("Enter name to search: ").strip().lower()
        found = False

        with open("contacts.txt", "r") as file:
            for line in file:
                if search_name in line.lower():
                    print(f"Contact Found: {line.strip()}")
                    found = True
                    break
        
        if not found:
            print("Contact not found!")
        
        input("Press Enter to continue...")

    elif options == 4:  
        delete_name = input("Enter name to delete: ").strip().lower()
        updated_contacts = []

        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        found = False
        for contact in contacts:
            if delete_name in contact.lower():
                found = True
            else:
                updated_contacts.append(contact)

        if found:
            with open("contacts.txt", "w") as file:
                file.writelines(updated_contacts)
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

        input("Press Enter to continue...")

    else:
        print("Invalid option, please try again!")

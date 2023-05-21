import csv
import shutil
from datetime import datetime
import os
import sys
 
            
def generate_backup_file_name():
        # This function generates a unique backup file 
        try:
            current_data = datetime.now().strftime("%d%m%Y")
            backup_file_name = f"contactbook_{current_data}.csv"
            return backup_file_name
        except:
            print("Sorry,some error happend when create backup file name ")
            
def backup(backup_directory):
        # This function creates a backup of the contact book by copying the file to the specified backup directory.
        try:
            if not os.path.exists(backup_directory):
                os.makedirs(backup_directory)
            backup_file_name = generate_backup_file_name()
            shutil.copy('contactbook.csv', os.path.join(
                backup_directory, backup_file_name))
        except:
            print("Sorry,some error happend when backup ")
 # will save the content in csv file 
def save_contact(username, email, phone, address, insertion_date):
     with open('contactbook.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, phone, address, insertion_date])
        
           # will view the content in csv file
def view_contacts():
    with open('contactbook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
          # will add the content then save it
def add_contact():
    
    username = input("Enter username: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    insertion_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    save_contact(username, email, phone, address, insertion_date)
    print("Contact added successfully!")

    # update content if needed
def update_contact():
    username = input("Enter username of contact to update: ")
    field = input("Enter field to update (username/email/phone/address/): ")
    new_value = input("Enter new value: ")
    
    
    
    with open('contactbook.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        for row in rows:
         if row[0] == username:
            if field == "username":
                row[0] = new_value
            elif field == "email":
                row[1] = new_value
            elif field == "phone":
                row[2] = new_value
            elif field == "address":
                row[3] = new_value
         
                
    with open('contactbook.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
                
    print("Contact updated successfully!")
# remove a content if needed

def remove_contact():
    name = input("Enter name of contact to remove: ")

    with open('contactbook.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == name:
            rows.remove(row)

    with open('contactbook.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Contact removed successfully!")
    
    # allow you to choose what you will need to do




while True:
    print("\nWelcome to the Contact Book!")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Update a contact")
    print("4. Remove a contact")
    print("5. backup your contact")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
       update_contact()
    elif choice == "4":
       remove_contact()
    elif choice == "5":
         backup_dir_name = input("Enter Backup Directory Name: ")
         backup(backup_dir_name)
    elif choice == "6":
        print("Thank you for using the Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")


        
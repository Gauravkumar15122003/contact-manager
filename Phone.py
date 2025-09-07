import tkinter as tk
from tkinter import messagebox, simpledialog
import json

CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter the contact name:")
    if not name: return
    phone = simpledialog.askstring("Input", "Enter the phone number:")
    email = simpledialog.askstring("Input", "Enter the email address:")
    address = simpledialog.askstring("Input", "Enter the address:")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    save_contacts(contacts)
    messagebox.showinfo("Success", f"Contact {name} added successfully.")

# View all contacts
def view_contacts():
    if not contacts:
        messagebox.showinfo("Info", "No contacts found.")
        return
    contact_info = "\n".join(
        f"Name: {name}\n  Phone: {details['phone']}\n  Email: {details['email']}\n  Address: {details['address']}\n"
        for name, details in contacts.items()
    )
    messagebox.showinfo("Contacts", contact_info)

# Search for a contact
def search_contact():
    search_term = simpledialog.askstring("Input", "Enter the name or phone number to search:")
    if not search_term: return
    found = False
    contact_info = ""
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone']:
            contact_info += (f"Name: {name}\n  Phone: {details['phone']}\n  Email: {details['email']}\n  Address: {details['address']}\n\n")
            found = True
    if found:
        messagebox.showinfo("Search Results", contact_info)
    else:
        messagebox.showinfo("Info", "No contact found.")

# Update a contact
def update_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Input", "Enter the new phone number:")
        email = simpledialog.askstring("Input", "Enter the new email address:")
        address = simpledialog.askstring("Input", "Enter the new address:")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {name} updated successfully.")
    else:
        messagebox.showinfo("Info", "Contact not found.")

# Delete a contact
def delete_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
    else:
        messagebox.showinfo("Info", "Contact not found.")

# Create main window
root = tk.Tk()
root.title("Contact Manager")

# Create buttons with colors
btn_add = tk.Button(root, text="Add Contact", command=add_contact, width=20, height=2, font=('Arial', 12), bg='lightblue', fg='black')
btn_view = tk.Button(root, text="View Contacts", command=view_contacts, width=20, height=2, font=('Arial', 12), bg='lightgreen', fg='black')
btn_search = tk.Button(root, text="Search Contact", command=search_contact, width=20, height=2, font=('Arial', 12), bg='lightyellow', fg='black')
btn_update = tk.Button(root, text="Update Contact", command=update_contact, width=20, height=2, font=('Arial', 12), bg='lightcoral', fg='black')
btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact, width=20, height=2, font=('Arial', 12), bg='lightsalmon', fg='black')
btn_exit = tk.Button(root, text="Exit", command=root.quit, width=20, height=2, font=('Arial', 12), bg='lightgray', fg='black')

# Arrange buttons in the window
btn_add.pack(pady=10)
btn_view.pack(pady=10)
btn_search.pack(pady=10)
btn_update.pack(pady=10)
btn_delete.pack(pady=10)
btn_exit.pack(pady=20)

# Load existing contacts
contacts = load_contacts()

# Start the GUI event loop
root.mainloop()

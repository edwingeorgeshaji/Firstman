# Guido Task Reminder App

import json
from datetime import datetime



# File to store reminders
ReminderFile = "GuidoTaskReminder.json"



# Load reminders from file
def load_reminders():
    try:
        with open(ReminderFile, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



# Save reminders to file
def save_reminders(reminders):
    with open(ReminderFile, "w") as file:
        json.dump(reminders, file, indent=4)



# Add a new reminder
def add_reminder():
    description = input("Enter reminder description: ")
    due_date = input("Enter due date (DD-MM-YYYY HH:MM): ")
    
    try:
        due_date = datetime.strptime(due_date, "%d-%m-%Y %H:%M")
        reminders = load_reminders()
        reminders.append({"description": description, "due_date": due_date.strftime("%d-%m-%Y %H:%M")})
        save_reminders(reminders)
        print("Reminder added successfully!")
    except ValueError:
        print("Invalid date format. Please try again.")



# View all reminders
def view_reminders():
    reminders = load_reminders()
    if not reminders:
        print("No reminders found.")
        return
    
    print("\nYour Reminders:")
    for i, reminder in enumerate(reminders, start=1):
        print(f"{i}. {reminder['description']} (Due: {reminder['due_date']})")
    print()



# Delete a reminder
def delete_reminder():
    view_reminders()
    reminders = load_reminders()
    if not reminders:
        return
    
    try:
        reminder_index = int(input("Enter the reminder number to delete: ")) - 1
        if 0 <= reminder_index < len(reminders):
            reminders.pop(reminder_index)
            save_reminders(reminders)
            print("Reminder deleted successfully!")
        else:
            print("Invalid reminder number.")
    except ValueError:
        print("Invalid input. Please enter a number.")



# Main menu
def main():
    while True:
        print("\nGuido Task Reminder\n")
        print("1. Add a reminder")
        print("2. View all reminders")
        print("3. Delete a reminder")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            delete_reminder()
        elif choice == "4":
            print("Goodbye!\nCreated by R.E.C (ifykyk).")
            break
        else:
            print("Invalid choice buddy!. Please try again.")

if __name__ == "__main__":
    main()

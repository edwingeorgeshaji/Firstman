# Guido Task Reminder App

## Introduction
Guido Task Reminder is a simple yet efficient console-based application built in Python. This app allows users to manage their tasks and reminders effortlessly. Users can add, view, and delete reminders, ensuring they never miss important deadlines.

---

## Features
- **Add Reminders**: Add tasks with a description and a specific due date and time.
- **View Reminders**: Display all the reminders with their details in an organized format.
- **Delete Reminders**: Remove completed or unwanted tasks.
- **Persistent Storage**: All reminders are saved in a `reminders.json` file, ensuring data is retained even after the program is closed.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - `json` for data storage and retrieval.
  - `datetime` for handling date and time.

---

## Prerequisites
- Python 3.7 or above installed on your system.

---

## How to Run the App
1. Clone the repository:
   ```bash
   git clone https://github.com/edwingeorgeshaji/Firstman/task-reminder.git
   ```

2. Navigate to the project directory:
   ```bash
   cd guido-task-reminder
   ```

3. Run the application:
   ```bash
   python guido_task_reminder.py
   ```

---

## Usage
1. **Adding a Reminder**:
   - Select option `1` from the menu.
   - Enter the task description and due date in the format `DD-MM-YYYY HH:MM`.
   
2. **Viewing All Reminders**:
   - Select option `2` to see all your saved reminders.

3. **Deleting a Reminder**:
   - Select option `3`, then enter the number corresponding to the reminder you wish to delete.

4. **Exit**:
   - Select option `4` to close the application.

---

## Example Output
```plaintext
Guido Task Reminder
1. Add a reminder
2. View all reminders
3. Delete a reminder
4. Exit

Enter your choice: 1
Enter reminder description: Buy groceries
Enter due date (DD-MM-YYYY HH:MM): 27-12-2024 18:30
Reminder added successfully!

Enter your choice: 2

Your Reminders:
1. Buy groceries (Due: 2024-12-27 18:30)

Enter your choice: 3
Enter the reminder number to delete: 1
Reminder deleted successfully!

Enter your choice: 4
Goodbye!
```

---

## File Structure
- `guido_task_reminder.py`: Main Python script containing the app logic.
- `reminders.json`: JSON file used for storing reminders persistently.

---

## Future Improvements
- Add functionality to edit existing reminders.
- Integrate a graphical user interface (GUI) for better user experience.
- Add notifications for upcoming reminders.

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to enhance the app.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Author
Created by [E D W I N](https://github.com/edwingeorgeshaji). Feel free to reach out for any questions or suggestions!



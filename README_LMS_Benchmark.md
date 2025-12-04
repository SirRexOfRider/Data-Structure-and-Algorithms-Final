# Library Management System

This is a **Library Management System** built using Python. It was created as part of my learning journey with Python programming. The system provides basic functionality for managing a library's books and users. It runs through the command line and allows users to perform operations such as adding books, borrowing books, returning books, and viewing available books.

## Features

- **Add Books**: Add new books to the library collection.
- **View Books**: List all available books in the library.
- **Borrow Books**: Borrow books from the library (updates book availability).
- **Return Books**: Return borrowed books to the library.
- **Exit Program**: Safely exit the application.

## Requirements

To run this program, you need:

- Python 3.x installed on your system.
- A terminal or command line interface.

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python file using the command:
   ```bash
   python LMS.py
   ```
4. Follow the prompts in the command line to interact with the Library Management System.

## Usage

Once the program is running, you can perform the following actions:

1. **Add a Book**:
   - Enter the book's title, author, and other relevant details when prompted.
2. **View All Books**:
   - Displays a list of all books currently available in the library.
3. **Borrow a Book**:
   - Specify the title of the book you want to borrow. The system will check availability and update the record.
4. **Return a Book**:
   - Provide the title of the book being returned. The system will mark it as available.
5. **Exit**:
   - Safely exit the application without losing the data for the current session.

## Example Output

Here’s an example of what the command-line interface might look like:

```
### Welcome to the Central library of the university ###
Please Enter the option:
1. List the names of all available books
2. Request to borrow a book
3. Return a book
4. Add a book to the library
5. Exit the Library

How can I help you: 2
Enter the name of the book: Sherlock Holmes
You have borrowed the Sherlock Holmes. Please keep it safe...

### Welcome to the Central library of the university ###
Please Enter the option:
1. List the names of all available books
2. Request to borrow a book
3. Return a book
4. Add a book to the library
5. Exit the Library

How can I help you: 5
Thanks for using the Central Library!!
```

## Project Structure

The project consists of a single Python file, `LMS.py`. All the logic for managing the library is contained in this file, making it simple and easy to use.

## Future Enhancements

While this is a basic implementation, the following features could be added to improve the system:

- User authentication to manage accounts for members and administrators.
- Persistent data storage using a database or file system.
- Enhanced search functionality for finding books by title, author, or genre.
- GUI-based interface for a more user-friendly experience.

## Learning Outcomes

Through this project, I learned:

- How to write Python scripts for real-world use cases.
- Working with data structures like lists and dictionaries.
- Implementing a menu-driven program in Python.
- Writing clean and modular code.

## Contributing

This project was created for educational purposes, but if you’d like to contribute or suggest improvements, feel free to open an issue or submit a pull request.

## License

This project is open-source and free to use. No license is currently specified.

---

Thank you for checking out my Library Management System! 😊
```

Feel free to adapt this README to match the specifics of your project or add any additional details you think are relevant.

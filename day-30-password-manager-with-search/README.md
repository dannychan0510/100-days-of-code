# Day29: Password Manager

This simple password manager allows you to generate strong, random passwords and store them along with the associated website and username information in a local text file. The app is built using Python's Tkinter library for the graphical user interface.

## Python Concepts Learned

While building this password manager, I deepened my understanding of the following Python concepts:

1. **Further understanding of the .grid placement system in Tkinter with the columnspan argument**: This project involved arranging various widgets using the `.grid()` method in Tkinter. The `columnspan` argument was particularly useful in placing widgets spanning multiple columns.

2. **List comprehension in the password generator**: The password generator function employs list comprehension to efficiently create a random set of characters, numbers, and symbols for the password.

3. **Using the pyperclip package**: The pyperclip package was used to automatically copy the generated password to the user's clipboard, making it easy to paste the password wherever needed.

## How to Run the Program

To run the program, follow these steps. 

1. Ensure that you have Python 3 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Download the `main.py` file.

3. If you don't have the `pyperclip` package, You can install the pyperclip package using `pip install pyperclip`, or through your IDE.

4. After the package is installed, you can run the program by executing the main script `python main.py`. This will launch the Password Manager application, where you can generate and save passwords for various websites.

---

Disclaimer: This README is generated with the help of ChatGPT-4.
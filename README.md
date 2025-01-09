# Pytest Exercises

This project contains a series of exercises to learn automated testing in Python using the `pytest` library. The project includes examples of functions and tests, utilizing concepts such as exception handling, assertions, and input validation.

## Project Structure

The project is organized as follows:

pytest-exercises/ ├── src/ │ └── mainn.py # Implemented functions ├── tests/ │ ├── init.py # Empty file, marks the folder as a Python module │ └── test_main.py # Tests for the functions in main.py 


## How to Run the Tests

1. Clone the repository:
   ```bash
   git clone https://github.com/Serin15/pytest-exercises.git
   cd pytest-exercises

   
Implemented Functions
assembly(a, b)

This function takes two numbers and returns their sum.
Example:

assembly(2, 3)  # Returns 5
divide(a, b)

Divides two numbers. Raises a ValueError if b is 0.
Example:

divide(10, 2)  # Returns 5
divide(10, 0)  # Raises ValueError
check_age(age)

Checks if the age is valid. Raises a ValueError if it's negative.
Example:

check_age(25)  # Valid age
check_age(-5)  # Raises ValueError
only_str(text)

Accepts only strings, raises a TypeError otherwise. Converts the text to uppercase.
Example:

only_str("hello")  # Returns "HELLO"
only_str(123)      # Raises TypeError


License
This project is open-source and uses the MIT License.



### **Explanation for each section:**

1. **Project Structure:**
   - Describes how the project is structured, showing the `src/` folder with the functions and the `tests/` folder where the test files are.

2. **How to Run the Tests:**
   - Provides clear instructions for setting up the project, installing dependencies, and running the tests using `pytest`.

3. **Implemented Functions:**
   - Each function is explained with its behavior and an example of how it can be used. This section describes the core functions of your project: `assembly`, `divide`, `check_age`, and `only_str`.

4. **How to Contribute:**
   - This section encourages others to contribute by forking the project and creating a pull request.

5. **License:**
   - States that the project is open-source and provides a link to the MIT license (you can change this if you use a different license).

---

### **How to Add this README to Your GitHub Repository:**

1. Copy the content above into a new file called `README.md` in the root directory of your project.
   
2. Add it to Git and commit the changes:
   ```bash
   git add README.md
   git commit -m "Added README.md"
   git push origin main

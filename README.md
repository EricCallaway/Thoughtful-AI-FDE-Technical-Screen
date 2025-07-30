# Thoughtful AI: Forward Deployed Engineer Position Project Submission

Hello! This is my submission for the Forward Deployed Engineer Position. In this readme, I will walk through a quick list of steps to run the code and then a brief architectural design explaining the decisions behind the structure of this software to accomplish the intended goal.

## Dependencies
- Python <= 3.9.6  
- Pytest <= 8.4.1

## Steps to Test
1. `git clone https://github.com/EricCallaway/Thoughtful-AI-FDE-Technical-Screen.git`
2. `cd Thoughtful-AI-FDE-Technical-Screen`
3. `python3 main.py`
4. Observe results.
5. To run the unit test suite, simply run `pytest` while in the root directory of the project.
6. You are able to load different csv files to test for different outcomes of the program. Simply follow the same format of the given input.csv file.

## Architectural Decisioning

This problem essentially involves writing a program to place a package into the correct stack based on the quantitative measurements of that package (width, height, length, mass). The criteria that determine which stack to place the package in depend on the package’s attributes (heavy or bulky).

From the problem description, I derived three separate objects that interact with each other:
1. Factory  
2. Package  
3. Stack

### Factory Object

I conceptualized the factory object as having the main function requested in the original problem, `sort_package`. This function is a behavior that a factory can perform, so it makes sense to have it as a member function of the Factory object.

#### Factory Object: Attributes

1. `name`  
   The Factory technically does not require any attributes to solve the original problem. However, I build software with extensibility in mind. Who’s to say we won't require multiple factories in the future? In that case, we would need some way to differentiate between them. In a real-world application, they would have a name and unique identifier—this is just a placeholder for that functionality.

#### Factory Object: Functions

1. `sort_package`  
   This function takes the necessary input (width, height, length, mass) and creates a Package object. The Package object handles its own logic to determine whether it's heavy or bulky. The factory then places the package into the correct stack based on that classification and returns the type of stack it belongs to.

> **Note**: In an actual program, the list of stack types would not be hard-coded. Instead, we would dynamically query a list of stack types along with their corresponding criteria. This function would likely just place the package into the appropriate stack, rather than returning a string. That’s why I created a Stack class even though it isn’t fully used here. In a real implementation, the Factory class would also have attributes to track the existing stacks, and each stack would contain Package objects. This is out of scope for this project but would be straightforward to implement given the current architecture.

### Package Object

I chose to make a Package class because the data provided (mass, width, height, length) describes a physical package. Structuring this data in an object-oriented way is much cleaner and more maintainable than doing raw computations in the factory. This allows for easier future enhancements as well.

#### Package Object: Attributes

1. `mass`, `width`, `height`, `length`, `volume`  
   These are the measurements of the package. The constructor takes the values as parameters, performs basic validation (more would be required in production), and assigns them to attributes.

2. `bulky`, `heavy`  
   These attributes are derived from the dimensional and mass measurements. Once the measurements are set, the Package can determine whether it is considered bulky or heavy.

#### Package Object: Functions

1. `_is_bulky`, `_is_heavy`, `_get_volume`  
   These are helper methods called when the Package object is instantiated. They encapsulate the logic for setting `bulky` and `heavy`, which allows for easy modification in the future if business requirements change.

### Stack Object

Although the Stack class is not used in this version of the code, I chose to include it because the problem statement refers to stacks as distinct entities. A Stack has its own attributes and responsibilities. If this code were to be extended, having a dedicated Stack class would make the code more readable, maintainable, and adaptable.

### Testing

The current test suite is very simple and only serves to demonstrate basic correctness. To improve the coverage and robustness of these tests, I would create edge-case tests focusing on boundary conditions, particularly for logic that involves thresholds.

For example, the `_is_bulky` function returns true or false based on whether the package volume exceeds 1,000,000. To test this properly, I would include three test cases:
- Volume = 999,999.99 (Should return False)
- Volume = 1,000,000.00 (Should return True)
- Volume = 1,000,000.01 (Should return True)

Similarly, I’d test edge values around the mass threshold of 20 for the `heavy` property.

In addition, I would write system-level tests simulating realistic use cases (user story tests), such as creating a package, sorting it, and verifying it ends up in the correct stack. This broader integration testing is out of scope for the submission and would take additional time beyond what’s suggested.

## Thank You :)

Thank you for taking the time to review my submission. Thoughtful AI seems like an incredible company, and I hope to hear from you all soon!

# CSC436_Programming_Assignment1

## How to run
All you need is your command line and python3 installed all the library used are the default library that comes with python3

To run you use the following command:
"py main.py {R} A B C D E {F} A,B C,D D,E"
- replace {R} with the number of attributes in relation
- A B C D E is the relation variable, you must seperate individual variable by space. A single attribute must be represented by a single character variable.
- replace {F} with number of functional dependencies
- A,B C,D D,E are the functional dependencies, the comma represents => so these translate into A => B, C => D, and D => E

## Examples
Given R = (ABCDE), F = {A=>C, E=>D, B=>C}
to find the candidate key you will run:
- py main.py 5 A B C D E 3 A,C E,D B,C

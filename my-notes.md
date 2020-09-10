# Notes For Session #2
> - **Remember to record the session**
> - **Remember to pause during the break**
- Brief self-introduction of the students who did not get a chance to speak.
- Assignment 01 Q & A and the course in general
    - Text book: SECOND edition
    - Students in this course have different level of experience in Python. 
        - I will do my best to accommodate everyone
        - Students also should help each other 
- Tips 
    - Python is case-sensitive
    - Keep four spaces for indeentation
    - Remember colon ":" at the end of "if", "for", "with open", try/except statement and indent lines that follow
    - In Jupyter notebook, when you are stuck (for instance, in a infinite loop), shut down the kernel and restart it.
    - In Python interactive shell, type "exit()" or "quit()" to get out. Don't forget the parenthesis.
    - When running a Python script, you are stuck (for instance, in a infinite loop), type CTRL + C.
    - Be aware of your current directory and where your files are.
    - Dont' try to rember the syntax. You can alway Google the answer. 
- Rules for assignment submission
    - Two days grace period after the due day
    - Lose half of the total points after the grace period 
    - Exception: Communicate prior to due day with legitimate reasons. 
- Python environments
    - Show the free env list
    - pythonanywhere.com
    - Google Colab
- Python Fundamentals 
    - Show the Python summary first 
    - Data types
    - Control flows
    - Inputs/outputs
    - Functions
- Assignment #2
- Individual Projects

# Prep Notes for Tutorial Session
## My Pep talk
- Python is fundamental, You must master it before you can move on to more advanced topics such as ML, NLP, EDA, Visualization, and Big Data. 
- No short cut. Must work extra hard in a continuous and consistent way, day in and day out for a long period of time, months and years.
- If you fail data 690, you will have little chance to succeed in other courses. 
- We can't call ourself a Data Scientist, if we are not a hardcore Python programmer.
- Time is precious and no much tiime left to catch up if you are behind. 
- The most important quality in a students is the combination of curiosity and work ethics. You must have both to really call yourself a student. 
- I am here to help only if you have the inner drive to help yourself. 
## Python
- Collections
    - list is the most used collection. Make it your BFF
    - create a new empty list and use append() function to add elements
- for loops
- while loops
- if/elif/else
- try/catch
- Statistics vs statistics
- Population vs Sample
## Programming best practices
- Break down complext problem into small pieces or pphases (snippets, functions, modules)
- Make one piece work first - Minimal Viable Product (MVP)
- Incrementally add more capabilities. 
- Refine and restructure as you go (In Software Engineering, it is call "refactor"), always strive to simplify.
- "given two solutions, only the simpler one is correct." 

# Session 3 Prep Notes
- Assignment #2 
    - Prefer Google Colab - The button on top of a Jupyter notebook is very convenient
    - How to create a new folder (tricky)
- Talk about coding standards and how to structure Jupyter notebook files for readability.
    - Don't put all your code in one cell - break them up in several logical parts and place them in different cells
    - Indent only necessary. 
    - Pay attention to readability/maintainability/reusability
    - Pay attention to usability (user experience, user-centered design, human-factor)
- Example
```python
import math 
num_list = []

while len(num_list) < 10:

    num = input(f"\nplease enter an integer ({len(num_list) + 1} of 10): ")

    try:
        num = int(num)
        num_list.append(num)
    except:
        print("\nYou have entered a non-integer. Please try again.")

    print("\n", num_list)

    total = 0
for num in num_list:
    total += num

average = total/len(num_list)
```
- Example 2
```python

import math
try:
    int_list=[]
    for i in range(1,11):
        inte=int(input())
        int_list.append(inte)
    print("Minimum of integers:",min(int_list))
    print("Maximum of integers:",max(int_list))
    print("Range of integers:",min(int_list),"-",max(int_list))
    print("Mean of integers:",(sum(int_list)/10))
    print("Varience of integers:",sum((i - (sum(int_list)/10)) ** 2 for i in int_list) / len(int_list))
    print("Standard deviation of integers:",(sum((i - (sum(int_list)/10)) ** 2 for i in int_list) / len(int_list))**0.5)
        
except:
    print("Please enter integers only")
```

- The most important programming skill is looping. 
    - Most useful mechanism for looping is through collections.
        - range()
        - List
- The most used functions are string manipulation functoins in Data Analysis
    - strip(), lstrip(), rstrip()
    - replace()
    - find()
    - startswith()/endswith()
- Functions
    - User defined
    - Anonymous/lambda
- File Input/Output
- In class exercise: Copy the user names of this class from BB and to extract out first name, last name, and middle name.
- In class exercise: Practice input/output and data cleansing
    - copy data from https://www.genealogybranches.com/censuscosts.html to a text file
    - read the text file
    - read line by line and clease the data elements
    - Output the cleansed data to a file using CSV format
- Talk about assignment #3

# Session 3 Prep Notes
- Assignment #2 
    - A few turned in homework but the code did not work
    - Interactive tutorials and videos online. Please take advantage of them and catch up soon. Time is running out.
    - Make sure you notebook include results including error corrections 
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

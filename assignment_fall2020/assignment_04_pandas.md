# Assignment 04 - Using Pandas
1. Use Pandas read_html() function to retrive the tables as dataframes from the web page: https://www.genealogybranches.com/censuscosts.html
2. PAndas returns two dataframes. Find out which one of the two contain the data and use that one for further processing.
3. Display the dataframe to explore the data (rows, columns, etc.) and determine the data quality (bad rows, bad columns, bad elements, null values, etc.)
4. Document the data quality issue using a Markdown cell so the reader understands what the problems are.
5. Write a function named cleanse_year() that takes a string as input and removes any "*" in the string and return the cleansed string.
6. Cleanse the column "Census Year" using the function cleanse_year() and Pandas's apply() function.
7. Repeat this process for column "Total Population", 	"Census Cost", 	"Average Cost Per Person".
8. After all columns are cleansed, save the clenased dataframe to a file named "census_cost_cleansed.csv" using CSV format.
9. Use Pandas to read the saved cleansed file and explore to make sure it is clean. 

Give yourself a pad on the back. Now you get a feel of how wonderful Pandas is and how powerful the combination of apply() and user-defined functions are.

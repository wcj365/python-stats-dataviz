# Assignment 06 - Using Pandas
## Instructions
- This assignment is a re-do of assignment 04. We use Pandas and functions instead. 
- This assignment is a simple example of an important and complex process of "web scraping" to collect data.
- You get to use the simple and convenient read_html() from Pandas to extract **HTML tables** from web pages. 
    - **NOTES: The function return a list of data frames, one for each table in the HTML page.**
- We had walked through the process during last sesssion. The sample solution is here:
- https://github.com/wcj365/python-stats-dataviz/blob/master/pandas_apply.ipynb
- You will try to do it on your own and use the sample solution when you get stuck. 
- Make sure you user **Markdown cells** to document the process and its steps.
## Requirements
1. Use Pandas read_html() function to retrive the HTML tables as dataframes from the web page: https://www.genealogybranches.com/censuscosts.html
2. Find out how many HTML tables Pandas retrieves from the web page. Find out which dataframe contain the data and use it for further processing.
3. Display and explore the data (rows, columns, etc.) and determine the data quality (bad rows, bad columns, bad elements, null values, etc.)
4. Document the data quality issues using a Markdown cell so the reader understands what the problems are.
5. Write a function named cleanse_year() that takes a string as input and removes any asterisks in the string and return the cleansed string. Test the function by using test strings (for example, "1989*", "20*10")
6. Cleanse the column "Census Year" using the function cleanse_year() and Pandas's apply() function.
7. Repeat this process for column "Total Population", 	"Census Cost", 	"Average Cost Per Person". (define, test, and apply the function)
8. After all columns are cleansed, save the clenased dataframe to a file named "census_cost_cleansed.csv" using CSV format.
9. Use Pandas to read the saved cleansed file and explore to make sure it is clean. 
10. Updload both the Jupyter notebook and the cleanse data file to GitHub and submit the GitHub link in BlackBoard.

> Give yourself a pad on the back. Now you get a feel of how wonderful Pandas is and 
> how powerful the combination of apply() and user-defined functions are.

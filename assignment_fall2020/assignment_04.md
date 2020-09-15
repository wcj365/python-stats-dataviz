# Assignment 04
1. Write code to open the file "census_cost.txt" and read all lines into a list of strings each representing a line in the text file.
2. Since the first two lines are not used, remove them so we only keep the useful data.
3. Extract the column **"Census Year"** from the data and assign them to a list named **year_list**. Remove the "*" from the last element "2010*". Print the cleansed year_list.
4. Extract the **"Total Population"** column from the data and assign them to a list named **"pop_list"**. Remove the "," from the numbers since Python doesn't recognize them.
Print the cleansed "pop_list".
5. Extract the **"Census Cost"** column from the data and assign them to a list named **"cost_list"**. Remove the ",", and "$", and "Billion".
Make sure to add the "0"s to the numbers from which you stole "Billion" dollars. Print the cleansed cost_list.  
6. Extract the **"Average Cost per Person"** column from the data and assign them to a list named **"avg_list"**. Remove the "cents", and "$".
Make sure to divide the numbers in cents by 100 so that all numbers are measured in dollar. Print the cleansed avg_list.
7. Calculate the min, max, mean, and standard deviation of the census cost over the years and print it.
8. Calculate the min, max, mean, and standard deviation of the average cost per person over the years and print it.
9. Save the cleansed data to a text file named "cleansed_census_cost.txt" in the same format as the original text file except that the numbers have been cleansed.
10. Give yourself a pat on the back. Good job! Now you what data scientists do most of time: Data Cleansing.

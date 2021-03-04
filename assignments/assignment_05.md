# Assignment 05
Note: You will be using Pandas for this assignment.
1. Explore College Scorecard website - https://collegescorecard.ed.gov/ 
2. Explore College Scorecard Data web page - https://collegescorecard.ed.gov/data/
3. Download and read the documentation - https://collegescorecard.ed.gov/assets/FullDataDocumentation.pdf
4. Download the dataset - https://ed-public-download.app.cloud.gov/downloads/CollegeScorecard_Raw_Data.zip (265MB Zip File)
5. Unzip the file into a folder in your personal computer (there are many files, one for each school year)
6. Upload the 2017-2018 school year file "MERGED2017_18_PP.csv" to Colab/Deepnote or any Cloud environment of your choice (you can use your local environment too) and create a Jupyter notebook to explore the dataset:   
    - how many colleges or rows?   
    - how many variables or columns?   
    - Look at the first 5 colleges   
    - look at the last 5 colleges
    - Look at a random sample of 5 colleges    
7. Since there are too many variables to explore, many of which are not interesting. Create a smaller data frame with the following 9 variables:
    - UNITID
    - INSTNM
    - CITY
    - STABBR
    - ZIP
    - ADM_RATE
    - UGDS
    - TUITIONFEE_IN
    - MN_EARN_WNE_P10 
8. Download and read (use naked eyes, no coding) the data dictionary file - https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx
9. Find out the definition of the above 9 variables and document the definitions in the Jupyter Notebook in a Markdown cell so that the readers of your notebook
will know the meaning of these variables.
10. Explore the smaller data frame
    - Look at the first 10 colleges   
    - look at the last 10 colleges
    - Look at a random sample of 10 colleges  
    - Find and display UMBC 
    - Find Univ. of Maryland College Park
    - Find and display Loyola College Maryland
    - Find and display Johns Hopskins
    - Calculate the min, max, and average in-state tution of the above four institutions.
 11. Filter the smaller dataset further to only keep colleges from Maryland, Virgina, Washington DC, Delaware, and Pennsylvinia. Save the filtered dataset to a new file named "Five_States_Colleges.csv" for future analysis. Upload this file to your GitHub along with the notebook.
 
**Note:** 
- Make sure your notebook file is well organized using Markdown and code comments.

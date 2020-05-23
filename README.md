
```
    A visitor to New York City asked a passerby for directions to the city's famous classical music venue:

    Visitor: Excuse me, how do I get to Carnegie Hall?

    Passerby: Practice, practice, practice!
```
# Statistical Analysis and Data Visualization with Python
Online Class WebEx: http://umbc.webex.com/meet/jaywang
## Course Summary
Statistical Analysis, Data Visualization, and Python Programming All in One Place with Hands-on Practices. 
## Three Ways to Run Python Code and Free Cloud-based Tools
- Use Interactive Python Shell (Interpreter) 
    - python.org 
    - No registeration is required
- Run Python Scripts through Command Line
    - pythonanywhere.com
    - Requires account registeration
    - Need basic Linux familiarity
- Use Jupyter Notebooks
    - Google Colab
        - Plus: Seemless integration with GitHub
    - Kaggle.com
        - Plus: Data science community with public datasets and notebooks for learning 
    - notebooks.ai 
        - Plus: Acess to Linux terminal to run Python Scripts and Python Webapps  
    - Microsoft Azure Notebook
## Four Levels of Python Code
https://m.facebook.com/story.php?story_fbid=2596321403939440&id=1815765878661667
1. Syntax (most basic programming requirements)
2. Idiom (use of .join for string concatenation)
3. Design Patterns (best practices and approaches to common problems and issues)
4. Architectural (Overall project structure)

Most books and courses teach level 1 and 2 and rarely touch on level 3 and 4.

## Four Paradigms of Python Programming
https://blog.newrelic.com/engineering/python-programming-styles/
- Imperative
- Procedural
- Object-oriented
- Functional
## Four Major Components of a Data Science Project and Your Responsibility
- **Written Code** - Solely your responsibility - Make sure it is clean, correct, and commented (3C rule)
- **Source Data** - Primary data is your responsibity. You have no control over secondary data so be careful in the selection and cleansing.
- **Existing Libraries** - You have no control on existing libraries/algothorithms so be careful in selecting and using them.
- **Interpretation of Results** - Be careful about what is objective and what is subjective and what data exhibit and what experts know.

The one thing you have absolute control is **the code you write**. Make sure don't write bad code (complicated, incorrect, and undocumented code), so-called **spaghetti code**.

[Wikipedia's Definition of Spaghetti Code](https://en.wikipedia.org/wiki/Spaghetti_code): 

> *"Spaghetti code is a pejorative phrase for unstructured and difficult-to-maintain source code. Spaghetti code can be caused by several factors, such as volatile project requirements, lack of programming style rules, and insufficient ability or experience."*

## Jupyter Notebooks
The name Jupyter comes from the fact that it supports writing code in three popular languages:
- **Ju**lia
- **Pyt**hon
- **R**

Julia and R are popular for statistical analysis and data science. Python is a more generic programming language that happens to be popular in data science as well, though Python is good for all kinds of development, not just data science.
## Data Visualization Six Steps
1. Define Problem and Ask Questions
2. Define Data Source and Elements
3. Tidy up Data (Normalize "messy" data so that is is "Tidy". )
4. Summarize Data (Summarize/Tablulate, descriptive statistics)
5. Visualize Data (static and interactive)
6. Interpret and Communicate Results

Check out this [paper](https://www.jstatsoft.org/article/view/v059i10) for data tidying.

All Six steps must be guided by domain knowledge, principles, and purposes. 

## Data Visualization - Plots/Charts
- One Variable
   - Categorical Variable (frequency table)
       - Bar chart/Pareto Chart (sorted)
       - Pie Chart (Avoid it when there are two many categories)
   - Numerical Variable (discrete or continuous, frequency distribution)
       - Boxplot
       - Histogram
       - Line Chart
       - Area Chart
   - Textual Variable/Data
       - Wordcloud
- Multiple variables
   - Two categorical variables (contingency table, pivot table)
       - Stacked Bar Chart
       - Grouped Bar Chart
   - Two numerical variables
       - Scatter Plot
       - Bubble Chart (Scatter plot with varying size of dots based on the third numerical variable)
       - Motion Chart (Interactive scatter plot reflecting the trend on a third time series categorical variable such as quarter, month)
       - Scatter Plot with varying colors and Shapes of dots/marks reflecting additional categorical variables (dimensions)
## My Pedagogy
- I put practice above PowerPoint. I don't focus on syntax and mechanics.
- I share with students how I learn. I show them how to learn on their own so that they become life-long learners without relying on teachers or gurus. 
- I offer no fishes nor fishing gears. I show students where and how to find them.
- The Internet is the biggest fish pond and Google is the best fishing gear. 
- Curiocity may kill a cat, it sure makes a student.
## References
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [AP Statistics Tutorial](https://stattrek.com/tutorials/ap-statistics-tutorial.aspx)
- [Practice Python](https://www.practicepython.org/)
- [Python Exercises, Practice, Solution](https://www.w3resource.com/python-exercises/)
- [A Visual Intro to NumPy and Data Representation](http://jalammar.github.io/visual-numpy/)
- [A Gentle Visual Intro to Data Analysis in Python Using Pandas](http://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/)
- [Summarising, Aggregating, and Grouping data in Python Pandas](https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/)
- [Visualizing Pandas' Pivoting and Reshaping Functions](http://jalammar.github.io/visualizing-pandas-pivoting-and-reshaping/)
- [Data Visualization with Python](https://www.shanelynn.ie/data-visualisation-in-python-pycon-dublin-2018-presentation/)
- [From Data to Viz](https://www.data-to-viz.com/)
- [Data Visualization Best Practices](https://mode.com/analytics-dispatch/data-visualization-best-practices/)
- [Introduction to Exploratory Data Analysis in Python.ipynb](https://github.com/ilyagerner/pandas/blob/master/Introduction%20to%20Exploratory%20Data%20Analysis%20in%20Python.ipynb)
- [Object-Oriented Programming in Python vs Java](https://realpython.com/oop-in-python-vs-java/)
- [Ask, Acquire, Analyze, Apply, Announce, Assess](https://qcc.qlik.com/mod/resource/view.php?id=21115) 
- [A First Course in Data Science](https://arxiv.org/pdf/1905.03121.pdf)

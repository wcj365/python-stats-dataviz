# Assignment 06 Data Visualization

## 1 - Using Matplotlib

https://github.com/srisaisrikar/Data_690_assignments/blob/main/Assignment_06/Assignment_06.ipynb

## 2 - Using Seaborn

https://github.com/ramteja384/690_Assignment6/blob/main/690_Assignment_06.ipynb

## 3 - Using Plotly

https://github.com/Jyothsna9618/Jabboju1/blob/main/Assignment_06/assignment_06.ipynb

## 4 - Using Plotly Express

https://github.com/Priyankabalumuri/690/blob/main/assignments_06/assignment_06.ipynb

## 5 - Calculation of Growth Rate

### 5.1 - Use core Python

```

tut_fee = []
tut_fee.append(np.nan)
for x, y in zip(tutionfee, tutionfee[1:]):
    tut_fee.append((y - x) / x * 100)

tut_fee

Percent_list_tut = [round(item, 2) for item in tut_fee]

```

```
def growth_rate(tuition_list):

    # initialize empty list to hold year over year percent change
    change_list = []

    # loop through each year, calculate year over year percent change, and add to list
    for i in range(len(tuition_list) - 1):
        change_list.append((tuition_list[i+1] - tuition_list[i]) / tuition_list[i])

    # round to 2 decimal places
    change_list = [round(change_percent, 2) for change_percent in change_list]

    return change_list
    
 
 # convert column to list
tuition_list = list(df_JHU["TUITIONFEE_IN"])

# call function and assign results to list
change_list = growth_rate(tuition_list)

print(change_list)

df_JHU["PCT_CHANGE"] = np.nan
df_JHU.PCT_CHANGE[1:] = change_list
df_JHU

```

### 5.2 - Use Numpy Array

```

a = np.array(TUITIONFEE_IN_list, dtype=float)
per_change=np.diff(a) / a[:-1] * 100.
per_change

rounded_list = [round(item, 2) for item in per_change]
print(rounded_list) 

```


## 6 - Python Data Visualization Ecosystem

There are no shortage of data visualzation libraries in Python. Matplotlib, Seaborn, Plotly, Altair, Bokeh are among the most popular ones. 

Visualization libraries can be classified 
using two dimensions - Static vs Interactive and Low-level vs High-level.

Static libraries only produce static visualizations that are still images without support for human interaction.  Interactive libraries produces visualizations that are dynamic and allow users to interact via mouse movement and screen touch. Interactive visualizations are great tools for exploratory data analysis. Interactive visualizations also support the download of the interactive chars
as static images for embedding in publication. 

Low-level libraries provide more options and flexibility for customization but are more complex and require steeper learning curve. High-level libraries are easier to learn, simpler to use, and require fewer lines of code. 

Table 1 provides a summary of Python data visualization libraries along these two dimensions.

|                | Static     | Interactive |
|----------------|------------|-------------|
|**Low-level**   | Matplotlib | Plotly      | 
|**High-level**  | Seaborn    | Plotly Express, Altair, Bokeh | 


Matplotlib is the first python library for data visualization and it is modelled based on a commercial visualization and modelling software MatLab. As a low-level library, Matplotlib is rich in functionalities and features which come with the downside of complexity and learning curve. Many data engineers and scientists in the Python camp choose Matplotlib as the first choice for learning and using data visualization. 

Seaborn is a high-level library built on the foundation of Matplotlib. It is simpler to learn and essier to use than Matplotlib. Since it is based on Matplotlib, you can always resort to Matplotlib for more advanced and complex use cases where Seaborn falls short.

The main disadvantage of Matplotlib and Seaborn is that their visualizations are static and not interactive. 

Interactivity is where Plotly and Plotly Express shine. Similar to Matplotlib and Seaboran. Plotly is a low-level library while Plotly Express is a high-level library built on the foundation of Plotly.


## 7 - Benefit of Plotly EXpress: Best of Both Worlds

### 7.1 - Both Static and Interactive

With Plotly Express, you can create highly interactive publication-quality visualizations. The visualizations can be published to a web site for sharing across the Internet. In addition, the visualizations can be exported as static images for embedding in online blogs, business reports, academic papers, presentations, and books.  
#### 7.2 - Simple to Code yet Highly Customizable

As depicted in table 1, Plotly is a low-level interactive library and Plot Express is a high-level interactive library.  Plotly Express is built on top of Plotly and enjoys the best of both worlds. Plotly Express is simple yet powerful. It provides tens of built-in interactive charts with just one line of code while providing advanced functionality and customizations via access to the low-level functions of Plotly. 

### 7.3 Backed by a viable Company and a lively Ecosystem 

Plotly is also the name of a Toroto-based company which builds several related open source products based on Plotly.js, a Java Script library for interactive data visualization. These products include Plotly, Plotly Express, Dash, and Chart Studio. 

Dash is a Python library for generating interactive dashboards using Plotly and Plotly Express. Interactive dashboards can be published as websites for sharing on the Internet.

Plotly Chart Studio provides registered users an online environment for authoring Plotly visualizations with drag-and-drop design tool without writing code. The visualizations are hosted on the Cloud and can be shared. Users can also write code using Plotly Express to save the visualizations to the Chart Studio's Cloud environment for sharing.

For more information about Plotly, Plotly Express, Dash, and Chart Studio, check out the company website:
http://www.plotly.com

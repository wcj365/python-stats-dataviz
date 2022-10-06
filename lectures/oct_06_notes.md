# Oct 6 Session Notes

## Assignment 04

Student solutions:

- https://github.com/ramteja384/Assignment4_690/blob/main/690_Assignment4.ipynb (Use of for loops)
- https://github.com/Jyothsna9618/Jabboju1/blob/main/Assignment_04/assignment04.ipynb (str.contains, isin)
- https://github.com/manishbhima/Data690_DVS/blob/main/assignment_04/assignment_04.ipynb (use query)
- https://github.com/konkasivaji/690-stats-and-visulaization/blob/main/Assignment_04/assignment_04.ipynb (concat)
- five_state_colleges = data[(data['STABBR']=='MD') | (data['STABBR']=='VA') | (data['STABBR']=='DC') | (data['STABBR']=='DE') | (data['STABBR']=='PA')]
- df_city= df_new.loc[df['STABBR'].str.contains("MD|VA|DC|DE|PA")]
- Prefered: df2 = df[df["STAABR"].isin(["MD", "VA", "PA", "DC", "DE"])]

## Tips

- df.to_csv("Five_States_Colleges.csv", index=False)  (don't save the index as a column in the output)
- df_read_csv(... usecols=[list of columns]) to reduce memory usage

## Assignment 5

- https://github.com/YHarshitha1997/DATA-690-STATS-FALL-2022/tree/main/ASSIGNMENT-05 
- https://github.com/konkasivaji/690-stats-and-visulaization/tree/main/Assignment_05
- https://github.com/kavyasreemaniga/DATA_690/tree/main/Assignment_05
- https://github.com/Susrinivas/Python-Stats-and-Visualization/tree/main/Assignment_05

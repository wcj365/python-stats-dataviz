# Assignment 07

## Comparing Regions

Some of you did not use data from all countries.

## Groupby

Two approaches: as_index=False vs reset_index()

- df8 = df7.groupby('Region', as_index=False)['value'].sum()
- df8 = df7.groupby('Region')['value'].sum().reset_index()
 
Sort the values for bar chart

- df8 = df8.sort_values(by="value", ascending=False)

## Title for Axis

```
fig.update_layout(
    xaxis_title="GDP per Capita",
    yaxis_title="Life Expectancy")
```

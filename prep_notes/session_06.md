```python
midatl_colleges_data=subset_college_data.loc[subset_college_data['STABBR'] == 'MD'].append(subset_college_data.loc[subset_college_data["STABBR"]=='VA']).append(subset_college_data.loc[subset_college_data['STABBR'] == 'DC']).append(subset_college_data.loc[subset_college_data['STABBR'] == 'DE']).append(subset_college_data.loc[subset_college_data['STABBR'] == 'PA'])
midatl_colleges_data
```

This can be simplified by using isin() function.
```python
df = df[df_2['STABBR'].isin(['MD','VA','DC','DE','PA'])]
```

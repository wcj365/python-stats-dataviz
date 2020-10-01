```python

# The following function gets rid of any asterisks, and converts the value to an integer.

def cleanse_year(x):
  y=x
  for k in x:
    if k=='*':
      y=int(x.replace('*',''))
  return y
```

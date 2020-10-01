## Session 7 Prep Notes

### Assignment #6

```python

# The following function gets rid of any asterisks, and converts the value to an integer.

def cleanse_year(x):
  y=x
  for k in x:
    if k=='*':
      y=int(x.replace('*',''))
  return y
```

```python

def cleanse_avg(raw_avg):
  
  if raw_avg.find('cents') != -1:                    #if you see 'cents'
    new_avg=float(raw_avg.replace('cents',''))/100   #replace it with nothing, change to a float, and divide by 100
  elif raw_avg.find('$') != -1:                      #if you see a '$'
    new_avg=raw_avg.replace('$','')                  #replace it with nothing
  else: new_avg=raw_avg
  return new_avg
```

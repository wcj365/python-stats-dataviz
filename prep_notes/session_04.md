## Prep note for Session 4
- Many solutions to the assignment 3
### Solution example 1 - USe nexted loops
```python
for i in range(1, 11):
  for j in range(1,11):
    num = random.randint(0, 9)
    if (j == 10):
      print(num)
    else:
      print(num, end=" ")
```
### Solution example 2 - Using a single loop
https://github.com/steinruck/WANG-690-FALL-2020/blob/master/Assignment_03/Exercise_03.ipynb
```python
numbers_list = []
for x in range(0, 100):
    numbers_list.append(random.randint(0,9))
    
counter = 0
for y in numbers_list:      # Jay Comment: use a single loop instead of nested loops.
    print(str(y), end=' ')
    counter += 1
    if counter == 10:
        counter = 0
        print()
```
### Solution example 3 - the lean and mean (least SLOC)
https://github.com/YM53858/DATA-690-WANG/blob/master/Assignment-03/Assignment-03.ipynb
```python
import numpy as np

A = np.random.randint(10, size=(10, 10))

for row in A:
    print(" ".join(map(str,row)))   # Jay comment: use advanced map() function.
```

### Solution example 4 - use List Comprehension
```python
m = []  # create an empty list for 10 lines.
for k in range(10): # 10 lines.
        #m.append(a) # move to the final line.
    a = [] # creat an empty list for 1 line. 
    for i in range(10): # 10 elements in onw line.
        j = random.randrange(10) 
        a.append(j) 
    print(*a)
    m.append(a) #form final 10*10 matrix.

for i in m: # the indelted for loop inside the description of element. 
    n = ["@" if x%2 else x for x in i]
    print(*n, sep = ' ')
```

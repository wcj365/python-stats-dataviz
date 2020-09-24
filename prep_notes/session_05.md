# Preparation Notes for Session 5
## Talk about individual project
## Talk about assignment 4
- Coalesciing multiple lists 

```python
fileOut = open(fileNameOut, 'w') 
fileOut.writelines(top2_list) 
length= len(avg_list)
for index in range(0,length):
    line= year_list[index] + "," + pop_list[index] + "," + str(cost_list[index]) + "," + str(avg_list[index]) + "\n"
    fileOut.writelines(line)
fileOut.close()
```
- The following works but is not the best practice

```python
file = open(fileNameIn, 'r') 
line_list = file.readlines() 
print(line_list) 
file.close()
```
- The best practice is to use "with open() as" which automatically close the file at the end.

```python
with open(fileName, 'rt) as f:
    line_list = file.readlines() 
    print(line_list) 
```
## Use of functions   
## Use Pandas for assignment 4
- use of functions
- use apply
## Talk about assignment 05
- How to query dataframe to select desired rows?
- How to select desired columns 
- How to remove wanted columns?


# Assignment 03
## The Problem:
Write a program that generates 100 random integers between 0 and 9. 
1. Print them in a 10 by 10 matrix neatly arranged like the following (one space between each number):
```
5 1 5 6 2 7 8 6 4 2 
2 3 7 0 6 9 2 4 2 8 
0 0 8 6 4 1 7 2 7 6 
0 1 9 0 0 8 5 8 6 8 
4 1 0 5 5 7 4 6 4 4 
6 0 2 0 1 9 8 2 3 9 
4 0 4 8 1 7 6 6 2 1 
1 7 6 8 5 4 1 9 6 7 
6 4 7 9 9 3 8 2 6 1 
9 0 6 4 0 1 0 6 9 9 

```
2. If the random number is an odd number, print "@" instead.  like the following:
```
@ @ 0 2 6 @ 8 8 0 0 
@ 4 @ 4 4 @ 2 @ 2 2 
@ 6 8 @ @ @ 0 @ 0 @ 
2 6 @ 0 @ 2 @ @ 0 @ 
8 4 @ @ @ 0 @ @ 6 @ 
@ @ 4 6 @ @ @ 2 @ 2 
@ @ @ @ 4 @ @ 2 2 0 
@ 6 @ 0 0 8 @ 2 0 @ 
8 8 @ @ @ 0 0 @ 4 6 
@ 2 2 6 8 2 @ @ @ 6
```
3. Calculate and Print the total of each row like the following (use "*" to separate the total from the numbers):
```
7 6 5 8 8 0 7 6 0 1 * 48 
8 5 7 9 8 0 9 3 0 1 * 50 
4 0 3 5 3 9 0 8 3 9 * 44 
3 5 5 3 8 3 4 3 2 2 * 38 
7 7 4 1 2 7 2 3 0 8 * 41 
3 9 7 7 0 9 4 0 6 5 * 50 
1 9 7 1 3 0 0 1 4 5 * 31 
4 4 0 6 7 4 5 6 9 3 * 48 
2 1 1 4 2 0 1 2 9 2 * 24
2 1 6 7 7 8 1 0 0 4 * 36
```

4. Optional: Surround the matrix with asterisks (*) like the following:
```
***********************
* 5 1 5 6 2 7 8 6 4 2 *
* 2 3 7 0 6 9 2 4 2 8 *
* 0 0 8 6 4 1 7 2 7 6 *
* 0 1 9 0 0 8 5 8 6 8 *
* 4 1 0 5 5 7 4 6 4 4 *
* 6 0 2 0 1 9 8 2 3 9 *
* 4 0 4 8 1 7 6 6 2 1 *
* 1 7 6 8 5 4 1 9 6 7 *
* 6 4 7 9 9 3 8 2 6 1 *
* 9 0 6 4 0 1 0 6 9 9 *
***********************
```
## The Requirements:
- You should program and test the solution in Jupyter notebook:
- Save/upload the notebook file to your GitHub repository
- Submit the link of your GitHub repo to BB.

## Hints:
- You can use Python standard library random to generate one random number at a time 
- Alternatively you can use NumPy random library to generate 10 numbers at a time or 100 random number altogether in one shot.
- You are likely to use nested loop - a loop within in another loop since you are dealing with a 10 x 10 matrix.
- You will use modular operator (%) to determine if an integer is an odd number or an even number.
- Use the "end=" option of the print() function to avoid a new line after the print and also to add additional spaces. 
    - for example, print(9, end="   ") will print 9 followed by three spaces and not starting a new line.
- Think through the logic. Try simple things first. Don't make it too complicated. You only need a few lines of code.



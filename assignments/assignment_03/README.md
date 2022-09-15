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

4. Surround the matrix with asterisks (*) like the following:
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
5. Calculate and Print the total of each row and column like the following:
```
6  8  0  2  3  4  2  2  4  4  * 35 
3  7  5  8  9  7  4  8  6  0  * 57 
4  7  7  4  3  8  2  1  7  0  * 43 
7  8  1  3  0  8  4  7  9  2  * 49 
0  0  2  4  5  6  6  7  1  4  * 35 
3  7  0  0  7  3  3  2  1  6  * 32 
2  5  6  6  5  6  5  5  4  7  * 51 
9  2  7  5  5  9  2  4  7  9  * 59 
0  0  4  7  6  3  9  6  6  7  * 48 
0  1  6  5  2  7  4  1  6  4  * 36 
*  *  *  *  *  *  *  *  *  *  
34 45 38 44 45 61 41 43 51 43 
```
## The Requirements:
- You should program and test the solution in Jupyter notebook using Google Colab:
- Save/upload the notebook file to your GitHub repository.
- Submit the link of your GitHub repo to BB.

## Hints:
- You can use Python standard library random to generate one random number at a time. 
- You are likely to use nested loop - a loop within in another loop since you are dealing with a two-dimentional matrix.
- You will use modular operator (%) to determine if an integer is an odd number or an even number.
- You may Use the "end=" option of the print() function to avoid a new line and also to add additional spaces. 
    - for example, print(9, end="   ") will print 9 followed by three spaces and not starting a new line.
- Think through the logic. Try simple things first. Don't make it too complicated. You only need a few lines of code.

## Additional Guidance
1. Please don't use NumPy. Use the standard random library instead. 
2. Generate one row of 10 number using for loop. 
3. Generate 10 rows using another for loop.
4. Don't use print(a_list) function which displays unwanted brackets "[" and "]". 
5. Print one number at a time using a loop so that you have full control of what to print and how to print (adding spaces, summation, and other simbols). 
6. Experiment easy things:
    - For example, use random library to generate 10 numbers and print them one at a time in a for loop.
    - If it prints each number in a separate line, find a way to print them all in one line. 
    - If the numbers are next to each other without spaces, try to insert spaces (one or many) in between.
    - Try to print odd number using "@".
    - Try to add the 10 numbers to get a total and print the 10 numbers followed by "*" and the total.
    - After you can do all these simple things for 10 numbers, repeat this 10 times using for loop.
    - If you are having problem, email me with questions and/or set an appointment with one of the two tutors.

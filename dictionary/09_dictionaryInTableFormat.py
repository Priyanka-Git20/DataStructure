'''
@Author : Priyanka
@Date : 2022-04-23  1:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 1:40:00
@Title :Write a Python program to print a dictionary in table format
'''


dict1 = {(0, 0): 'priyanka', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'siya', (1, 1): 20, (1, 2): 'MySql',
         (2, 0): 'aditya', (2, 1): 21, (2, 2): 'OOPS with python'
         }

print("NAME   " , "  AGE   "   ,  "  COURSE  ")

# Iterate through the dictionary
for i in range(3):

    for j in range(3):
        print(dict1[(i, j)], end='   ')

    print()
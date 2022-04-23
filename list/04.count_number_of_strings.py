'''
@Author : Priyanka
@Date : 2022-04-19  1:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 2:00:00
@Title : Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
'''


def count_number_of_string():
    """
       Description:
            Count the number of strings whose first and last character are same and length is greater than or equal to two .
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """
    count = 0
    lst =  ['abc', 'xyz', 'aba', '1221']
    for i in lst:
        if len(i)>2 and i[0]== i[-1]:
            count += 1

    print("Count of strings whose first and last character are same and length is greater than or equal to two is ",count)

if __name__ == '__main__':
    count_number_of_string()

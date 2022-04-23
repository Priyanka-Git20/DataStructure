'''
@Author : Priyanka
@Date : 2022-04-19  2:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 3:00:00
@Title : Write a Python program to find the list of words that are longer than n from a given list of words.
'''


def list_of_longer_word():
    """
       Description:
            Finding the longest word.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    n = int(input("Enter the length "))
    lst = ["Yellow","Red","Green","Pink","orange","parrotGreen"]
    lst2 = []
    for i in lst:
        if len(i)> n:
            lst2.append(i)
    print("List of word whose lenghth longer than {} is {}".format(n ,lst2))


if __name__ == '__main__':
    list_of_longer_word()


'''
@Author : Priyanka
@Date : 2022-04-20  12:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 12:30:00
@Title : Write a Python program to get the number of occurrences of a specified element in an array.
'''


def get_number_of_occurence():
    """
      Description:
           Finding the number of occurrences of a specified element in an array.
      Parameter:
           None
      Return:
          Returning nothing but printing the result.
    """

    myarray = [12,2,3,5,7,12,0,34,12,4,6,8]
    print("Array is: ", myarray)
    print("Occurance of 1 in array is: ", myarray.count(12))

if __name__ == '__main__':
    get_number_of_occurence()


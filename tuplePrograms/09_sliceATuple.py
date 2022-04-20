'''
@Author : Priyanka
@Date : 2022-04-20  4:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 4:40:00
@Title :Write a Python program to slice a tuple..
'''


def slice_a_tuple():
    """
       Description:
            By using index slice the tuple and print it.
       Parameter:
            none
       Return:
           Returning nothing but printing result.
   """
    mytuple = (1,2,3,4,5,6,7,8,9,10,11,12,13)
    slice = mytuple[3:5]
    print("Tuple after slicing is",slice)
    slice = mytuple[:5]
    print("Tuple after slicing is",slice)
    slice = mytuple[1:]
    print("Tuple after slicing is", slice)
    slice = mytuple[-5:-1]
    print("Tuple after slicing is", slice)

if __name__ == '__main__':
    slice_a_tuple()

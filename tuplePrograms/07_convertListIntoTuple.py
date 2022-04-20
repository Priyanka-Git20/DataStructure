'''
@Author : Priyanka
@Date : 2022-04-20  4:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 4:10:00
@Title :Write a Python program to convert a list to a tuple.
'''


def convert_list_to_tuple():
    """
       Description:
            By using tuple function and passing list as parameter converting list inti tuple.
       Parameter:
            none
       Return:
           Returning nothing but printhing result.
   """

    lst = ["Apple","Orange",False,12,3.4]
    print("List = ",lst)
    mytuple = tuple(lst)
    print("Tuple = ",mytuple)

if __name__ == '__main__':
    convert_list_to_tuple()



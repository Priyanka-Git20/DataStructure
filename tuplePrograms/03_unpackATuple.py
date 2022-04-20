'''
@Author : Priyanka
@Date : 2022-04-20  1:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 1:50:00
@Title :Write a Python program to unpack a tuple in several variables.
'''

def unpack_tuple_in_variables():
    """
       Description:
            Extract the values back into a variable means unpacking is done and print it.
       Parameter:
            none
       Return:
           Returning nothing but printing message.
   """
    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits

    print("The value of the variable green is ",green)
    print("The value of the variable yellow is ",yellow)
    print("The value of the variable red is ",red)

    fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (green, yellow, *red) = fruits1  #when no. of value is greater than variable then we can add an * to the variable name and the values will be assigned to the variable as a list

    print("The value of the variable green is ", green)
    print("The value of the variable yellow is ", yellow)
    print("The value of the variable red is ", red)

if __name__ == '__main__':
    unpack_tuple_in_variables()
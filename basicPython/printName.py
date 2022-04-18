'''
@Author : Priyanka
@Date : 2022-04-18  10:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 11:00:00
@Title : Print the name in reverse order with space between them.
'''


def print_name():
    """
       Description:
           Taking input of first name and last name from user and printing the name in reverse order.
       Parameter:
            none
       Return:
           Returning nothing but print the message
   """

    firstName = input("Enter the first name")
    lastName = input("Enter the last name")
    print(lastName +" "+firstName)

print_name()
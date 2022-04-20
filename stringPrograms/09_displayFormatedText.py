'''
@Author : Priyanka
@Date : 2022-04-18  10:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 10:25:00
@Title :Write a Python program to display formatted text (width=50) as output.
'''

import  textwrap

def display_formated_text():
    """
       Description:
            First import the textwrap module then user write the paragraph. By using wrap()module print the paragraph with the width=50.
       Parameter:
            none
       Return:
           Returning nothing but printing the result.
   """

    txt = input("Enter the paragraph")
    text_wrap = textwrap.fill(txt,50)
    print(text_wrap)

if __name__ == '__main__':
    display_formated_text()

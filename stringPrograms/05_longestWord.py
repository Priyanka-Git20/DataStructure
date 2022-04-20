'''
@Author : Priyanka
@Date : 2022-04-18  9:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 9:15:00
@Title : Write a Python function that takes a list of words and returns the length of the longest one.
'''


def longest_word():
    """
       Description:
            Find the longest word.
       Parameter:
            none
       Return:
           Returning nothing but printing the longest word with the length.
   """

    txt = input("Enter a string")
    longest = 0
    for word in txt.split():
        if len(word) > longest:
            longest = len(word)
            longest_word = word

    print("Longest word is {} with the length {}".format(longest_word,len(longest_word)))

longest_word()
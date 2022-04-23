'''
@Author : Priyanka
@Date : 2022-04-23  1:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 1:40:00
@Title :Write a Python program to count the values associated with key in a dictionary.
'''

my_dict= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
print("Id Sum IS:", sum(i['id'] for i in my_dict))
print("success Sum IS:", sum(i['success'] for i in my_dict))
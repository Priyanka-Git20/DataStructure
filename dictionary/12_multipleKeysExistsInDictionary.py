'''
@Author : Priyanka
@Date : 2022-04-23  2:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 2:50:00
@Title :Write a Python program to check multiple keys exists in a dictionary.
'''

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}

print(thisdict.keys() >= {'brand', 'model'})
print(thisdict.keys() >= {'model', 1964})
print(thisdict.keys() >= {'year', 'brand'})
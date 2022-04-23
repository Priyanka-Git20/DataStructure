'''
@Author : Priyanka
@Date : 2022-04-19  2:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 2:30:00
@Title : Write a python program to check whether two lists are circularly identical.
'''

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
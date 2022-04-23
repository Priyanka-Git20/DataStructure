'''
@Author : Priyanka
@Date : 2022-04-18  3:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 3:00:00
@Title : Print the name in reverse order with space between them.
'''

import operator

my_dict = {1: 23, 2: 67, 4: 12, 3: 90}
print(my_dict)

# Sorting dictionary
sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))

# Printing sorted dictionary
print("Sorted dictionary in assending order is :", sorted_dict)

sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
print("Sorted dictionary in desending order is :", sorted_dict)
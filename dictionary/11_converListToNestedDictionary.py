'''
@Author : Priyanka
@Date : 2022-04-23  1:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 2:20:00
@Title :Write a Python program to convert a list into a nested dictionary of keys.
'''


def nested_dictionary(list):
    res_dict={my_list[i]:my_list[i+1] for i in range(0,len(my_list),2)}
    return res_dict

if __name__ == '__main__':
    my_list = ['a', 12, 'b', 2, 'c', 6, 'd', 9]
    print("Dictionary Become: ", nested_dictionary(my_list))


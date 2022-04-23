'''
@Author : Priyanka
@Date : 2022-04-18  3:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018  4:10:00
@Title :Write a Python script to concatenate following dictionaries to create a new one.
'''


def concatenate_dictionaries():
    """
       Description:
            By using the update method concatenate dictionaries to create one.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    # dir4 = {**dic1,**dic2,**dic3} #unpack operator
    # dir4=dic1|dic2|dic3 #merge operator
    # print(dir4)
    dic1.update(dic2)
    dic1.update(dic3)
    print("updated Dictionary :",dic1)

concatenate_dictionaries()



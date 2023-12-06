#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = {i for i in my_list}
    count = 0
    for i in new_list:
        count += i
    
    return count

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:20:58 2018

@author: Victor
"""
# This function the elements of a list on another list
def append_elements_on_a_list(list, updated_list):
    for element in list:
        updated_list.append(element.lower()) # All words must be preferably lowercase
    return updated_list

# This function receives a list of strings and returns ALL words (lowercased)
# from across all strings in the list of strings and returns all of these 
# words in a single list
def generate_string_list(list_of_strings):
    string_list = []
    for string in list_of_strings:
        # I need this temporary list to store the substrings from the current
        # string in the iteration
        temp_list = string.split()
        string_list = append_elements_on_a_list(temp_list, string_list)
    return string_list
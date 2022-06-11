#!/usr/bin/python3
def number_keys(a_dictionary):
    for i in sorted(a_dictionary):
        print("{:s}: {}".format(i, a_dictionary[i])) 

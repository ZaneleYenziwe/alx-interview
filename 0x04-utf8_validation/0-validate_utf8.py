#!/usr/bin/python3
""" 
Module for UTF-8 validation
"""

def validUTF8(data):
    """
    validate if a data set represents valid UTF-8 encoding
    """
    num_bytes=0
    for num in data: 
    bin_rep = format(num, '#010b')[-8
    if num_bytes == 0:
    if bin_rep.startswith('110'): 
    num_bytes = 1 elif bin_rep.startswith('1110'): 
    num_bytes = 2 elif bin_rep.startswith('11110'):
    num_bytes = 3 elif not bin_rep.startswith('0'): 
    return False
    else:
    if not bin_rep.startswith('10'):
    return False 
    num_bytes -= 1
    return num_bytes ==0

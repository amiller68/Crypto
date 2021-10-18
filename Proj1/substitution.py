""" This file contains a function that will attempt shifting the cipher n times, where n is the length of the ciper. It will
    print all possibilities.
"""


import string
from typing import NewType
import frequency

def shift():
    file = str(input())

    original_nums = []

    ctxt = open('ctxts/' + file).read()

    freq_dict = frequency.generate_frequency(ctxt)
    new_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
    
    print(new_dict)
    
    alpha_dict = {}
    
    for i,j in enumerate(ctxt):
        alpha_dict.setdefault(j, []).append(i)
            
    new_string = list(ctxt)
    print(alpha_dict)
    
    
    while True:
        letters = str(input())
        old_letter = letters[0]
        new_letter = letters[1]
        
        if old_letter in alpha_dict:
            for i in alpha_dict[old_letter]:
                new_string[i] = new_letter
            
        
        print("".join(new_string))

    
if __name__ == '__main__':
    shift()
    
        

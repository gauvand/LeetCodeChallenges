#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:05:53 2020

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0

 

Constraints:

    -231 <= x <= 231 - 1



@author: gauravanand
"""        
    
def reverse_myattempt(x):
    sign = ('-' if x < 0 else '')
    x_string = str(abs(x))
    # Handle length 0 input
    if len(x_string) == 0 or len(x_string) == 1:
        return x
    
    # Flip string 
    flipped = x_string[::-1]
    if flipped[0] == '0':
        flipped = int(sign + flipped[1:])
    else:
        flipped = int(sign + flipped[1:])
    # Handle non 32 bit integers
    if flipped < -2147483648 or flipped > 2147483647:
        return 0

    return int(sign + flipped)

def reverse_myattempt2(x):
    f = (x < 0)
    x_string = list(str(abs(x)))
    x_string.reverse()
    x = int(''.join(x_string))
    x = -1*f*x + (not f)*x # returns -x if f = True else returns x
    if abs(x) > 2**31:
        return 0
    return x
        
        
    
    
if __name__ == '__main__':
    print(reverse_myattempt2(123))
    
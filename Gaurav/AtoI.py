#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:02:08 2020

@author: gauravanand
"""

class Solution:        
    def myAtoi(self, s: str) -> int:
        # 1.  remove whitespace
        # 2.  take plus 
        pass
    def remove_whitespace(self, s):
        # recursive case
        if s[0] == " ":
            return self.remove_whitespace(s[1:])
        #base case
        else: 
            return s
if __name__ == "__main__":
    string = "   42"
    sol = Solution()
    print(sol.remove_whitespace(string))
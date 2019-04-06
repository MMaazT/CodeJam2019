# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 02:17:07 2019

@author: mmaaz
"""

T = int(input())

for t in range(1, T + 1):
    n=int(input())
    s=input()
    
    new=""
    for c in s:
        if c is 'S':
            new=new + 'E'
        else:
            new= new + 'S'
    print("Case #{}: {}".format(t,new))
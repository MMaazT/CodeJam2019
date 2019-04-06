# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 00:08:47 2019

@author: mmaaz
"""
import numpy as np
T = int(input())

for t in range(1, T + 1):
    n=int(input())
    s=input()
    #select indexes
    arr=[]
    a=np.zeros([n,n], dtype=int) #BUILD MATRIX
    a[0][0]=1
    x=0
    y=0
    #BUILD MATRIX
    for c in s:
        if c is 'S':
            x=x+1
            a[x][y]=1
        else:
            y=y+1
            a[x][y]=1
    z=[]
    i=0
    j=0
    while (i<n-1 or j<n-1):
        if(a[i][j]==1):
            if( a[i][j+1]==1):
                z.append('S')
                i=i+1
            elif(a[i+1][j]==1):
                z.append('E')
                j=j+1
        elif(a[i][j]==0 and a[i+1][j]==1):
            if(i+1==n-1):
                z.append('E')
                j=j+1
            else:
                z.append('S')
                i=i+1
        elif(a[i][j]==0 and a[i][j+1]==1):
            if(j+1==n-1):
                z.append('S')
                i=i+1
            else:
                z.append('E')
                j=j+1
                
    Z=''.join(z)
    print("Case #{}: {}".format(t,Z))
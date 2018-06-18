# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:59:42 2018

@author: Anders, s174008
"""

def Koch(lch):
    rstr = ""
    if lch == 'S':
        rstr = 'SLSRSLS'   
    else:
        rstr = lch    

    return rstr

def Sierpinski(lch):
    rstr = ""
    if lch == 'A':
        rstr = 'BRARB'   
    elif lch == 'B':
        rstr = 'ALBLA' 
    else:
        rstr = lch    

    return rstr




def stringOperationS(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Sierpinski(ch)

    return newstr

def stringOperationK(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Koch(ch)

    return newstr

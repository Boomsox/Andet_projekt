# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:42:36 2018

@author: Anders, s174008
"""

from Underfunktioner import Koch
from Underfunktioner import Sierpinski
from Underfunktioner import stringOperationK
from Underfunktioner import stringOperationS

def LindIter(System, N):
    
    if N > 8:
        print("The chosen number of iterations is higher than the allowed number (8).")
        LindenmayerString = ""
        return LindenmayerString
    
    
    elif N < 0:
        print("Negative numbers are an invalid value.")
        LindenmayerString = ""
        return LindenmayerString
    
    
    elif System == "Koch":
        startIter = "S"
        LindenmayerString = ""
       
        if N == 0:
            LindenmayerString = startIter
        else:
            for i in range(N):
                LindenmayerString = stringOperationK(startIter)
                startIter = LindenmayerString
        
        return LindenmayerString
        
        
    elif System == "Sierpinski":
        startIter = "A"
        LindenmayerString = ""
        
        if N == 0:
            LindenmayerString = startIter
        
        else:
            for i in range(N):
                LindenmayerString = stringOperationS(startIter)
                startIter = LindenmayerString
                return LindenmayerString
    
print(LindIter("Koch", 2))
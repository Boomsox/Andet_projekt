#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 11:32:12 2018

@author: Lasse Bruun
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from turtleGraphV2 import turtleGraph
from LindIter import LindIter

# Koch kurve:
kv = np.array([1/3**2, 1/3*math.pi])
kh = np.array([1/3**2, -2/3*math.pi])
ks = np.array([1/3**2, 0])

# Sierpinski kurve:
sv = np.array([1/2**4, 1/3*math.pi])
sh = np.array([1/2**4, -1/3*math.pi])
ss = np.array([1/2**4, 0])

# Koch kurve iteration 2
#turtleCommands = np.concatenate((ks, kv, kh, kv, kv, kv, kh, kv, kh, kv, kh, kv, kv, kv, kh, kv, ks))

# Sierpinski iteration 4
#turtleCommands = np.concatenate((ss, sv, sv, sh, sh, sh, sh, sv, sv, sv, sh, sh, sv, sv, sv, sv, sh, sh, sv, sv, sv, sh, sh, sh, sh, sv, sv, sh, sh, sh, sv, sv, sv, sv, sh, sh, sh, sv, sv, sh, sh, sh, sh, sv, sv, sh, sh, sh, sv, sv, sv, sv, sh, sh, sh, sv, sv, sh, sh, sh, sh, sv, sv, sv, sh, sh, sv, sv, sv, sv, sh, sh, sv, sv, sv, sh, sh, sh, sh, sv, sv, ss))

# Inputtet er en vektor, der skiftevis består af en længde og en vinkel, som
# til sammen udgør næste linje
def turtlePlot(turtleCommands):
    
    
    # Tomme vektorer, en række for x-værdier og en for y-værdier
    d = np.array((np.zeros(int(np.size(turtleCommands) / 2)+1), np.zeros(int(np.size(turtleCommands) / 2)+1)))
    x = np.array((np.zeros(int(np.size(turtleCommands) / 2)+1), np.zeros(int(np.size(turtleCommands) / 2)+1)))

    d[:, 0] = [1,0]
    x[:, 0] = [0,0]
    
    # Vinklerne og længderne sættes ind i hver deres vektor
    Vinkler = turtleCommands[range(1, np.size(turtleCommands), 2)]
    Længde = turtleCommands[range(0, np.size(turtleCommands), 2)]
    
    for n in range(1, int(np.size(turtleCommands) / 2) + 1):
        # Næste 'retningsvektor'
        d[:, n] = np.dot(np.array([[math.cos(Vinkler[n-1]), -math.sin(Vinkler[n-1])], [math.sin(Vinkler[n-1]), math.cos(Vinkler[n-1])]]), d[:, n - 1])
        
        
        # Næste punkt på grafen
        x[:, n] = x[:, n - 1] + (Længde[n-1] * d[:, n])    

    
    from MainScript import System;
    
#De forskellige plots med labels
    plt.plot(x[0, :], x[1, :])
    
    ##  Plot title
    plt.title("{:s} Curve, Iteration".format(System))
    
    
        # Koch Curve
    #if turtleCommands[2] == 1/3:
        #plt.title("Koch Curve, Iteration 1")
    
    #if turtleCommands[2] == 1/3**2:
    #    plt.title("Koch Curve, Iteration 2")
        
    #elif turtleCommands[2] == 1/3**3:
    #    plt.title("Koch curve, iteration 3")
        
    #elif turtleCommands[2] == 1/3**4:
    #    plt.title("Koch curve, iteration 4")
        
    #elif turtleCommands[2] == 1/3**5:
    #    plt.title("Koch curve, iteration 5")
        
    #elif turtleCommands[2] == 1/3**6:
    #    plt.title("Koch curve, iteration 6")
        
    #elif turtleCommands[2] == 1/3**7:
    #    plt.title("Koch curve, iteration 7")
        
    #elif turtleCommands[2] == 1/3**8:
    #    plt.title("Koch curve, iteration 8")
        
        
        # Sierpinski Curve
    #elif turtleCommands[2] == 1/2**1:
    #    plt.title("Sierpinski curve, iteration 1")
        
    #elif turtleCommands[2] == 1/2**2:
    #    plt.title("Sierpinski curve, iteration 2")
        
    #elif turtleCommands[2] == 1/2**3:
    #    plt.title("Sierpinski curve, iteration 3")
    
    #elif turtleCommands[2] == 1/2**4:    
    #    plt.title("Sierpinski curve, iteration 4")
      
    #elif turtleCommands[2] == 1/2**5:
    #    plt.title("Sierpinski curve, iteration 5")
        
    #elif turtleCommands[2] == 1/2**6:
    #    plt.title("Sierpinski curve, iteration 6")
        
    #elif turtleCommands[2] == 1/2**7:
    #    plt.title("Sierpinski curve, iteration 7")
        
    #elif turtleCommands[2] == 1/2**8:
    #    plt.title("Sierpinski curve, iteration 8")
    
    
    #Akselabels
    #plt.xlabel('Nice')
    #plt.ylabel('Ice')
    
    
    #Limits på plottet
    #plt.xlim([10, 60])
    #plt.ylim(ymin=0)
    
    #Viser grafen. 
    plt.show()
    
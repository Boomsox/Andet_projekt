#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 11:32:12 2018

@author: Lasse Bruun
"""

import numpy as np
import math
import matplotlib.pyplot as plt

# Inputtet er en vektor, der skiftevis består af en længde og en vinkel, som
# til sammen udgør næste linje
def turtlePlot(turtleCommands):
    
    # Tomme vektorer, en række for x-værdier og en for y-værdier
    d = np.array((np.zeros(int(np.size(turtleCommands) / 2)+1), np.zeros(int(np.size(turtleCommands) / 2)+1)))
    x = np.array((np.zeros(int(np.size(turtleCommands) / 2)+1), np.zeros(int(np.size(turtleCommands) / 2)+1)))

    # Startværdien sættes til Origo med retningsvektoren (1,0)
    d[:, 0] = [1,0]
    x[:, 0] = [0,0]
    
    
    # Vinklerne og længderne sættes ind i hver deres vektor
    Vinkler = turtleCommands[range(1, np.size(turtleCommands), 2)]
    Længde = turtleCommands[range(0, np.size(turtleCommands), 2)]
    
    
    # Herefter udregnes hver vinkel og længde af linjerne
    for n in range(1, int(np.size(turtleCommands) / 2) + 1):
        # Næste 'retningsvektor'
        d[:, n] = np.dot(np.array([[math.cos(Vinkler[n-1]), -math.sin(Vinkler[n-1])], [math.sin(Vinkler[n-1]), math.cos(Vinkler[n-1])]]), d[:, n - 1])
        
        
        # Næste punkt på grafen
        x[:, n] = x[:, n - 1] + (Længde[n-1] * d[:, n])    

    
    # Loader variablene valgt i MainScript.py
    Var = np.load("Variables.npz")
    System = Var["System"]
    N = Var["N"]
    
    # Plottet, forbinder automatisk hvert koordinat
    plt.plot(x[0, :], x[1, :])
    
    ##  Plot titel
    plt.title("{:s} Curve, Iteration {:.0f}".format(System, N))
    
    
    #Viser grafen. 
    plt.show()
    
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:03:09 2018

@author: loved
"""

import math;
import numpy as np;

def turtleGraph(lms):
    
    turtleCommands = np.array([]);
    
    if ('S' in lms):
        
        y = lms.count('SLSRSLS');
        
        try:
            iteration = int((math.log(4*y)) / (2 * math.log(2))) ;
        
        except ValueError:
            iteration = 0;
        
        length = (0.5)**iteration;
        
        if length == 0:
            length = 1;
    
        for i in range(len(lms)):
            
            if lms[i] == 'R':
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),((-2/3)*math.pi));
            
            elif lms[i] == 'L':
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),((1/3)*math.pi));
            
            else:
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),0);
             
        
        
    if ('A' in lms):
        
        y = lms.count('BRARB');
        y += lms.count('ALBLA');
        
        try:
            iteration = int((math.log(3*y)) / (math.log(3)));
            
        except ValueError:
            iteration = 0;
        
        length = (1/3)**iteration;
        
        if length == 0:
            length = 1;
        
        for i in range(len(lms)):
            
            if lms[i] == 'R':
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),((-2/3)*math.pi));
            
            elif lms[i] == 'L':
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),((1/3)*math.pi));
            
            else:
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
                turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),0);
    
    return turtleCommands
        
        
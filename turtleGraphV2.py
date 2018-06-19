# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:54:11 2018

@author: loved
"""
import math;
import numpy as np;

def turtleGraph(lms):

    from MainScript import N;
    from MainScript import codes;
    from MainScript import LR_turn;

    ## Variable til funktionen
    turtleCommands = np.array([]);
    ids = np.array([]);
    #factor = 0;
    
    ##Globale variable
    #codes = np.array(['S',(1/3),'A',0.5,'B',0.5]);
    #it_change = np.array(['SLSRSLS','BRARB','ALBLA']);
    #LR_turn = np.array([(1/3)*math.pi,-(2/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi]);
    
    
    ##Identificer streng
    
    for i in range(np.size(codes[::2])):
        
        if (codes[::2][i] in lms):
            
            try:
               rev_letters = np.insert(rev_letters,np.size(rev_letters),codes[::2][i]);
                
            except:
                rev_letters = codes[::2][i]
            
            ids = np.insert(ids,np.size(ids),int(i));
            
    #udtag længdeskaleringen
    length_factor = float(codes[1::2][int(ids[0])]);
    
    ## the factor is used to find the iteration in line 64. This variable is now redundant.
        ## Since we use a global variable instead this version is outdated.
        ## Basically it tells how many unique letters each unique letter becomes.
        ## Then the y variable counts how many unique letters there are in the lms-string.
        
    #for n in range(np.size(it_change)):
        
    #    for i in range(np.size(rev_letters)):
    #        factor += it_change[n].count(rev_letters[i]);
    
    #factor = (factor / np.size(rev_letters));
    
    
    
    ##Find iteration
    #y = 0;
    
    #for i in range(np.size(it_change)):
    #    y += lms.count(it_change[i]);
    
    #try:
    #    iteration = int(( math.log( factor * y )) / ( math.log(factor) )) ;
    
    #except ValueError:
    #    iteration = 0;
    
    iteration = N;
    
    length = (length_factor)**(iteration);
    

    if length == 0:
        length = 1;
    
    for i in range(len(lms)):
        
        if lms[i] == 'R':
            turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
            turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),LR_turn[1::2][int(ids[0])]);
        
        if lms[i] == 'L':
            turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
            turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),LR_turn[::2][int(ids[0])]);
        
        if np.any(lms[i] == rev_letters) and (lms[i-1] != 'R') and (lms[i-1] != 'L'):
            turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),length);
            turtleCommands = np.insert(turtleCommands,np.size(turtleCommands),0);
    
    return turtleCommands

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:10:33 2018

@author: Lasse Bruun
"""

#import packages
import numpy as np;
import matplotlib.pyplot as plt;
import math;
import os;


#import functions
from userInput import userInputMenu;
from userInput import userInputNumber;
from userInput import userInputString;

from turtleGraphV2 import turtleGraph;

from LindIter import LindIter;

from Plots import turtlePlot;

from addCode import addCode;


#global variables
codes = np.array(['S',(1/3),'A',0.5,'B',0.5]);
it_change = np.array(['SLSRSLS','BRARB','ALBLA']);
LR_turn = np.array([(1/3)*math.pi,-(2/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi]);
names = np.array(['Koch','Sierpinski']);

while True:
    
    print();
    
    ## Hovedmenu
    choice = userInputMenu(np.array(['Choose Lindenmeyer system', 'Set number of interations', 'Create plots', 'See information for the systems', 'Quit']),'Please select an option');
    
    
    ####   Lindenmeyer system and iterations  ####
    if (choice == 1):
        
        print();
        
        # Vælge system
        while True:
            system_choice = userInputMenu(np.insert(names,np.size(names),('Custom','Go back')),'Please select an option');
            
            
            ##  Koch Curve
            if system_choice == 1:
                
                System = names[0];
                
                print();
                print('You chose the Koch Curve. Returning to main menu.');
                
                break;
                
            ## Sierpinski Curve  
            if system_choice == 2:
                
                System = names[1];
                
                print();
                print('You chose the Sierpinski Curve. Returning to main menu.');
                
                break;
                
            if np.size(names) == 3:
                
                if system_choice == 3:
                    
                    System = names[2];
                
                    print();
                    print("You chose the custom curve '{:s}'. Returning to main menu.".format(names[2]));
                    break;
            
            ## Add code  
            if system_choice == np.size(np.insert(names,np.size(names),('Custom','Go back'))) - 1:
                print();
                go_back = False;
                if np.size(names) == 3:
                    system_question = userInputMenu(np.array(['Yes','No']),'Do you want to change the predefined function {:s}?'.format(names[2]));
                    
                    if system_question == 2:
                        go_back = True;
                
                if go_back == False:
                    codes = np.array(['S',(1/3),'A',0.5,'B',0.5]);
                    it_change = np.array(['SLSRSLS','BRARB','ALBLA']);
                    LR_turn = np.array([(1/3)*math.pi,-(2/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi]);
                    names = np.array(['Koch','Sierpinski']);
                    
                    (a,b,c,d,e,f) = addCode(codes,it_change,names)
                    
                    codes = np.insert(codes,np.size(codes),(a,c));
                    it_change = np.insert(it_change,np.size(it_change),b);
                    LR_turn = np.insert(LR_turn,np.size(LR_turn),(d,e));
                    names = np.insert(names,np.size(names),f);
                
                System = names[2];
                
                print();
                print("You chose the custom curve '{:s}'. Returning to main menu.".format(names[2]));
                break;
                
                
            ## Go back   
            if system_choice == np.size(np.insert(names,np.size(names),('Custom','Go back'))):
                print();
                print('Returning to main menu.');
                
                break;
    
    
        print();
        
        while True:
        
            Iter_choice = userInputMenu(np.array(['1', '2', '3', '4', '5', '6', '7', '8']),'Please choose a number between 1 and 8');
            
            N = int(Iter_choice)
            np.savez("Variables.npz", System = System, N = N, names = names, codes = codes, it_change = it_change, LR_turn = LR_turn)
            break;
        
        
        
    ####    Plots   ####
    if (choice == 3):
        print(turtlePlot(turtleGraph(LindIter(System, N))))
        
        
        
        
    ####    Info on systems   ####
    if (choice == 4):
        
        print();
        
        # Vælge systeminfo
        while True:
            system_choice = userInputMenu(np.array(['Lindenmeyer systems', 'Koch Curve','Sierpinski Curve','Go back']),'Please select an option');
            
            
             ##  Lindenmeyer system info
            if system_choice == 1:
                
                print();
                print('A Lindenmeyer System is a system originally created to describe the behaviour of plant cells and to model the growth processes of plant development. A Lindemeyer system is created of a string of letters which will follow replacement rules and develop for each iteration. The visualisation of the developed string follows certain rules, each letter is translated into a a so-called turtle graphics. Beginning in Origo with the basic vector (1,0) L can be translated to a left turn with a given angle and R is a right turn with another angle. After each iteration the lenght of the line segment is scaled by a certain factor given by the system.  Then the system completes the string by translating each letter into a complete turtle graphic.');
                print();
                print();
            
            
            ##  Koch Curve info
            if system_choice == 2:
                
                print();
                print('The Koch Curve is generated with three letters: S, L and R. The initial string is S and the replacement rules states that: \n S -> SLSRSLS \n L -> L \n R -> R \nWhich means the initial string is S and the first iteration becomes SLSRSLS and the second iteration becomes SLSRSLSLSLSRSLSRSLSRSLSLSLSRSLS. \nThe visualization rules states: \n L is translated to a left turn with 1/3*pi \n R is translated to a right turn with -2/3*pi and the scaling factor is 1/3');
                print();
                print();
                
                
            ## Sierpinski Curve info 
            if system_choice == 3:
                
                print();
                print('The Sierpinski triangle is generated with the four letters: A, B, L and R. The initial string is A and the replacement rules states that: \n A -> BRARB \n B -> ALBLA \n L -> L \n R -> R \nSince the initial string is A, the first iteration becomes BRARB and the second iteration will then become ALBLARBRARBRALBLA. \nThe visualization rules states: \n L is translated to a left turn with 1/3*pi \n R is translated to a right turn with 12/3*pi and the scaling factor is 1/2');
                print();
                print();
               
                
                
            ## Customized Curve info 
            #if system_choice == 3:
                
            #    print();
            #    print('The');
            #    print();
            #    print();
                
            
            ## Go back   
            if system_choice == 4:
                print();
                print('Returning to main menu.');
                
                break;
        
        
        
        
    ####    Quit program   ####
    if (choice == 5):
        print();
        print('Program shutting down.');
        break;
    
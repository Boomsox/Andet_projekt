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
names = np.array(['Koch Curve','Sierpinski Curve']);

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
                
                System = "Koch"
                
                print();
                print('You chose the Koch Curve. Returning to main menu.');
                
                break;
                
            ## Sierpinski Curve  
            if system_choice == 2:
                
                System = "Sierpinski"
                
                print();
                print('You chose the Sierpinski Curve. Returning to main menu.');
                
                break;
                
            
            ## Add code  
            if system_choice == np.size(np.insert(names,np.size(names),('Custom','Go back'))) - 1:
                print();
                (a,b,c,d,e,f) = addCode(codes,it_change,names)
                codes = np.insert(codes,np.size(codes),(a,c));
                it_change = np.insert(it_change,np.size(it_change),b);
                LR_turn = np.insert(LR_turn,np.size(LR_turn),(d,e));
                names = np.insert(names,np.size(names),f);
                
                break;
                
                
            ## Go back   
            if system_choice == np.size(np.insert(names,np.size(names),('Custom','Go back'))):
                print();
                print('Returning to main menu.');
                
                break;
    
            if (np.size(names) >= 3):
                if system_choice == np.size(np.insert(names,np.size(names),('Custom','Go back'))) - 2:
    
    ####    Info on systems   ####
    if (choice == 2):
        
        print();
        
        while True:
        
            Iter_choice = userInputMenu(np.array(['1', '2', '3', '4', '5', '6', '7', '8']),'Please input the number of iterations');
            
            N = int(Iter_choice)
        
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
                
                print('A Lindenmeyer System is a system originally created to describe the behaviour of plant cells and to model the growth processes of plant development. A Lindemeyer system is created of a string of letters which will be converted to');
                
            
            
            ##  Koch Curve info
            if system_choice == 2:
                
                print('The Koch Curve ');
                
                
                
            ## Sierpinski Curve inof 
            if system_choice == 3:
                
                print();
                
               
                
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
    
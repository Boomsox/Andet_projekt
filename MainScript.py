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

from turtleGraphV2 import turtleGraph;

from Lindter import LindIter;

from Plots import turtlePlot;


#global variables


while True:
    
    print();
    
    ## Hovedmenu
    choice = userInputMenu(np.array(['Choose Lindenmeyer system', 'See information for the systems', 'Set number of interations', 'Create plots', 'Quit']),'Please select an option');
    
    
    ####   Lindenmeyer system and iterations  ####
    if (choice == 1):
        
        print();
        
        # Vælge system
        while True:
            system_choice = userInputMenu(np.array(['Koch Curve','Sierpinski Curve','Go back']),'Please select an option');
            
            
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
                
                
            ## Go back   
            if system_choice == 3:
                print();
                print('Returning to main menu.');
                
                break;
    
    
    
    ####    Info on systems   ####
    if (choice == 2):
        
        print();
        
        # Vælge systeminfo
        while True:
            system_choice = userInputMenu(np.array(['Lindenmeyer systems', 'Koch Curve','Sierpinski Curve','Go back']),'Please select an option');
            
            
             ##  Lindenmeyer system info
            if system_choice == 1:
                
                print('A Lindenmeyer System is a system originally created to describe the behaviour of plant cells and to model the growth processes of plant development. A Lindemeyer system is created of a string');
                
            
            
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
        
    
    ####    Iterations   ####
    if (choice == 3):
        
        print();
        
        while True:
        
            Iter_choice = userInputMenu(np.array(['1', '2', '3', '4', '5', '6', '7', '8']),'Please input the number of iterations');
            
            N = int(Iter_choice)
        
            break;
        
    ####    Plots   ####
    if (choice == 4):
        print(turtlePlot(turtleGraph(LindIter(System, N))))
        
        
        
        
    ####    Quit program   ####
    if (choice == 5):
        print();
        print('Program shutting down.');
        break;
    
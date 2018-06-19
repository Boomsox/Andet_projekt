# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:32:54 2018

@author: loved
"""

import math;
import numpy as np;

from userInput import userInputNumber;
from userInput import userInputString;

codes = np.array(['S',(1/3),'A',0.5,'B',0.5]);
it_change = np.array(['SLSRSLS','BRARB','ALBLA']);
LR_turn = np.array([(1/3)*math.pi,-(2/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi,(1/3)*math.pi,-(1/3)*math.pi]);
names = np.array(['Koch','Ser']);


# addCode giver brugeren muligheden for at tilføje en ny sekvens, der kan bearbejdes af programmet.
    #de givne input er dem vi har valgt som globale variable, og er er kun med for at brugeren ikke vælger karakterer der allerede er i brug.
def addCode(codes,it_change,names):
    
    wrong_string = False;
    
    
    #input unikt bogstav
    u_letter = userInputString('Please input a unique letter to represent a unique sequence',np.insert(codes[::2],np.size(codes[::2]),('L','R')),1);
    
    
    #input unik sekvens
    while True:
        if wrong_string == True:
            print();
            print('String contains symbols that are not valid. Please try again.')
            wrong_string = False;
            
        u_string = userInputString("Please input a unique sequence, using only 'L', 'R' and '{:s}'".format(u_letter),it_change,20);
    
        for i in range(len(u_string)):
            if (u_string[i] != 'L') and (u_string[i] != 'R') and (u_string[i] != u_letter):
                wrong_string = True
            
        if (wrong_string == False):
            break;
            
    print();
    print('Each iteration scales the length of the drawn lines.');
    sc_number = userInputNumber('Please select the length-scaling factor',np.array([1e-5,1-1e-5]));
    
    print();
    print("Each 'R' and 'L' turns the direction in a certain angle. Please note that the next input will be used as a multiple of pi.");
    L_turn = math.pi * userInputNumber('Please input a positive integer as the angle of the left turn',np.array([1e-2,1-(1e-2)]));
    R_turn = -math.pi * userInputNumber('Please input a positive integer as the angle of the right turn',np.array([1e-2,1-(1e-2)]));
    
    print();
    name = userInputString("Please input a unique name",names,20);
    
    return (u_letter, u_string, sc_number, L_turn, R_turn, name.capitalize())
    
    
    
    
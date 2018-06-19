# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:23:24 2018

@author: Ditlev
"""

import numpy as np;

#userInputMenu printer en menu til brugeren og beder om en valgmulighed.
#options er et NumPy array, der indeholder de strings, som skal være brugerens muligheder.
#showstring er den streng som vises til brugeren, og forklarer hvad der skal inputtes.
def userInputMenu(options,showstring):
    
    #option-list
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    
    # Get a valid menu choice
    choice = -12345675364131245;
    
    #undersøger om choice er en af de viste muligheder
    while not(np.any(choice == np.arange(len(options))+1)):
        if choice != -12345675364131245:
            print("Input must have one of the displayed id's. Please try again.")
        while True:
            try:
                choice = float(input("{:s}: ".format(showstring)));
                break;
            except ValueError:
                print('Input is not valid. Please try again.')
                pass
    
    return choice


# userInputNumber printer en forespørgsel om et talinput fra brugeren
    
# input:
    # showstring er den forespørgsel, der vises til brugeren
    # limit er et NumPy array der indeholder to værdier; henholdsvis et minimum og et maksimum for inputtet.
        # hvis der ikke ønskes et max eller min inputtes værdien False.
        # Ex: Hvis man kun vil have et max på 60.
        # limit = np.array([False,60]);
def userInputNumber(showstring,limit):
    
    while True:
            
            try:
                
                choice = float(input("{:s}: ".format(showstring.capitalize())));
                
                if (limit[0] != False):
                    
                    if (limit[0] <= choice):
                        condition = 1;
                    
                    else:
                        print('Input is below the desired minimum of {:f}. Please try again.'.format(limit[0]));
                        condition = 0;
                
                else:
                    condition = 1;
                    
                if (condition == 1):
                    
                    if (limit[1] != False):
                    
                        if (limit[1] >= choice):
                            break;
                    
                        else:
                            print('Input is higher than the desired maximum of {:f}. Please try again.'.format(limit[1]));
                            condition = 0;
                    else:
                        break;
                        
            except ValueError:
                print("Not a valid number. Please try again.")
    
    return choice


# userInputString printer en forespørgsel om et strenginput fra brugeren
    
# input:
    # showstring er den forespørgsel, der vises til brugeren.
    # string_limit er et NumPy array med de strenge, der ikke må inputtes.
        # Hvis der ikke er nogen begrænsninger inputtes limit = np.array([0])
    # char_limit er antallet af karakterer der maksimalt må inputtes.
def userInputString(showstring,string_limit,char_limit):
    
    limit = np.copy(string_limit);
    
    for i in range(np.size(limit)):
        limit[i] = limit[i].upper();
        
    while True:
        
        condition = True;
        
        try:
            
            choice = str(input("{:s}: ".format(showstring)));
            choice = choice.upper();
            
            if limit[0] == False:
                condition = True;
                
            else:
                for i in range(len(choice)):
                    
                    if np.any(limit == choice):
                        
                        condition = False;
                    
            
            if condition == True:
                
                if choice.isalpha():
                    
                    if (len(choice) <= char_limit):
                        break;
                    
                    else:
                        print();
                        print('Please input only {:.0f} character(s).'.format(char_limit));
                
                else:
                    print();
                    print('The input can only contain letters. Please try again');
                    
                    
            else:
                print();
                print("The string '{:s}' is already used. Please input another.".format(choice));
                print();
                        
        except:
            print();
            print("Not a valid string. Please try again.")
        
    return choice
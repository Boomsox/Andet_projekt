# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:56:27 2018

@author: Anders V. Sehested, s174008
"""
import numpy as np

def LindIter(System, N):
    #LindIter's funktion er at skabe en string der kan oversættes til retninger og drejninger
    #i funktionen turtleGraph. Det gør den ved at få inputtet en string (System), som er navnet på det
    #system man ønsker at kigger på, og få inputtet det antal iterationer (N), man ønsker den skal gennemløbe. 
    
    
    #Henter de globale variable der bliver specificeret fra mainscriptet
    from MainScript import names
    from MainScript import codes
    from MainScript import it_change
    
    
    #Fjerner længderne fra den globale variable codes, så kun de intialiserende bogstaver står tilbage
    int_string = codes[::2]
    
    
    #Finder Systemets plads i names, da det (næsten) er analogt med det tilhørende erstatningsreglernes
    #og det initialiserende bogstavs plads.
    i = 0
    for i in range(np.size(names)):
        
        if (names[i] == System):
            n_place = i
            break
        else:
            i = i +1
   
    
    
    #Her udvikles de forskellige systemer, alt efter antallet af iterationer. Koch og Sierpinski
    #er de to første statements og den sidste er til brugerns egne regler. 
    
    #Den udskifter tegnet med sekvensen af bogstaver, og gør det N gange. 
    if n_place == 0:
           
        LindenmeyerString = int_string[n_place]
            
        for i in range(N):
                
            LindenmeyerString = LindenmeyerString.replace(int_string[n_place], it_change[n_place])
       
        return LindenmeyerString
        
    #Den udskifter flere tegn med sekvensen af de rigtige bogstaver, og gør det N gange. 
    #Da de to sekvenser indeholder de samme bogstaver, laves en af dem om til en midlertidig string, inden den igen laves om.
    elif n_place == 1:
            
        LindenmeyerString = int_string[n_place]
            
        for i in range(N):
            
            LindenmeyerString = LindenmeyerString.replace(int_string[n_place], "%temp%").replace(int_string[n_place + 1], it_change[n_place + 1]).replace("%temp%", it_change[n_place])
            
        return LindenmeyerString
        
    #Den udskifter tegnet med sekvensen af bogstaver, og gør det N gange. Den kigger dog en gang længere henne,
    #da Sierpinski fylder to pladser.
    else:
            
        LindenmeyerString = int_string[n_place + 1]
            
        for i in range(N):
                
            LindenmeyerString = LindenmeyerString.replace(int_string[n_place + 1], it_change[n_place + 1])
       
        return LindenmeyerString    



       
       
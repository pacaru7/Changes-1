
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the code for the internal game structure.
It starts off with the setting of game parameters, the player features 
as specified in Classes.py, and continues with the specific game level
structures.

Things we still have to figure out: 
    - Default option when you don't have any units left to expend. 
    

"""
from Functions import *
from Level import *   
       
def game_setting(): 
    """
    

    Returns
    -------
    This function sets the player parameters, using the methods setName()
    and setCountry() from the class Player() in the Classes.py file. It does 
    not return any value but is designed to take as input the name and the 
    country of the player. 
    
    The name of the player can be any type of string or even number 
    constellation. The country of the player ignores letter case and can 
    only take the country name (e.g. Germany) as opposed to the nationality
    (German) as input.
    
    The objects of the class are specified in Classes.py file.

    """
    printSlow("Welcome to the game!\n")
    stats.setName()
    printSlow("Welcome to the game, " + stats.getName() + "!\n")
    stats.setCountry(str(input(printSlow("Your nationality will "\
    "determine your gameplay. What is the country of your nationality?\n"))))         

# function for gameplay
def game(): 
    """
    

    Returns
    -------
    This function contains aside from the setting of the game parameters 
    all the existing game pathways.

    """
    game_setting()
    countryName = stats.getCountry()
    countryVisas = [ 'Colombia','India']
    if(countryName in countryVisas):
        printSlow("You've somehow managed to get German Visa.\n")
        printSlow(input("Press enter to continue.\n"))
    printSlow("How will you proceed to the airport for your flight to Berlin?\n"\
    "Let's see if the luck is in your hands.\n")
    printSlow(input("Press enter to continue.\n"))

    level1() 
    level2()
# Possibility of adding bank account, health insurance as extra levels 
    level3()
    level4() 

    

game()


    
    
    
    
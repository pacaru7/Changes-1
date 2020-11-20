# -*- coding: utf-8 -*-
"""
This module contains all the level structures. 


"""
from Functions import *
from Classes import * 
from Dictionaries import *

def level1(): 
    """
    

    Returns
    -------
    This function returns the plot structure for the first level, 
    transportation from the player's current destination to the airport.

    """
    # Level 1: transportation from residence to airport 
    m = diceRoll()
    ##m = 
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        ##for x in range(len(L1_1)): 
        ## just one question
        y = question(L1_1[0])
        if y == L1_1[0]["results"][0]: 
            printSlow("You went home. Gameover.")
            exit()
        elif y == L1_1[0]["results"][1]: 
            assets.assetChange(20, 0, 0)
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        # for not necessary. just one question...
        for x in range(len(L1_25)):
            y = question(L1_25[x])
            # Uber
            if y == L1_25[0]["results"][0]: 
                if m == 2: 
                    assets.assetChange(45, 50, -30)
                elif m == 3: 
                    assets.assetChange(40, 30, -20) 
                elif m == 4: 
                    assets.assetChange(35, 20, -10)
                else: 
                    assets.assetChange(30, 10, -5)
                if actioncard()% 2 == 0: 
                    printSlow(L1_25[0]["actioncard_u"][0])
                    assets.assetChange(0, 30, 0)
                else: 
                    printSlow(L1_25[0]["actioncard_u"][1])
                    assets.assetChange(0, 0, -20)
#                printSlow(Lvlup[0]["lvl1"])
            # Public transportation
            elif y == L1_25[0]["results"][1]:
                if m == 2: 
                    assets.assetChange(5, 20, 0)
                elif m == 3: 
                    assets.assetChange(5, 15, 0)
                elif m == 4: 
                    assets.assetChange(5, 10, 0)
                else: 
                    assets.assetChange(5, 5, 0)
                if actioncard()%2 == 0:
                    printSlow(L1_25[0]["actioncard_p"][0])
                    assets.assetChange(0, 20, 0)
                else: 
                    printSlow(L1_25[0]["actioncard_p"][1])
                    assets.assetChange(30, 0, 0)
               # printSlow(Lvlup[0]["lvl1"])

    ## if it is 6 continue here
    printSlow(Lvlup[0]["lvl1"])
    printSlow("\n. . .\n", 0.5)
    printSlow("Yay, you arrived in Berlin. But how do you get to your accommodation?")
    printSlow(input("\nPress enter to continue."))
    
def level2():
    """
    

    Returns
    -------
    This function returns the plot structure for the second level, 
    transportation from the airport to the player's accommodation in Germany.

    """
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        printSlow("For some reason, you felt like walking, so you walked all "\
                  "the way from the airport to your accommodation.\n") 
        assets.assetChange(0, 60, 0)
        printSlow(Lvlup[0]["lvl2"][1])
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        # for not necessary. just one question...
        for x in range(len(L2_25)):
            y = question(L2_25[x])
            if y == L2_25[0]["results"][0]:
                if m == 2: 
                    assets.assetChange(45, 40, -30)
                elif m == 3: 
                    assets.assetChange(40, 30, -20) 
                elif m == 4: 
                    assets.assetChange(35, 20, -10)
                else: 
                    assets.assetChange(30, 10, -5)
                if actioncard() > 50: 
                    printSlow(L2_25[0]["actioncard_u"][0])
                    assets.assetChange(0, 30, 0)
                else: 
                    printSlow(L2_25[0]["actioncard_u"][1])
                    assets.assetChange(0, 0, -20)
            elif y == L2_25[0]["results"][1]:
                if m == 2: 
                    assets.assetChange(5, 20, 0)
                elif m == 3: 
                    assets.assetChange(15, 15, 0)
                elif m == 4: 
                    assets.assetChange(10, 10, 0)
                else: 
                    assets.assetChange(5, 5, 0)
                if actioncard() > 50: 
                    printSlow(L2_25[0]["actioncard_p"][0])
                    assets.assetChange(0, 20, 0)
                else: 
                    printSlow(L2_25[0]["actioncard_p"][1])
                    assets.assetChange(30, 0, 0)
            printSlow(Lvlup[0]["lvl2"][1])
    elif m == 6: 
        printSlow(Lvlup[0]["lvl2"][0])
    printSlow("You've settled in for a couple days. But for you to stay and "\
              "become a permanent non-tourist resident, you need the residence "\
              "permit and appropriate passport photos for it.\n")
    printSlow(input("Press enter to continue."))
    
def level3(): 
    """
    

    Returns
    -------
    This function returns the plot structure for the third level, 
    acquisition of appropriate photos for the bureaucratic procedures to 
    follow.

    """
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        printSlow(L3_16[0]["x1"])
        assets.assetChange(0, 40, 0)
    if m == 2: 
        printSlow(L3_16[0]["x2"])
        assets.assetChange(10, 30, 0)
    if (m == 3 or m == 4): 
        printSlow(L3_16[0]["x34"])
        assets.assetChange(5, 0, 0)
    if (m == 5 or m == 6): 
        printSlow(L3_16[0]["x56"])
        assets.assetChange(20, 0, 0)
    printSlow(Lvlup[0]["lvl3"])
    # Paths are yet to be finished !!
    
def level4(): 
    """
    

    Returns
    -------
    This function returns the plot structure for the fourth level. It
    asks the player to decide between the Anmeldung or residence permit 
    process. Either option will be followed by the other one. Essentially, 
    plot structures are activated.

    """
    u = input(printSlow("Which one do you want to do first: " \
                        "Anmeldung or residence permit?\n"))
    if u.lower() == "residence permit": 
        Residencepermit() 
        Anmeldung()
    if u.lower() == "anmeldung": 
        Anmeldung()
        Residencepermit()
    
def Anmeldung():
    """
    Returns
    -------
    This function returns the plot structure for the fourth level, 
    registration at local Bürgeramt, also called Anmeldung.

    """
    printSlow("Time to get your Anmeldung!\n")
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if (m == 1 or m == 2): 
        printSlow(L4_1[0]["x12"]) 
        assets.assetChange(50, 50, 50)
        if actioncard() > 5: 
            printSlow(L4_1[0]["actioncard_12"])
            assets.assetChange(0, 0, -20)
    elif (m == 3 or m == 4):  
        printSlow(L4_1[0]["x34"])
        assets.assetChange(50, 50, 50)
        ## 25 % should be 100-25
        if actioncard() > 75: 
            printSlow(L4_1[0]["actioncard_34"][0])
            assets.assetChange(0, 100, 0)
        elif actioncard() > 70: 
            printSlow(L4_1[0]["actioncard_34"][1])
            assets.assetChange(0, 50, 0)
    elif (m == 5 or m == 6): 
            printSlow(L4_1[0]["x56"])
            assets.assetChange(50, 50, 50)
    printSlow("Anmeldung finished. Sth sth to be replaced by dict.")
    printSlow(input("Press enter to continue."))
# not completed! 

def Residencepermit():   
    """
    

    Returns
    -------
    This function returns the plot structure for the fourth level, 
    acquisition residence permit.

    """
    printSlow("Time to get your residence permit!\n")      
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if (m == 1):         
        printSlow(L4_2[0]["x1"]) 
        assets.assetChange(0, 50, 0)
    elif (m == 2):          
        printSlow(L4_2[0]["x2"])
        assets.assetChange(0, 50, 0)
    elif (m == 3): 
        printSlow(L4_2[0]["x3"])
        assets.assetChange(0, 50, 0)
    elif (m == 4 or m == 5 or m == 6): 
        printSlow(L4_2[0]["x4_6"])
    printSlow("Residence permit obtained. Sth sth to be replaced by dict.")
    printSlow(input("Press enter to continue."))
    
    
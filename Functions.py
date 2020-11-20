# -*- coding: utf-8 -*-
"""

This module contains system (?) functions.

"""

# function for printing strings a bit more slowly
import sys, time
def printSlow(sth, x = 0.01):
    """
    

    Parameters
    ----------
    sth : STRING
        Some string.
    x : FLOAT, optional
        Pace parameter. The default is 0.01.

    Returns
    -------
    str
        A string returned in the pace of 0.01 at default or 
        at a specified pace.

    """
    for letter in sth:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(x)
    return ""

 
# function for the dice roll
import random
def diceRoll():
    """
    

    Returns
    -------
    INTEGER
        Returns a random dice roll number.

    """
    return random.choice([1,2,3,4,5,6])

# function for actioncard 
def actioncard(): 
    """
    

    Returns
    -------
    INTEGER
        Returns a random number from 1 to 100.

    """
    return random.randrange(101)

# function for dict junctions
def question(aDictionary):
    """
    

    Parameters
    ----------
    aDictionary : DICTIONARY
        Takes as input a dictionary of choice with three keys: 
            1. "questions" with 1 value 
            2. "answers" with 2 values
            3. "results" with 2 values 

    Returns
    -------
    DICTIONARY VALUE 
        Returns a dictionary value of the "results" key or a default 
        message: "[userInput] is not a Valid Answer".

    """
    userInput = None
    printSlow(aDictionary["question"])
    printSlow("Write " +'"'+ aDictionary["answers"][0] + '"' + " or " 
                  + '"' + aDictionary["answers"][1]+  '"'+".\n")
    userInput = str(input()).strip()
    if userInput not in aDictionary["answers"]:
        printSlow(userInput + " is not a Valid Answer.\n")   
        return question(aDictionary)
    else:
        index = aDictionary["answers"].index(userInput)
        printSlow(aDictionary["results"][index])
        return aDictionary["results"][index]
           
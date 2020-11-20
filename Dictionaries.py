# -*- coding: utf-8 -*-
"""

This module specifies the text input for the game, such as details of 
every pathway. There are three types of dictionaries as of now: 
    1. Lvlup-nature: contains messages for the successful clearance of a level.
    2. Level-nature: question, answer and result messages of every pathway. 
    3. Dice-nature: dice roll options

"""

# Level up messages 

Lvlup = [{
    "lvl1": "Congratulations. You made it to your flight on time, and "\
          "will be arriving in Berlin shortly.\n", 
    "lvl2": ["You got an international SIM card and can access Google "\
             "maps to get to your accomodation.\n" \
              "Yay, you've made it to your accomodation!\n", 
              "Yay, you've made it to your accomodation!\n"], 
    "lvl3":[ "Your passport photos fit the criteria and you are ready to "\
              "proceed to your appointments.\n"], 
    "lvl4": ["You got a nice English-speaking public servant"\
            "Yay!,your residence permit have been approved "]
        }]

# Level 1 (transportation) for dice roll of 1
L1_1 = [{
    "question": "Will you go home or pay 20 units of money "\
                "for a new flight?\n",
    "answers" : ["Go home", "Pay"],
    "results" : ["You chose to go home.\n", "You chose to pay 20 units "\
                "of money for a new flight.\n"]      
    }]
    
    
# Level 1 (transportation) for dice roll of 2 to 5
L1_25 = [{ 
     "question": "Will you take an Uber or Public transportation?\n",
     "answers" : ["Uber","Public"],
     "results" : ["You chose Uber.\n","You chose public transportation.\n"], 
     "actioncard_u": ["You temporarily got stuck in a traffic jam and lost "\
                    "some valuable time.\n", "The uber driver connects you "\
                    "to a friend of his in Berlin who will happily help " \
                    "you out.\n"],
    "actioncard_p": ["You got lost and lost valuable "\
                    "time.\n", "You forgot to validate your "\
                    "ticket and had to pay a penalty.\n"]
    }]

# Level 2 (transportation in Berlin) 
L2_25 = [{
     "question": "Will you take an Uber or Public transportation?\n",
     "answers" : ["Uber","Public"],
     "results" : ["You chose Uber.\n","You chose public transportation.\n"], 
     "actioncard_u": ["You temporarily got stuck in a traffic jam and lost "\
                      "some valuable time.\n", "The uber driver has a nephew "\
                      "in Berlin who will help you out in need.\n"], 
     "actioncard_p": ["You got lost and lost valuable time.\n", 
                      "You forgot to validate your "\
                      "ticket and had to pay a penalty.\n"]
    }]

# Level 3 (photo for residence permit/Anmeldung) 
L3_16 = [{
    "x1": "Oops, you've tried to use old photos. They got rejected "\
        "and you wasted time in that attempt.\n",
    "x2": "You went to a photo box but there was a rat that bit you. "\
        "You needed to go the hospital, and lost time and money.\n", 
    "x34": "You used a photo box at some random S-Bahn station close "\
        "to your home and it worked out just fine.""You used a photo "\
        "box at some random S-Bahn station close to your home and it "\
        "worked out just fine.\n",
    "x56": "You went to a professional photo shop."
    
    }]
    
# Level 4.1 (residence permit)
L4_1 = [{ 
    "x12": "A mean, non-English-speaking public servant grunts at you. It "\
            "looks like you will have to exert some additional resources "\
            "pass this test.\n",
    "x34": "A moody public servant with broken English greets you. Let's "\
            "see whether the force is with you.\n", 
    "x56": "Bingo! A nice, English-speaking public servant welcomes you. "\
            "Today is a good day.\n", 
    "actioncard_12": "Weirdly enough, the public servant finds you pleasant "\
                    "and befriends you. Either you are a very likable or "\
                    "questionable person.\n", 
    "actioncard_34": ["The public servant is in a very bad mood today. "\
                        "You better make a new appointment and hope to "\
                        "meet someone else next time.\n", "The public servant "\
                        "is in a bad moody today and appears not cooperative. "\
                        "You have to wait in line.\n"],   
    
    }]
    
# Level 4.2 (Anmeldung)
L4_2 = [{
    "x1": "You slept in and missed you appointment. You need to reschedule "\
        "for two months later.\n",
    "x2": "You forgot to bring the necessary documents. You need to reschedule "\
        "for 2 months later.\n",
    "x3": "You went to the wrong Bürgeramt and haste to the right one.\n",
    "x4_6": "You brought the passport, completed registration form, and "\
            "confirmation of your moving in. You also made it to your "\
            "appointment on time. Yay!"
    
    
    }]
import random
import food_list
from food_list import *

while True:
    main = True
    while main:                                                                 #welcome prompt and first question
        print("welcome back Emi! Let's choose your next meal!")
        choice_1 = input("Do you want to eat something warm or cold? ")
        valid_choice_1 = ('warm', 'cold')                                       #accepted inputs 
        while choice_1 not in valid_choice_1:                                   #while loop untill one of the accepted inputs are entered
            print('Invalid choice. Please choose again.')                       
            choice_1 = input("Do you want to eat something warm or cold? ")      #first question block ends   

        choice_2 = input("The meal should be hard, soft, or a liquid? ")
        valid_choice_2 = ('hard', 'soft', 'liquid')                             #second question block
        while choice_2 not in valid_choice_2:
            print('Invalid choice. Please choose again.')
            choice_2 = input("The meal should be hard, soft, or a liquid? ")

        choice_3 = input("Finnaly, it should be bitter, sweet, sour, salty, spicy, hot, or umami? ")
        valid_choice_3 = ('bitter', 'sweet', 'sour', 'salty', 'spicy', 'hot', 'umami')                    #third question block
        while choice_3 not in valid_choice_3:
            print('Invalid choice. Please choose again.')
            choice_3 = input("Finnaly, it should be bitter, sweet, sour, salty, spicy, hot, or umami? ")

        if choice_1 == 'warm':   #first question choice validation and transformation
            q_1 = tuple(warm)
        elif choice_1 == 'cold':
            q_1 = tuple(cold)

        if choice_2 == 'hard':       #second question choice validation and transformation
            q_2 = tuple(hard)
        elif choice_2 == 'soft':
            q_2 = tuple(soft)          
        elif choice_2 == 'liquid':
            q_2 = tuple(liquid)

        if choice_3 == 'bitter':             
            q_3 = tuple(bitter) 
        if choice_3 == 'sweet':             
            q_3 = tuple(sweet)          #third question choice validation and transformation
        elif choice_3 == 'sour':
            q_3 = tuple(sour)          
        elif choice_3 == 'salty':
            q_3 = tuple(salty)
        elif choice_3 == 'spicy':
            q_3 = tuple(spicy)          
        elif choice_3 == 'hot':
            q_3 = tuple(hot)
        elif choice_3 == 'umami':
            q_3 = tuple(umami)

        q_1_as_set = set(q_1)   #reformating answers to sets, to use .intersection
        q_2_as_set = set(q_2)
        q_3_as_set = set(q_3)
        result_as_set = q_1_as_set.intersection(q_2_as_set, q_3_as_set)   #create a new set with common items from food_list

        if len(result_as_set) > 0:  #conditional check and response in case zero items in set
            suggestion = random.choice(list(result_as_set))  #in case more than one food present, randomly choose one
        else:
            suggestion = ('again. Sorry, my list of recepies is a bit limited') #in case of empty set(), say sorry!

        print('-------------------------------------------------------------------------------') #easier to read consecutive print statements
        print("You chose something {0}, {1}, and {2}.".format(choice_1.lower(), choice_2.lower(), choice_3.lower())) #show input provided by user
        print('-------------------------------------------------------------------------------')
        print("I suggest you try", str(suggestion)+'.') #and finally, show the suggestion
        print('-------------------------------------------------------------------------------') #easier to read consecutive print statements
        main = False #end main loop
    restart = input("Not really happy with my suggestion? Type 'yes' to try again. ") #restart block
    if restart.lower() == 'yes': #only YES or yes inputs accepted as criteria to restart main 
        main = True
    else:
        exit()
    
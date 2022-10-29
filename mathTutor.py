#toy.py
#October 16, 2022
#This program will help the user practice his/her math skills

from random import randint

#This function will do the addition at level 1
def addition1():
    #variable for the final grade in the exercises
    total = 0.0
    
    #The number of problems the user wants to try.
    problems = int(input('Enter how many problems you would like to try: '))
    #Variable counting the number of problems
    q = 1
    #Variable counting the right answers
    r = 0

    #loop for the exercises
    while q <= problems:
        #x and y as the 2 variables assigned to the random numbers for the operations
        x = randint(1, 9)
        y = randint(1, 9)

        #Prompt the user to answer the question
        answer = int(input('Problem ' + str(q) + ':' + '\n'+ str(x)+ '+'+ str(y)+'=? ' ))

        #variable (int) for the result of the operation
        rightAnswer = x + y

        #when the right answer is given
        if rightAnswer == answer :

            r += 1
            print('Correct! Great Job!')
            
         #when the wrong answer is given   
        else:
            print('Sorry, that is incorrect. The correct answer is ' + str(rightAnswer))

        q += 1
    
    #to calculate the final grade for the exercises
    total = (r * 100)/(q-1)
    
    #Final grade display
    print('\nYou answered ' + str(r) + ' out of ' + str(q-1)+ ' correctly. Your score = ' +\
          str(round(total)) + '%')

#This function will do the addition at level 2
def addition2():
    #variable for the final grade in the exercises
    total = 0.0
    
    #The number of problems the user wants to try.
    problems = int(input('Enter how many problems you would like to try: '))
    #Variable counting the number of problems
    q = 1
    #Variable counting the right answers
    r = 0

    #loop for the exercises
    while q <= problems:
        #x and y as the 2 variables assigned to the random numbers for the operations
        x = randint(1, 99)
        y = randint(1, 99)

        #Prompt the user to answer the question
        answer = int(input('Problem ' + str(q) + ':' + '\n'+ str(x)+ '+'+ str(y)+'=? ' ))

        #variable (int) for the result of the operation
        rightAnswer = x + y

        #when the right answer is given
        if rightAnswer == answer :

            r += 1
            print('Correct! Great Job!')
            
         #when the wrong answer is given   
        else:
            print('Sorry, that is incorrect. The correct answer is ' + str(rightAnswer))

        q += 1
    
    #to calculate the final grade for the exercises
    total = (r * 100)/(q-1)
    
    #Final grade display
    print('\nYou answered ' + str(r) + ' out of ' + str(q-1)+ ' correctly. Your score = ' +\
          str(round(total)) + '%')









#This function will do the substraction at level 1
def substraction1():
    #variable for the final grade in the exercises
    total = 0.0
    
    #The number of problems the user wants to try.
    problems = int(input('Enter how many problems you would like to try: '))
    #Variable counting the number of problems
    q = 1
    #Variable counting the right answers
    r = 0

    #loop for the exercises
    while q <= problems:
        #x and y as the 2 variables assigned to the random numbers for the operations
        x = randint(1, 9)
        #x >= y to avoid negative answers
        y = randint(1, x)

        #Prompt the user to answer the question
        answer = int(input('Problem ' + str(q) + ':' + '\n'+ str(x)+ '-'+ str(y)+'=? ' ))

        #variable (int) for the result of the operation
        rightAnswer = x - y

        #when the right answer is given
        if rightAnswer == answer :

            r += 1
            print('Correct! Great Job!')
            
         #when the wrong answer is given   
        else:
            print('Sorry, that is incorrect. The correct answer is ' + str(rightAnswer))

        q += 1
    
    #to calculate the final grade for the exercises
    total = (r * 100)/(q-1)
    
    #Final grade display
    print('\nYou answered ' + str(r) + ' out of ' + str(q-1)+ ' correctly. Your score = ' +\
          str(round(total)) + '%')





#This function will do the substraction at level 2
def substraction2():
    #variable for the final grade in the exercises
    total = 0.0
    
    #The number of problems the user wants to try.
    problems = int(input('Enter how many problems you would like to try: '))
    #Variable counting the number of problems
    q = 1
    #Variable counting the right answers
    r = 0

    #loop for the exercises
    while q <= problems:
        #x and y as the 2 variables assigned to the random numbers for the operations
        x = randint(1, 99)
        #x >= y to avoid negative answers
        y = randint(1, x)

        #Prompt the user to answer the question
        answer = int(input('Problem ' + str(q) + ':' + '\n'+ str(x)+ '-'+ str(y)+'=? ' ))

        #variable (int) for the result of the operation
        rightAnswer = x - y

        #when the right answer is given
        if rightAnswer == answer :

            r += 1
            print('Correct! Great Job!')
            
         #when the wrong answer is given   
        else:
            print('Sorry, that is incorrect. The correct answer is ' + str(rightAnswer))

        q += 1
    
    #to calculate the final grade for the exercises
    total = (r * 100)/(q-1)
    
    #Final grade display
    print('\nYou answered ' + str(r) + ' out of ' + str(q-1)+ ' correctly. Your score = ' +\
          str(round(total)) + '%')






#This function will do the multiplication at level 1
def multiplication1():
    #variable for the final grade in the exercises
    total = 0.0
    
    #The number of problems the user wants to try.
    problems = int(input('Enter how many problems you would like to try: '))
    #Variable counting the number of problems
    q = 1
    #Variable counting the right answers
    r = 0

    #loop for the exercises
    while q <= problems:
        #x and y as the 2 variables assigned to the random numbers for the operations
        x = randint(1, 9)
        y = randint(1, 9)

        #Prompt the user to answer the question
        answer = int(input('Problem ' + str(q) + ':' + '\n'+ str(x)+ '*'+ str(y)+'=? ' ))

        #variable (int) for the result of the operation
        rightAnswer = x * y

        #when the right answer is given
        if rightAnswer == answer :

            r += 1
            print('Correct! Great Job!')
            
         #when the wrong answer is given   
        else:
            print('Sorry, that is incorrect. The correct answer is ' + str(rightAnswer))

        q += 1
    
    #to calculate the final grade for the exercises
    total = (r * 100)/(q-1)
    
    #Final grade display
    print('\nYou answered ' + str(r) + ' out of ' + str(q-1)+ ' correctly. Your score = ' +\
          str(round(total)) + '%')




#This function will do the multiplication at level 2
def multiplication2():
    #variable for the final grade in the exercises
    total = 0.0
    
    #The number of problems the user wants to try.
    problems = int(input('Enter how many problems you would like to try: '))
    #Variable counting the number of problems
    q = 1
    #Variable counting the right answers
    r = 0

    #loop for the exercises
    while q <= problems:
        #x and y as the 2 variables assigned to the random numbers for the operations
        x = randint(1, 99)
        y = randint(1, 99)

        #Prompt the user to answer the question
        answer = int(input('Problem ' + str(q) + ':' + '\n'+ str(x)+ '*'+ str(y)+'=? ' ))

        #variable (int) for the result of the operation
        rightAnswer = x * y

        #when the right answer is given
        if rightAnswer == answer :

            r += 1
            print('Correct! Great Job!')
            
         #when the wrong answer is given   
        else:
            print('Sorry, that is incorrect. The correct answer is ' + str(rightAnswer))

        q += 1
    
    #to calculate the final grade for the exercises
    total = (r * 100)/(q-1)
    
    #Final grade display
    print('\nYou answered ' + str(r) + ' out of ' + str(q-1)+ ' correctly. Your score = ' +\
          str(round(total)) + '%')


def main():
    
    #variables declaration (int)
    choice = choice1 = level = 0

    #intro
    print('WELCOME TO THE VIRTUAL MATH TUTOR!')

    #prompt for the user's choice to practice or to see the rules or to exit 
    choice = eval(input("\n\nPlease, choose from the following menu: \
    \n1)See rules \n2)Math Practice \n3)Exit\
    \n\nPlease enter the number of your choice here: "))

    #loop to start the program
    while choice != 2 and choice != 3:

        #The number chosen
        if choice == 1:
            print('\nThis program will help you practice your math skills. '+\
                  'First, you will choose Addition, Subtraction or Multiplication. '+\
                  'Next, you will choose a level. '+\
                  'Level 1 will give you problems with single digits and Level 2 will use two-digit numbers.'+\
                  'Then, you will choose how many math problems you would like to complete. '+\
                  'After you have completed all your problems, you will be given a score. ' +\
                  'You can play as many times as you want. Have fun!!')
            choice = eval(input("\n\nPlease, choose from the following menu: \
                \n1)See rules \n2)Math Practice \n3)Exit\
                \n\nPlease enter the number of your choice here: "))

        
        #if the choice is not 1, 2, or 3
        elif choice != 1: 
            print('\nInvalid input. You must choose 1,2, or 3 from the menu')

            choice = eval(input("\n\nPlease, choose from the following menu: \
                \n1)See rules \n2)Math Practice \n3)Exit\
                \n\nPlease enter the number of your choice here: "))
    #if the choice is 3
    if choice == 3:
        print('Goodbye!')

    #if the choice is 2
    elif choice == 2:
        print('\nYou have chosen to do some math!!'+\
              '\n\nPlease, choose from the following menu: \n1)Addition \n2)Substraction\n3)multiplication')

        #Prompt the user to choose an operation
        choice1 = eval(input('\nEnter your choice here: '))

        #if an invalid choice
        while choice1 != 1 and choice1 != 2 and choice1 != 3:
            print('\nInvalid input. You must choose 1, 2, or 3 from the menu')

            choice1 = eval(input('\nEnter your choice here: '))
        # 1 for addition
        if choice1 == 1:
            print('\nNext, choose a level: \n1)Level one \n2)Level two')

            #which level?
            level = eval(input('\nEnter your level choice here: '))

            #If the user choose a number not on the menu
            while level != 1 and level != 2:
                print('\nInvalid input. You must choose 1 or 2 from the menu.')
                level = eval(input('\nEnter your level choice here: '))
                
            if level == 1:
                addition1()

            elif level == 2:
                addition2()
        # 2 for subtraction
        elif choice == 2:
            print('\nNext, choose a level: \n1)Level one \n2)Level two')

            level = eval(input('Enter your level choice here: '))

            while level != 1 and level != 2:
                print('\nInvalid input. You must choose 1 or 2 from the menu.')
                level = eval(input('\nEnter your level choice here: '))
                
            if level == 1:
                substraction1()

            elif level == 2:
                substraction2()
            
        #3 for multiplication
        elif choice == 3:
            print('\nNext, choose a level: \n1)Level one \n2)Level two')

            level = eval(input('\nEnter your level choice here: '))

            while level != 1 and level != 2:
                print('\nInvalid input. You must choose 1 or 2 from the menu.')
                level = eval(input('\nEnter your level choice here: '))
                
            if level == 1:
                multiplication1()

            elif level == 2:
                multiplication2()

main()
            

        
        


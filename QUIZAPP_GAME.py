print("HELLO WELCOME TO MY COMPUTER QUIZ!!!!!!")

#initialize score and question number
score = 0
question_number = 0

#Ask if the  user wants to play
playing = input("DO YOU WANT TO PLAY? (YES/NO): ").lower()

if playing != "yes":
    quit()
    
print("OK LETS PlAY: YOU HAVE 5 QUESTIONS")
print("GOOD LUCK")
print("SPELL THE ANSWERS CORRETLY TO GET THE POINTS")



    #QUESTION 1
question_number += 1
answer = input(f"\n{question_number}. what does CPU stand for? ").lower()
if  answer == "central processing unit":
        score += 10
        print("BOOM YES 10 POINTS")
else:
        print("NOOO DUMMY")  
        
        
        #QUESTION 2
question_number += 1
answer = input(f"\n{question_number}. what does GPU stand for? ").lower()
if  answer == "graphics processing unit":
        score += 10
        print("BOOM YES  ANOTHER 10 POINTS")
else:
        print("NOOO DUMMY")  
        
        
        
             #QUESTION 3
question_number += 1
answer = input(f"\n{question_number}. what does RAM stand for? ").lower()
if  answer == "random access memory":
        score += 10
        print("BOOM YES Another 10 POINTS")
else:
        print("NOOO DUMMY") 
        
        
        #QUESTION 4
question_number += 1
answer = input(f"\n{question_number}. what does PSU stand for? ").lower()
if  answer == "power supply unit":
        score += 10
        print("BOOM YES 10 POINTS")
else:
        print("NOOO DUMMY") 
        
        
        #QUESTION 5
question_number += 1
answer = input(f"\n{question_number}. what does ROM stand for? ").lower()
if  answer == "read only memory":
        score += 10
        print("BOOM YES 10 POINTS")
else:
        print("NOOO DUMMY") 
        
        print(f"\nNUMBER OF QUESTIONS: {question_number}")
        print(f"YOUR SCORE: {score}")
        print("THANK YOU !!!!!!!!!!!")


# creating a quiz program using for, if else, and 2-D lists

questions = (("How many bones in human body?"),
             ("How many muscles in human body?"),
             ("How many sense organs?"),
             ("How many planets in solar system?"),
             ("How many states in India?"))

options = (("A. 204","B. 205","C. 206","D. 207"),
             ("A. 400-450","B. 450-500","C. 500-550","D. 550-750"),
             ("A. 5","B. 6","C. 7","D. 8"),
             ("A. 7","B. 9","C. 8","D. 10"),
             ("A. 25","B. 26","C. 27","D. 28"))

guesses = []
score = 0
ques_counter = 0
answers = ["C","D","A","C","D"]

for ques in questions:
    print("---------------------")
    print(ques)

    for ans in options[ques_counter]:
        print(ans)
    
    answer = input("Enter your guess[A,B,C,D]: ")
    guess = answer.upper()
    guesses.append(guess)
  
    if guesses[ques_counter] == answers[ques_counter]:
        score +=1
        print("Correct !")
    else:
        print("Incorrect !")
    ques_counter +=1   
print("---------------------")
print(f"Your guesses are: {guesses}")
print(f"Correct guesses are: {answers}")
percentage = (score/ques_counter)*100
print(f"You scored {percentage}% ")
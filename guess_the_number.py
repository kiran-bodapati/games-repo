import random
EASY_LEVEL=10
HARD_LEVEL=5
def set_difficulty(level):
    if level=='easy':
      return EASY_LEVEL
    else:
      return HARD_LEVEL
def guess():    
    def check_number(guessed_number,answer,attempts):
     if guessed_number<answer:
         print("your answer is low")
         return attempts-1
     elif guessed_number>answer:
         print("your answer is high")
         return attempts-1
     else:
         print(f"your guess is right....The answer was {answer}")
         
    print("let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    level=input("choose the level of difficulty.... type 'easy' for easy level and 'hard' for for hard level:").lower()
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} no.of attempts left to guess the number")
        guessed_number=int(input("Guess a number:"))
        attempts=check_number(guessed_number,answer,attempts)
        if attempts==0:
          print("you are out of guesses....you lose")
          return
        elif guessed_number!=answer:
          print("guess again")
guess()



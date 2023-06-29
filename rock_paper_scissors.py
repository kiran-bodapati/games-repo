import random
a=int(input("Enter your choice:\n  0.Rock \t 1.Paper \t 2.Scissor \n"))
if a>2 or a<0:
     print("wrong input")

b=random.randint(0,2)
print(f'Computer choice: {b}')
print(b)
if a==b:
        print("It's a Draw")
elif a==2 and b==0:
        print("Computer won!")
elif a==0 and b==2:
        print("You won!")
elif a>b:
        print("You won!")
elif b>a:
        print("Computer won!")
    
 

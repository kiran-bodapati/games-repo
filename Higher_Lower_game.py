
import random
import os
data=[
    {
        'name':"Jenny's lectures",
        'follower_count':1,
        'description':'youtuber',
        'country':'India'
    },
     {
        'name':"Messi",
        'follower_count':480,
        'description':'sportsperson(football)',
        'country':"Argentina"
    },
     {
        'name':"Narendra modi",
        'follower_count':50,
        'description':'Prime minister',
        'country':"India"
    },
     {
        'name':"Kohli",
        'follower_count':398,
        'description':'sportsperson(cricket)',
        'country':"India"
    },
     {
        'name':"Cristiano Ronaldo",
        'follower_count':600,
        'description':'sportsperson(footballer)',
        'country':"portugal"
    },
     {
        'name':"Pawan kalyan",
        'follower_count':3,
        'description':'actor&politician',
        'country':"India"
    },
     {
        'name':"RRR",
        'follower_count':20,
        'description':'movie_name',
        'country':"India"
    },
]
score=0
def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name},a {description},from {country}"
    
def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess==1:
            return False
        else:
            return True
    elif followers_1>followers_2:
        if guess==1:
            return True
        else:
            return False


account_2=random.choice(data)
continue_flag=True
while continue_flag:
    account_1=account_2
    account_2=random.choice(data)
    while account_1==account_2:
        account_2=random.choice(data)
    print(f"compare1:{display_accountinfo(account_1)}")
    print(f"compare2:{display_accountinfo(account_2)}")
    
    guess=int(input("who has more followers? Type 1 or 2:"))
    followers_count_1=account_1['follower_count']
    followers_count_2=account_2['follower_count']
    print(followers_count_1)
    print(followers_count_2)
    is_correct=check_answer(guess,followers_count_1,followers_count_2)
    os.system('cls')
    if is_correct:
        score+=1
        print(f"You are right.Your score is :{score}")

    else:
        
        print(f"You are wrong.Your  final score is : {score}")
        continue_flag=False


                                  


    

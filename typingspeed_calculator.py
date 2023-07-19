from time import *           #impoting all methods from time module
import random as r#impoting random module as r
def mistake(test1,testinput):
    error=0
    for i in range(len(test1)):
      try:
          if test1[i]!=testinput[i]:
            error+=1
      except:
          error+=1
    return error

def  speed_time(time_1,time_2,testinput):
    time_delay=time_2-time_1
    time_R=round(time_delay,2)
    speed=len(testinput)/time_R
    return round(speed)

while True:
    ck=input("read to test (Yes/no):")     
    if ck=="yes":
      test=[" my name is kiran,i love playing cricket ,recently started watching football and iam loving it so much","the cool in the cool cool angry man","he is the king of the andhra"]
             #craeting a small list to generate strings for testing  
      test1=r.choice(test)    #generating a random string from above list
      print("                   ******Typing speed*********")
      print(test1)
      print()
      print()
      time_1=time()         #time function prints the number of seconds from 1971 to till this function called
      testinput=input("Enter:")
      time_2=time()
      print("speed:",speed_time(time_1,time_2,testinput),"l/sec")
      print("error:",mistake(test1,testinput))
      
    elif ck=="no":
       print("Thank You")
       break

    else:
       print("wrong input")
       break

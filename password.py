import random
letters=["a"," b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"A", "B", "C", "D", "E", "F", "G", "H",
         "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols= ["！","＃", "＄", "％", "＆", "＊","，"," ．", "：", "；", "？", "＠"]
numbers=['0','1','2','3','4','5','6','7','8','9']
a=int(input("enter the no of numbers:"))
b=int(input("enter the no of symbols:"))
c=int(input("enter the no of letters:"))
password_list=[]
for i in range(0,a):
    f=random.choice(numbers)
    password_list=password_list+f
for i in range(0,b):
    e=random.choice(symbols)
    password_list=password_list+e
for i in range(0,c):
    d=random.choice(letters)
    password_list=password_list+d
print(password_list)



#count=0
#for i in password:
    #count=count+1
#for i in range(0,count):
   #print(password[i])
   #print

    






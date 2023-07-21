from tkinter import *
import os
def restart():                       
    os.system("shutdown /r /t 1")    #using system() function from os module
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")
st=Tk()               #importing tk class from tkinter module
st.title("shutdown app")  #giving title to the app
st.geometry("500 * 500")    #setting  the size 
st.config(bg='blue')     #setting the background_color



r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")        
r_button.place(x=150,y=60,height=50,width=200,command=restart)


rt_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")        
rt_button.place(x=150,y=170,height=50,width=200,command=restart_time)



lg_button=Button(st,text="Log_out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")
lg_button.place(x=150,y=270,height=50,width=200,command=logout)


st_button=Button(st,text="shutDown",font=("Time New Roman",20,"bold"),relies=RAISED,cursor="plus")
st_button.place(x=150,y=370,height=50,width=200,command=shutdown)



st.mainloop()

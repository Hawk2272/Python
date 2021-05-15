from tkinter import *
import tkinter as tk
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    print("The Set Date is:",date)
    print(now)
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now =current_time.strftime("%H:%M:%S")
        date =current_time.strftime("%d/%m/%Y")
        if now==set_alarm_timer:
            print("\nTime to Wake up. The time is:",now)
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break   
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

while True:
    print("\tMain menu:")
    print("\t1. Alarm Sleep")
    print("\t2. Sleep suggestions")
    print("\t3. Exit")
    i=int(input("Enter your option:"))
    if i==1:
        clock= Tk()
        clock.iconbitmap(r'C:\Users\user\Downloads\alarm.ico')
        clock.title("Alarm Sleep")
        clock.geometry("400x200")
        time_format=Label(clock, text= "Enter time in 24 hour format!", fg="cyan",bg="black",font="Calibri").place(x=60,y=120)
        addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 130)
        setYourAlarm = Label(clock,text = "When to wake you up?",fg="blue",relief = "solid",font=("Times New Roman",8,"bold")).place(x=0, y=29)
        # The Variables we require to set the alarm(initialization):
        hour = StringVar()
        min = StringVar()
        sec = StringVar()
        #Time required to set the alarm sleep:
        hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=130,y=30)
        minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=170,y=30)
        secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=220,y=30)
        submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =135,y=60)
        clock.mainloop()
    if i==2:
        sleep=Tk()
        sleep.iconbitmap(r'C:\Users\user\Downloads\Snore-01-512.ico')
        sleep.geometry("400x200")
        time_format=Label(sleep, text= "Enter time in 24 hour format!", fg="SeaGreen1",bg="black",font="Calibri").place(x=60,y=120)
        ddTime = Label(sleep,text = "Hour  Min   Sec",font=60).place(x = 155)
        setYourAlarm = Label(sleep,text = "When did you sleep?",fg="blue",relief = "solid",font=("Times New Roman",8,"bold")).place(x=10, y=29)
        setYourAlarm = Label(sleep,text = "When did you wake up?",fg="blue",relief = "solid",font=("Times New Roman",8,"bold")).place(x=10, y=50)
        # The Variables we require to set the alarm(initialization):
        hour = StringVar()
        min = StringVar()
        sec = StringVar()
        hour1= StringVar()
        min1= StringVar()
        sec1= StringVar()
        #Time required to set the alarm sleep:
        hourTime= Entry(sleep,textvariable = hour,bg = "pink",width = 15).place(x=150,y=30)
        minTime= Entry(sleep,textvariable = min,bg = "pink",width = 15).place(x=200,y=30)
        secTime = Entry(sleep,textvariable = sec,bg = "pink",width = 15).place(x=250,y=30)
        hourTime2= Entry(sleep,textvariable = hour1,bg = "pink",width = 15).place(x=150,y=50)
        minTime2= Entry(sleep,textvariable = min1,bg = "pink",width = 15).place(x=200,y=50)
        secTime2= Entry(sleep,textvariable = sec1,bg = "pink",width = 15).place(x=250,y=50)
        submit = Button(sleep,text = "Check suggestions",fg="red",width = 20,command = actual_time1).place(x =120,y=80)
        sleep.mainloop()
    elif i==3:
        break
    
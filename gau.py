from tkinter import *
import tkinter as tk
import datetime
import time
import winsound
def answer():
    answer_1=tk.Tk()
    answer_1.title("Answer page 1")
    answer_1.geometry("400x200")
    time_format=Label(answer_1, text= "Enter time in 24 hour format!", fg="cyan",bg="black",font="Calibri").place(x=60,y=120)
    answer_1.after(30000,lambda:answer_1.destroy())
    answer_1= Button(answer_1,text = "Next page",fg="red",width = 15,command=answer2).place(x =135,y=60)
    answer_1.mainloop()

question=Tk()
question.title("Module 1")
question.geometry("400x200")
question.after(30000,lambda:question.destroy())
submit= Button(question,text = "Show Solution",fg="red",width = 15,command =answer).place(x =135,y=60)
question.mainloop()
print("Hello world")

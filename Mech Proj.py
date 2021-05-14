from tkinter import *
import tkinter as tk
import datetime
import time
import winsound
def answer():
    answer=Tk()
    answer.title("Answer page 1")
    answer.geometry("400x200")
    answer.after(10000,lambda:answer.destroy())
    answer= Button(answer,text = "Next page",fg="red",width = 15,command=answer2).place(x =135,y=60)
    #answer.mainloop()
def answer2():
    answer2=Tk()
    answer2.title("Answer page 2")
    answer2.geometry("400x200")
    answer2.after(30000,lambda:answer2.destroy())
    #answer2= Button(question,text = "Next page",fg="red",width = 15,command = answer2).place(x =135,y=60)
    answer2.mainloop()
question=Tk()
question.title("Module 1")
question.geometry("400x200")
question.after(30000,lambda:question.destroy())
submit= Button(question,text = "Show Solution",fg="red",width = 15,command =answer).place(x =135,y=60)
question.mainloop()
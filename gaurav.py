import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
def answer():
    image = mpimg.imread(r'C:\Users\user\Desktop\Lando_2020_1600_x_1200.jpg')
    fig=plt.imshow(image)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()
    print("Hello World")
    answer2()
def answer2():
    image=mpimg.imread(r'C:\Users\user\Desktop\F1\wallpaper.jpg')
    fig=plt.imshow(image)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()
    print("Whats up?")

question=Tk()
question.title("Module 1")
question.geometry("400x200")
#question.after(30000,lambda:question.destroy())
submit = Button(question,text = "Show Solution",fg="red",width = 15,command = answer).place(x =135,y=60)
question.mainloop()
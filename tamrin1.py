import numpy as np
import random
arr=np.empty((0,3),int)
arr=np.append(arr,np.array([["category","genre","names"]]),axis=0)
def movie_rec(choice):
    if choice==a:
        print("your",choice,"movie","name is",c,"with the code of",code)
    else:
        print("this item is not available here pls try again!")
zero=int(input("enter the number of genres u want:"))
for i in range(0,zero):
    code=random.randint(2000,3000)
    a=str(input(" enter the name of the genre:"))       
    c=(str(input("enter the name of the movie:")))
    x=str(input("enter ur choice of genre:"))
    arr=np.append(arr,np.array([[code,a,c]]),axis=0)
    print(arr)
    movie_rec(x)

def movie_rec(choice):
    if choice==a:
        print("your",choice,"names are",x,"with the code of",code)
    else:
        print("this item is not available here pls try again!")
    

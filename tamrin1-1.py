import numpy as np
import random
list1=[]
list2=[]
list3=[]
list4=[]
def rec_style(n):
    if d/id==parent:
      print (parent,":",id,",")
      list2.append(parent)
      list3.append(id)
    else:
      print("not")
arr=np.empty((0,3),int)
arr=np.append(arr,np.array([["id","code","parent"]]),axis=0)
x=int(input("pls enter the number of ur info:"))
for i in range(0,x):
     id=i+1
     code=random.randint(2000,3000)
     parent=int(input("enter the number of parent:"))
     d=parent*id
     arr=np.append(arr,np.array([[id,code,parent]]),axis=0)          
     list1.append(parent)
     list1.append(id)
     list1.append("////")
     rec_style(parent)     
     print(list2)
     print(list3)
     print(arr)
     print(list1)
     print("_____________________________________________")
print(list2)#parent
print(list3)#id
#print("______________________________________________________________")





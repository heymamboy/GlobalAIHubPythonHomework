# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:33:03 2020

@author: dogru
"""

name=input("Please write your name: ")
surname=input("Please write your surname: ")

if name.isalpha() and surname.isalpha():
    print("welcome")
    
else:
    name=input("Please write your name: ")
    surname=input("Please write your surname: ")
    if name.isalpha() and surname.isalpha():
        print("welcome")
    else:
        name=input("Please write your name: ")
        surname=input("Please write your surname: ")
        if name.isalpha() and surname.isalpha():
            print("welcome")
        else:
            print("Please try again later")

lst = []            
n = int(input("Enter number of courses : "))    
if 3<=n<5:
    for i in range(0, n): 
        ele = str(input())   
        lst.append(ele)
    print(lst) 
    v=input("You have to choose one of these courses and take an exam. Please write what you get from which exam and seperate them by ':', example-> midterm:your score final:your score project:your score. ") 
    temp=v.split(' ')
    v=[]
    for i in range(len(temp)):
        k=temp[i].split(':')
        v.append(k)

    keys=[]
    values=[]
    for i in range(0,3):
        keys.append(v[i][0])
        values.append(int(v[i][1]))

    grade_dictionary = dict(zip(keys, values))

    print(grade_dictionary)
    
    midterm=values[0]*(100/30)
    final=values[1]*(100/50)
    project=values[2]*(100/20)
    summ=midterm+final+project
    if summ>90:
        print("You got AA")
    elif 70<summ<90:
        print("You got BB")
    elif 50<summ<70:
        print("You got CC")
    elif 30<summ<50:
        print("You got DD")
    else:
        print("You got FF")
    
else:
    print("You failed in class")        




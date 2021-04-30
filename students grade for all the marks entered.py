# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:48:17 2021

@author: anila
"""

n=int(input("enter the number of students : "))
student_list=[]
grade_list=[]
s=1
for i in range (1,n+1):
    student_list.append(int(input("enter the students total marks: ")))
print("marks list of student according to their roll number = " ,student_list)
for s in range(0,len(student_list)):
    if(student_list[s]>=91 and student_list[s] <=100):
        grade = "A"
    elif(student_list[s]>=81 and student_list[s] <=90):
        grade = "B"
    elif(student_list[s]>=71 and student_list[s]<=80):
        grade = "C"
    elif(student_list[s]>=61 and student_list[s]<=70):
        grade = "D"
    else:
        grade ="O"  
    print(grade)
           
        
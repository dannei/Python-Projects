#calculate average grade for the class
stdPass=0
stdFail=0
A=0
B=0
C=0
D=0
F=0

#ask user for number of students in class
numberStds=int(input("Enter number of students: "))
total=0
i=1
grade_list=[]

#using a loop, ask user to input grade for each student
for gradeCounter in range (1, numberStds+1):
    grade=float(input("Enter grade for student " +str(i)+ ": "))
    i=i+1
    total=total+grade
    grade_list.append(grade)
    if grade>=91 and grade<=100:
        stdPass=stdPass+1
        A=A+1
        print ("A")
    elif grade>=81 and grade<=90:
        stdPass=stdPass+1
        B=B+1
        print ("B")
    elif grade>=71 and grade<=80:
        stdPass=stdPass+1
        C=C+1
        print ("C")
    elif grade>=60 and grade<=70:
        stdPass=stdPass+1
        D=D+1
        print ("D")
    elif grade<60 and grade>=0:
        stdFail=stdFail+1
        F=F+1
        print ("F")    
    else:
        print("invalid entry")

#Calculate Max, Min, and Range
highScore=max(grade_list)
lowScore=min(grade_list)
Range=highScore-lowScore
print("Highest Grade is:", highScore)
print("Lowest Grade is:", lowScore)
print("Range:", Range)

#Calculate Average
avg=round(total/numberStds,2)
print ("Average grade:", avg)

#Display number of students pass or fail
print ("No. of Students passed:", stdPass)
print ("No. of Students failed:", stdFail)

# Display Number of each grades and ratios
numOfGrades=A+B+C+D+F
print("Number of grades entered:", numOfGrades)
print ("No. of As:", A, "%15s"%"Ratio:", round(A/numOfGrades,2))
print ("No. of Bs:", B, "%15s"%"Ratio:", round(B/numOfGrades,2))
print ("No. of Cs:", C, "%15s"%"Ratio:", round(C/numOfGrades,2))
print ("No. of Ds:", D, "%15s"%"Ratio:", round(D/numOfGrades,2))
print ("No. of Fs:", F, "%15s"%"Ratio:", round(F/numOfGrades,2))






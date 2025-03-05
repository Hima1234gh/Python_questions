"""To accept student's five courses marks and compute his/her result. Student is
passing if he/she scores marks equal to and above 40 in each course. If student
scores aggregate greater than 75%, then the grade is distinction. If aggregate is
60>= and <75 then the grade if first division. If aggregate is 50>= and <60, then
the grade is second division. If aggregate is 40>= and <50, then the grade is
third division.""" 

marks = []
aggregate_marks = 0

for i in range(5):
    mark = float(input(f"Enter marks for course {i+1}: "))
    marks.append(mark)

total_marks = int(input("Enter Total Marks : "))

for i in marks :
    aggregate_marks =  i + aggregate_marks

aggregate_marks = aggregate_marks / total_marks * 100
print("Your Aggregate Score is : ",aggregate_marks)

if aggregate_marks >= 40 :
    print("PASS")
    if aggregate_marks > 75 :
        print("Grade : Distinction")
    elif aggregate_marks < 75 and aggregate_marks >= 60:
        print("Grade : First Division")
    elif aggregate_marks >= 50 and aggregate_marks < 60:
        print("Grade : Second Division")
    elif aggregate_marks >= 40 and aggregate_marks < 50 :
        print("Grade : Third Division")
else : 
    print("Fail")


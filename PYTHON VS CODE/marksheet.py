name_of_student=str(input("enter name of student"))
roll_number=int(input("enrter roll number of the student"))
school_name=str(input("enter school name"))
english_marks=float(input("enter english marks of the student"))
urdu_marks=float(input("enter urdu marks of the student"))
physics_marks=float(input("enter physics marks of the student"))
chemistry_marks=float(input("enter chemistry marks of the student"))
maths_marks=float(input("enter mathematics marks of the student"))
sum_of_marks_gained=english_marks+urdu_marks+physics_marks+chemistry_marks+maths_marks
if sum_of_marks_gained<=500.0:

 total_marks=500
 percentage=(sum_of_marks_gained/total_marks)*100
 if(percentage>=80 and percentage<=100):

     grade="A-ONE"
 elif(percentage>=70 and percentage<80):
     grade="A"
 elif(percentage>=60 and percentage<70):
     grade="B"
 elif(percentage>=50 and percentage<60):
    grade="c"
 elif(percentage>=40 and percentage<50):
     grade="D"
 else:
    grade="FAIL"
 print ("  ")
 print("   ")
 print("__________________________________________________________________________________________")

 print("Student Name:"+"                 ||"+name_of_student)
 print("Student Rollno:"+"               ||"+str(roll_number))
 print("School name:"+"                  ||"+school_name)
 print("  ")
 print("  ")
 print("------------------------------------------------------------------------------------------")
 print("|| ENGLISH MARKS    |URDU MARKS     |PHYSICS MARKS   |MATHS MARKS    |CHEMISTRY MARKS   ||")
 print("||______________________________________________________________________________________||")
 print("|| "+str(english_marks)+"          " +" | "+str(urdu_marks)+"                 | "+str(physics_marks)+"            |"+str(maths_marks)+"            |"+str(chemistry_marks) +"||")
 print("||______________________________________________________________________________________||")
 print("|| TOTAL GAINED MARKS OUT OF"+"    "+str(total_marks)+" IS     "+str(sum_of_marks_gained)+"                                        ||")
 print("||______________________________________________________________________________________||")
 print("|| PERCENTAGE OF STUDENT                "+str(percentage)+"                                            ||")
 print("||______________________________________________________________________________________||")
 print("||                        GRADE:    "+grade+"                                               ||")
 print("------------------------------------------------------------------------------------------")
 print("  ")
 print("   POWERED BY PYTHON  e-marksheet for schools ")

else:
      print("PLEASE ENTER CORRECT MARKS OF SUBJECTS UNDER 100 MARKING LEVEL !! !!")

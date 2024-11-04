
#assignment3
student_name= ["sandra", "Patricia", "Phionah", "Anitah"]
student_marks=[80,56,78,90]

#print Patricia to Anitah
#hint:slicing
print(student_name[1:4])

#add Masha at the forth position

student_name.insert(3,"Masha")
print(student_name)


#update the name Phiona to Aladina
print("\noriginal list:", student_name)
student_name[3] = "Aladina"
print("updated list:",student_name)


#display the length of the student list
length_of_the_list = len(student_name)
print("\nlenght of the list:", length_of_the_list )


#print all the student names having updated using a for loop
print("\nupdated list:")
for student_name in student_name:
    print(student_name)


#calculate the total marks for the student marks variable and the answer  is 304
student_marks = [80,56,78,90]
total_student_marks = (80 +  56 + 78 + 90)
print(f"\nThe total student marks:{total_student_marks}")


# Input student details
name = input("Enter Name: ")
roll_number = input("Enter Roll Number: ")
marks = float(input("Enter Marks out of 100: "))

# Determine grade point and remark
if marks >= 90:
    grade_point, remark = 10, "OUTSTANDING"
elif marks >= 80:
    grade_point, remark = 9, "VERY GOOD"
elif marks >= 70:
    grade_point, remark = 8, "GOOD"
elif marks >= 60:
    grade_point, remark = 7, "AVERAGE"
elif marks >= 50:
    grade_point, remark = 6, "PASS"
else:
    grade_point, remark = 0, "FAIL"

print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks}")
print(f"Grade Point: {grade_point}")
print(f"Remark: {remark}")

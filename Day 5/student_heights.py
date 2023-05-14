student_heights=input("Input a list of heights: ").split(", ")
sum=0
for n in range(0,len(student_heights)):
  student_heights[n]=int(student_heights[n])
  sum=sum+student_heights[n]
average=round(float(sum)/float(len(student_heights)))
print(student_heights)
print(average)
  
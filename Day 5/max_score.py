student_scores = input("Input a list of scores: ").split()
maxim = int(student_scores[0])

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > maxim:
    maxim = student_scores[n]
print(maxim)
#min sau max function
#max(student_scores)
#min(student_scores)
#range(1, 101, 3)->de la 1 la 101-1 cu pas=3
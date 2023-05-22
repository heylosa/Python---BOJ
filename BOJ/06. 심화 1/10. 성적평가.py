name_of_subject = []
subject_grade = []
subject_grade2 = []


for j in range (20):
    major_grade = list(input().split())
    name_of_subject.append(str(major_grade[0]))
    subject_grade.append(float(major_grade[1]))
    subject_grade2.append(str(major_grade[2]))
    if subject_grade2[j] == 'P':
        subject_grade[j] = subject_grade[j] * 0

sum_subject_grade = sum(subject_grade)

for i in range (20):
    if subject_grade2[i] == 'A+':
            subject_grade[i] = subject_grade[i] * 4.5
    elif subject_grade2[i] == 'A0':
            subject_grade[i] = subject_grade[i] * 4.0
    elif subject_grade2[i] == 'B+':
            subject_grade[i] = subject_grade[i] * 3.5
    elif subject_grade2[i] == 'B0':
            subject_grade[i] = subject_grade[i] * 3.0
    elif subject_grade2[i] == 'C+':
            subject_grade[i] = subject_grade[i] * 2.5
    elif subject_grade2[i] == 'C0':
            subject_grade[i] = subject_grade[i] * 2.0
    elif subject_grade2[i] == 'D+':
            subject_grade[i] = subject_grade[i] * 1.5
    elif subject_grade2[i] == 'D0':
            subject_grade[i] = subject_grade[i] * 1.0
    elif subject_grade2[i] == 'P':
            subject_grade[i] = subject_grade[i] * 0
    elif subject_grade2[i] == 'F':
            subject_grade[i] = subject_grade[i] * 0

print(sum(subject_grade)/sum_subject_grade)

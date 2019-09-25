def hinne(lectures, practicals, project, quiz1, quiz2, exam, additional):
    s = lectures + practicals + project + quiz1 + quiz2 + exam + additional
    if s > 90:
        return 'A'
    elif s >= 80 and s < 90:
        return 'B'
    elif s >= 70 and s < 80:
        return 'C'
    elif s >= 60 and s < 70:
        return 'D'
    elif s >= 50 and s < 60:
        return 'E'
    elif s < 50:
        return 'F'

in_lectures = float(input('Sisesta loengute punktid: '))
in_practicals = float(input('Sisesta praktikumide punktid: '))
in_project = float(input('Sisesta projekti punktid: '))
in_quiz1 = float(input('Sisesta esimese kontrolltöö punktid: '))
in_quiz2 = float(input('Sisesta teise kontrolltöö punktid: '))
in_exam = float(input('Sisesta eksami punktid: '))
in_additional = float(input('Sisesta lisaülesannete punktid: '))

print(hinne(in_lectures, 
            in_practicals, 
            in_project, 
            in_quiz1, 
            in_quiz2, 
            in_exam, 
            in_additional))
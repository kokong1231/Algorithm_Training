count = int(input())
student = []
sequc = []

for input_status in range(count):
    student.append(input().split(" "))

def seq(student):
    temp_index = 0

    for sec in range(len(student)):
        if float(student[temp_index][1]) > float(student[sec][1]):
            temp_index = sec

        elif float(student[temp_index][1]) == float(student[sec][1]):
            if float(student[temp_index][2]) > float(student[sec][2]):
                temp_index = sec
            
    return student[temp_index]

for sort_ in range(count):
    sequc.append(seq(student))
    del student[student.index(seq(student))]

for prnt in sequc:
    print(prnt[0])
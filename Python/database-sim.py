student1 = {
    'student-number': '2021-00363-CM-0',
    'student-name': 'Shawn Michael Jumawan',
}

# print(student1['student-name'])

if student1['student-name'] == 'Shawn Michael Jumawan':
    print('Hi ' + student1['student-name'])
    print('Your student number is ' + student1['student-number'])
else:
    print('Student unknown')
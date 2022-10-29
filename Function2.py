def display():
    with open('List_of_course.txt', 'r') as file:
        data = file.read()
        data = data.replace('_', ' ')
        print(data.rstrip())


def add(course_code, course_title, course_credit, course_prq):
    with open('List_of_course.txt', 'a') as file:
        file.write(f'{course_code}     {course_title}')
        file.write(' '*(77-len(course_title)))
        file.write(course_credit)
        file.write(' '*(11-len(course_credit)))
        file.write(f'{course_prq}\n')


def update(course_code, choice, new_title, new_credit, new_prq):
    with open('List_of_course.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            line = line.split()
            if course_code == line[0]:
                if choice == 'ct':
                    line[1] = new_title
                elif choice == 'cc':
                    line[2] = new_credit
                elif choice == 'cp':
                    line[3] = new_prq
            file.write(f'{line[0]}     {line[1]}')
            file.write(' '*(77-len(line[1])))
            file.write(line[2])
            file.write(' '*(11-len(line[2])))
            file.write(f'{line[3]}\n')


def lst():
    code_lst = []
    title_lst = []
    prq_lst = []
    with open("List_of_course.txt", 'r') as file:
        lines = file.readlines()
        for line_lst in lines:
            line_lst = line_lst.split()
            code_lst.append(line_lst[0])
            title_lst.append(line_lst[1])
            prq_lst.append(line_lst[3])
    return lines, code_lst, title_lst, prq_lst


def code_validate():
    while True:
        try:
            course_code = int(input("Enter course code(*It is unchangeable and unique must be 1234 digit integer): "))
            course_code = str(course_code)
            if len(course_code) == 4:
                break
            else:
                print('Course code must be 4 digits.')
        except ValueError:
            print('Course code must be integer.')
    return course_code


def add_code_validate():
    lines, codes, titles, pres = lst()
    course_code = code_validate()
    while True:
        if course_code in codes:
            for line in lines:
                line = line.split()
                if course_code == line[0]:
                    print(f'Course code match with code of {line[1]}')
                    course_code = input('Try another code or enter home go home: ')
                    if course_code.title() == 'Home':
                        break
                    else:
                        break
        elif course_code == 'Home':
            break
        else:
            break
    return course_code


def title_validate(course_title):
    lines, codes, titles, pres = lst()
    course_title = course_title.upper()
    course_title = course_title.replace(' ', '_')
    while True:
        if course_title in titles:
            for line in lines:
                line = line.split()
                if course_title == line[1]:
                    print(f'The title of course code {line[0]} is same: ')
                    course_title = input('Try another title or enter home to  go home: ')
                    course_title = course_title.upper()
                    course_title = course_title.replace(' ', '_')
                    if course_title.title() == 'Home':
                        break
                    else:
                        break
        elif course_title == 'Home':
            break
        else:
            break
    return course_title


def credit_validate(course_credit):
    while True:
        if course_credit == '1' or course_credit == '2' or course_credit == '3':
            break
        else:
            print('Course credit must be 1 to 3.')
            course_credit = input('Enter course credit again: ')
    return course_credit


def prq_validate(course_prq):
    lines, codes, titles, pres = lst()
    if course_prq in codes or course_prq == '-':
        function_prq = '1'
    else:
        print('Prerequisites course is not added in the list. Please add the prerequisites course first.')
        while True:
            function_prq = input('Enter add to add course or home to go home: ')
            if function_prq.title() == 'Add':
                break
            elif function_prq.title() == 'Home':
                break
            else:
                print('Enter invalid function.')
    return course_prq, function_prq


def update_code_validate():
    course_code = input('Enter the course code you want to update: ')
    lines, codes, titles, pres = lst()
    while True:
        if course_code in codes:
            break
        else:
            print(f'Course is not exist in the list')
            course_code = input('Try another code or enter home go home: ')
            if course_code.title() == 'Home':
                break
            else:
                pass
    return course_code


def choice_validate():
    while True:
        choice = input("Enter which you want to change,\n"
                       "Course title = ct\n"
                       "Course Credit = cc\n"
                       "Prerequisites = cp : ")
        new_title = '0'
        new_credit = '0'
        new_prq = '0'
        function = '1'
        if choice == 'ct':
            new_title = input("Enter your new course title: ")
            new_title = title_validate(new_title)
            if new_title.title() != 'Home':
                break
            else:
                pass
        elif choice == 'cc':
            new_credit = input("Enter your new course credit: ")
            new_credit = credit_validate(new_credit)
        elif choice == 'cp':
            new_prq = input("Enter your new course prerequisites: ")
            new_prq, function = prq_validate(new_prq)
            if function.title() == 'Add':
                break
            elif function.title() == 'Home':
                break
            elif function == '1':
                break
        else:
            print('Invalid choice.')
    return function, choice, new_title, new_credit, new_prq


def delete_prq_update(course):
    with open('List_of_course.txt', 'r+') as file:
        lines = file.readlines()
        checked = 0
        function = '1'
        for line in lines:
            for_cnt = 0
            line = line.split()
            if course == line[3]:
                print(f'Change the prerequisites for {line[1]} if you want '
                      f'to delete the course which code is {course}.')
                while True:
                    x = input(f'Enter check to check if another '
                              f'course have also prerequisites {course} or not: ')
                    if x.title() == 'Check':
                        for_cnt = 1
                        checked = 1
                        break
                    else:
                        pass
                if for_cnt == 1:
                    continue
            elif for_cnt == 0:
                pass
            else:
                pass
        if checked == 1:
            print(f'No other course have prerequisites {course}')
            while True:
                function = input("Enter update for update prerequisites or home "
                                 "if you dont want to delete course: ")
                if function.title() == 'Home':
                    break
                elif function.title() == 'Update':

                    break
                else:
                    print('Enter invalid function.')
    return function


def delete(course):
    with open('List_of_course.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            line = line.split()
            if course == line[0]:
                del line
            else:
                file.write(f'{line[0]}     {line[1]}')
                file.write(' ' * (77 - len(line[1])))
                file.write(line[2])
                file.write(' ' * (11 - len(line[2])))
                file.write(f'{line[3]}\n')


def details(course):
    with open('List_of_course.txt', 'r') as file:
        lines = file.readlines()
        n = 1
        for line in lines:
            line = line.split()
            if course == line[0] or course == line[1] or n == 1:
                print(f'{line[0]}     {line[1]}', end='')
                print(' ' * (77 - len(line[1])), end='')
                print(line[2], end='')
                print(' ' * (11 - len(line[2])), end='')
                print(f'{line[3]}', )
                n = 2
            else:
                pass


def search(course):
    with open('List_of_course.txt', 'r') as file:
        lines = file.readlines()

    n = 1
    for line in lines:
        line = line.replace('_', ' ')
        if n == 1 and course in line:
            print(line.rstrip())
            n = 2
        elif course in line:
            print(line.rstrip())

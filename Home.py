import Function2 as Fc
functions = '''Enter ___ to do ___
1. List to see list of course.
2. Add to add new course.
3. Update to update course.
4. Delete to delete course.
5. Details to course details
6. Search to search course'''
print(functions)
function = input("Choose your function: ")
while function != 'quit':
    if function.title() == 'List' or function == '1':
        Fc.display()

    elif function.title() == 'Add' or function == '2':
        main_while_cnt = 0
        Course_Code = Fc.add_code_validate()
        if Course_Code != 'Home':
            Course_Title = input('Enter course title(*Unique): ')
            Course_Title = Fc.title_validate(Course_Title)
            if Course_Title != 'Home':
                Course_Credit = input('Enter course credit 1 to 3: ')
                Course_Credit = Fc.credit_validate(Course_Credit)
                Course_Prq = input('Enter course prerequisites(course code or -): ')
                Course_Prq, function = Fc.prq_validate(Course_Prq)
                if function.title() == 'Add':
                    continue
                elif function.title() == 'Home':
                    pass
                elif function == '1':
                    Fc.add(Course_Code, Course_Title, Course_Credit, Course_Prq)
                    print('Course added successfully.')
                    while True:
                        function = input('Enter add to add more or list to see the list home or go home: ')
                        if function.title() == 'Add':
                            main_while_cnt = 1
                            break
                        elif function.title() == 'Home':
                            break
                        else:
                            print('Enter invalid function.')
            else:
                pass
        else:
            pass
        if main_while_cnt == 1:
            continue
        else:
            pass

    elif function.title() == 'Update' or function == '3':
        main_while_cnt = 0
        Fc.display()
        Course_Code = Fc.update_code_validate()
        if Course_Code.title() != 'Home':
            function, choice, new_title, new_credit, new_prq = Fc.choice_validate()
            if function.title() == 'Add':
                continue
            elif function.title() == 'Home' or new_title.title() == 'Home':
                break
            elif function == '1':
                Fc.update(Course_Code, choice, new_title, new_credit, new_prq)
                print('Undated Successfully.')
                while True:
                    function = input('Enter update to update more or list to see updated list home or go home: ')
                    if function.title() == 'Update' or function.title() == 'List':
                        main_while_cnt = 1
                        break
                    elif function.title() == 'Home':
                        break
                    else:
                        print('Enter invalid function.')

        else:
            pass
        if main_while_cnt == 1:
            continue
        else:
            pass

    elif function.title() == 'Delete' or function == '4':
        Fc.display()
        with open('List_of_course.txt', 'r') as file:
            data = file.read()
            while True:
                course = input("Enter the course code you want to delete: ")
                if course in data:
                    Fc.delete(course)
                    print("deleted successfully")
                    break
                else:
                    print('The course is not exist.')

    elif function.title() == 'Details' or function == '5':
        with open('List_of_course.txt', 'r') as file:
            lines = file.readlines()
            while True:
                de_v = 0
                course = input('Enter course code,title or home :')
                course = course.upper()
                course = course.replace(' ', '_')
                for line in lines:
                    line = line.split()
                    if course == line[0] or course == line[1]:
                        Fc.details(course)
                        de_v = 1
                        break
                    elif course == 'HOME':
                        de_v = 2
                if de_v == 2:
                    break
                elif de_v == 0:
                    print('Course not found.')

    elif function.title() == 'Search' or function == '6':
        with open('List_of_course.txt', 'r') as file:
            lines = file.readlines()
            while_brk = 0
            main_while_cnt = 0
            while True:
                course = input('Enter what you want to search or home: ')
                course = course.upper()
                course = course.replace(' ', '_')
                for line in lines:
                    line = line.split()
                    if course in line[0] or course in line[1]:
                        Fc.search(course)
                        break
                    elif course.title() == 'Home':
                        break
                else:
                    print('The course is not added.')
                    while True:
                        function = input("Add course or go Back: ")
                        if function.title() == 'Add':
                            main_while_cnt = 1
                            while_brk = 1
                            break
                        elif function.title() == 'Back':
                            while_brk = 1
                            break
                        else:
                            print('Invalid function entered.')
                    if while_brk == 1:
                        break
            if main_while_cnt == 1:
                continue

    functions = '''1. List
2. Add
3. Update
4. Delete
5. Details
6. Search'''
    print(functions)
    function = input("Enter quit to finish the program or continue entering function number: ")

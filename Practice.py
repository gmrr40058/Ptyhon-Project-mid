def code_prq_validate():
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
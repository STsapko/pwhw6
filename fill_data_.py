from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_INSTRUCTORS = 3
NUMBER_GROUPS = 3
NUMBER_GRADES = 20

groups = [f'Group#{group_number + 1:0>2}' for group_number in range(NUMBER_GROUPS)]
subjects = ['math', 'science', 'history', 'geography', 'biology', 'chemistry', 'physics', 'algebra']

def generate_fake_data(number_students, number_instructors) -> tuple():
    fake_students = []
    fake_instructors = []
    
    fake_data = faker.Faker()
    
    for _ in range(number_students):
        fake_students.append(fake_data.name())
            
    for _ in range(number_instructors):
        fake_instructors.append(fake_data.name())
         
    return fake_students, fake_instructors

def prepare_data(students, instructors) -> tuple():
    
    for_groups = [(group, ) for group in groups]
          
    for_students = [(student, randint(1, NUMBER_GROUPS)) for student in students]
            
    for_instructors = [(instructor, ) for instructor in instructors]
    
    for_subjects = [(subject, randint(1, NUMBER_INSTRUCTORS)) for subject in subjects]
    
    for_grades = []
    
    for _ in range(NUMBER_GRADES):
        grade = randint(1, 5)
        student_id = randint(1, NUMBER_STUDENTS + 1)
        subject_id = randint(1, len(subjects) + 1)
        month = randint(1, 12)
        day = randint(1, 28)
        grade_date = datetime(2023, month, day).date()
        
        for_grades.append((grade, student_id, subject_id, grade_date))
        
    return for_groups, for_students, for_instructors, for_subjects, for_grades

def insert_data_to_db(groups, students, instructors, subjects, grades) -> None:
    
    with sqlite3.connect('school.db') as con:
        
        cur = con.cursor()
        
        sql_to_groups = """INSERT INTO groups(group_name)
        VALUES (?)"""
        
        cur.executemany(sql_to_groups, groups)
        
        sql_to_students = """INSERT INTO students(student, group_id)
        VALUES(?, ?)"""
        
        cur.executemany(sql_to_students, students)

        sql_to_instructors = """INSERT INTO instructors(instructor)
        VALUES (?)"""
        
        cur.executemany(sql_to_instructors, instructors)

        sql_to_subjects = """INSERT INTO subjects(subject, instructor_id)
        VALUES(?, ?)"""
        
        cur.executemany(sql_to_subjects, subjects)
        
        sql_to_grades = """INSERT INTO grades(grade, student_id, subject_id, grade_date)
        VALUES(?, ?, ?, ?)"""
        
        cur.executemany(sql_to_grades, grades)
        
        con.commit()

if __name__ == '__main__':
    groups, students, instructors, subjects, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_INSTRUCTORS)) 
    print(groups)
    print(students)
    print(instructors)
    print(subjects)
    print(grades)
    insert_data_to_db(groups, students, instructors, subjects, grades)
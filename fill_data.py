from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 3
NUMBER_POINTS = 20


def generate_fake_data(number_students, number_groups, number_teachers, number_subject) -> tuple():
    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []
    points = [1, 2, 3, 4, 5]

    fake_data = faker.Faker('uk-UA')

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for index, _ in enumerate(range(number_groups)):
        fake_groups.append(index + 1)

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_subject):
        fake_subjects.append(fake_data.job())

    return fake_students, fake_groups, fake_teachers, fake_subjects, points


def prepare_data(students, groups, teachers, subjects, points) -> tuple():
    for_groups = []

    for group in groups:
        for_groups.append((group, ))

    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher,))

    for_points = []

    for point in points:
        for_points.append((point,))

    for_students = []

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_subjects = []

    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_education = []

    for student_id in range(1, NUMBER_STUDENTS + 1):
        for subject_id in range(1, NUMBER_SUBJECTS + 1):
            for_education.append((student_id, subject_id, randint(1, len(points)),
                                  datetime(2021, 12, randint(7, 15)).date()))

    return for_groups, for_teachers, for_points, for_students, for_subjects, for_education


def insert_data_to_db(groups, teachers, points, students, subjects, education) -> None:
    with sqlite3.connect('education.db') as con:
        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_points = """INSERT INTO points(point)
                               VALUES (?)"""
        cur.executemany(sql_to_points, points)

        sql_to_students = """INSERT INTO students(name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_subjects = """INSERT INTO subjects(subject, teacher_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_education = """INSERT INTO education(student_id, subject_id, point_id, point_time)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_education, education)

        con.commit()


if __name__ == "__main__":
    print(generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS))
    students, groups, teachers, subjects, points = generate_fake_data(NUMBER_STUDENTS,
                                                                      NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    groups, teachers, points, students, subjects, education = prepare_data(students, groups, teachers, subjects, points)
    print(groups)
    print(students)
    print(education)
    insert_data_to_db(groups, teachers, points, students, subjects, education)

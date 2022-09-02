import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('education.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql_1 = """
SELECT s.name, round(avg(p.point), 2) as grade
from education e 
left join students s on s.id = e.student_id 
left join points p on p.id = e.point_id 
GROUP BY s.id 
ORDER BY grade desc
limit 5;
"""

sql_2 = """
SELECT s2.subject, s.name, round(avg(p.point), 2) as grade
from education e 
left join students s on s.id = e.student_id 
left join points p on p.id = e.point_id 
left join subjects s2 on s2.id = e.subject_id 
WHERE e.subject_id  = 1
GROUP BY s.id, s2.id 
ORDER BY grade desc
limit 1;
"""

sql_3 = """
SELECT s2.subject, g.[group_name], round(avg(p.point), 2) as grade
from education e 
left join students s on s.id = e.student_id 
left join subjects s2 on s2.id = e.subject_id 
left join points p on p.id = e.point_id 
left join groups g on g.id = s.group_id
WHERE s2.id = 2
GROUP BY g.id  
ORDER BY grade desc;
"""

sql_4 = """
SELECT g.[group_name], round(avg(p.point), 2) as grade
from education e 
left join students s on s.id = e.student_id 
left join points p on p.id = e.point_id 
left join groups g on g.id = s.group_id
WHERE g.id = 1
GROUP BY g.id;
"""

sql_5 = """
SELECT s.subject, t.teacher_name
from subjects s 
left join teachers t on t.id = s.teacher_id 
WHERE t.id = 3
GROUP BY s.id 
"""

sql_6 = """
SELECT s.name, g.group_name
from students s 
left join groups g on g.id = s.group_id
WHERE g.id = 2
GROUP BY s.id  
"""

sql_7 = """
SELECT s2.subject, g.[group_name], s.name, p.point
from education e 
left join students s on s.id = e.student_id 
left join points p on p.id = e.point_id 
left join groups g on g.id = s.group_id
left join subjects s2 on s2.id = e.subject_id 
WHERE e.subject_id  = 2 and s.group_id = 1
order BY e.point_id desc
"""

sql_8 = """
SELECT s2.subject, g.[group_name], s.name, p.point, max(e.point_time) as last_date
from education e 
left join students s on s.id = e.student_id 
left join points p on p.id = e.point_id 
left join groups g on g.id = s.group_id
left join subjects s2 on s2.id = e.subject_id 
WHERE e.subject_id  = 1 and s.group_id = 3
"""

sql_9 = """
SELECT s2.name, s1.subject
from education e 
left join students s2 on s2.id = e.student_id 
left join subjects s1 on s1.id = e.subject_id 
WHERE e.student_id = 30
"""

sql_10 = """
SELECT s2.name, s1.subject, t.teacher_name 
from education e 
left join students s2 on s2.id = e.student_id 
left join subjects s1 on s1.id = e.subject_id 
left join teachers t on t.id = s1.teacher_id 
WHERE e.student_id = 30 and s1.teacher_id = 3
"""


sql_11 = """
SELECT s2.name, t.teacher_name, round(avg(p.point), 2) as grade
from education e 
left join students s2 on s2.id = e.student_id 
left join subjects s1 on s1.id = e.subject_id 
left join teachers t on t.id = s1.teacher_id 
left join points p on p.id = e.point_id 
WHERE s1.teacher_id = 3
GROUP by e.student_id 
order by grade desc
"""


sql_12 = """
SELECT t.teacher_name, round(avg(p.point), 2) as grade
from education e 
left join students s2 on s2.id = e.student_id 
left join subjects s1 on s1.id = e.subject_id 
left join teachers t on t.id = s1.teacher_id 
left join points p on p.id = e.point_id 
WHERE s1.teacher_id = 2
"""


if __name__ == '__main__':
    print('--- Select First ---')
    print(execute_query(sql_8))
    print()

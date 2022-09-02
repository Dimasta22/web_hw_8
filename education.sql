-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: points
DROP TABLE IF EXISTS points;
CREATE TABLE points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    point INTEGER UNIQUE NOT NULL
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject VARCHAR(255) UNIQUE NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: education
DROP TABLE IF EXISTS education;
CREATE TABLE education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    point_id INTEGER,
    point_time DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
    FOREIGN KEY (point_id) REFERENCES points (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE

);
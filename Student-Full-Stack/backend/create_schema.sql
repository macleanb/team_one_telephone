-- Schema
-- Database name: school

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(10),
    last_name  VARCHAR(10),
    age INT,
    subject INT
);

CREATE TABLE subjects (
    id serial PRIMARY KEY,
    subject VARCHAR(30)
);

CREATE TABLE teachers (
    id serial PRIMARY KEY,
    first_name VARCHAR(10),
    last_name  VARCHAR(10),
    age INT,
    subject INT
);

COPY students FROM '/Users/Wendy/Desktop/BriansCode/whiskey_platoon/W4/Student-Full-Stack/backend/data/student.csv' DELIMITER ',' CSV HEADER;
SELECT setval('students_id_seq', 20, true);  -- next value will be 21

COPY teachers FROM '/Users/Wendy/Desktop/BriansCode/whiskey_platoon/W4/Student-Full-Stack/backend/data/teachers.csv' DELIMITER ',' CSV HEADER;
SELECT setval('teachers_id_seq', 5, true);  -- next value will be 6

COPY subjects FROM '/Users/Wendy/Desktop/BriansCode/whiskey_platoon/W4/Student-Full-Stack/backend/data/subjects.csv' DELIMITER ',' CSV HEADER;
SELECT setval('subjects_id_seq', 5, true);  -- next value will be 6

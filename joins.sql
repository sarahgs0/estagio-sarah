-- joins.sql
-- Exercises about JOINs, subqueries, and CTEs

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    id INTEGER,
    name TEXT
);

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    course_id INTEGER,
    grade REAL

);

INSERT INTO courses VALUES (1, 'Math');
INSERT INTO courses VALUES (2, 'English');
INSERT INTO courses VALUES (3, 'Science');

INSERT INTO students VALUES (1, 'Ana', 1, 8.5);
INSERT INTO students VALUES (2, 'Maria', 2, 9.5);
INSERT INTO students VALUES (3, 'Harry', 3, 6.5);
INSERT INTO students VALUES (4, 'Joshua', 3, 7.5);
INSERT INTO students VALUES (5, 'Emma', 4, 9.0);


SELECT * FROM courses;
SELECT * FROM students;

-- 1. INNER JOIN: show only students that have a matching course
SELECT
    students.name AS student_name,
    courses.name AS course_name,
    students.grade
FROM students
INNER JOIN courses
ON students.course_id = courses.id;

-- 2. LEFT JOIN: show all students, even if they do not have a matching course
SELECT
    students.name AS student_name,
    courses.name AS course_name,
    students.grade
FROM students
LEFT JOIN courses
ON students.course_id = courses.id;

-- 3. Difference between INNER JOIN and LEFT JOIN
-- INNER JOIN shows only students that have a course in the courses table.
-- LEFT JOIN shows all students, even when the student does not have a matching course.

-- 4. Subquery in WHERE: show students with grades above the average
SELECT
    name,
    grade
FROM students
WHERE grade > (
    SELECT AVG(grade)
    FROM students
);

-- 5. CTE with WITH: rewrite the subquery using a CTE
WITH average_students AS (
    SELECT AVG(grade) AS average_grade
    FROM students
)
SELECT
    students.name,
    students.grade
FROM students
JOIN average_students
ON students.grade > average_students.average_grade;

-- 6. Mini-analysis: questions that need JOINs
-- Question 1: Which students are enrolled in each course?
SELECT
    students.name AS student_name,
    courses.name AS course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.id;
-- Question 2: Which students do not have a valid course?
SELECT
    students.name AS student_name,
    courses.name AS course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.id
WHERE courses.name IS NULL;
-- Question 3: What is the average grade for each course?
SELECT
    courses.name AS course_name,
    AVG(students.grade) AS average_grade
FROM courses
INNER JOIN students
ON courses.id = students.course_id
GROUP BY courses.name;
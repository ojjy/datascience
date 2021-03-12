"""
student
student_num
student_name
dept_id
student_type: 0 - alumni , 1 - enrolled students
adm_date

dept
dept_id
dept_name

sql statements

CREATE TABLE IF NOT EXISTS dept(
    dept_id INT,
    dept_name TEXT,
    PRIMARY KEY(dept_id)
);

CREATE TABLE IF NOT EXISTS student(
    student_num INT,
    student_name TEXT NOT NULL,
    dept_id TEXT,
    student_type INTEGER DEFAULT 0,
    adm_date DATE,
    PRIMARY KEY (student_num),
    FOREIGN KEY (dept_id)
        REFERENCES dept(dept_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

# Multiple row insertion
INSERT INTO dept (dept_id, dept_name) VALUES ("Computer Science"),
                                             ("Mechanical Engineer"),
                                             ("Medicine),
                                             ("Piano"),
                                             ("Economy"),
                                             ("History"),
                                             ("Law");

# Insert into Select
CREATE TABLE IF NOT EXISTS dept_backup(
    dept_id INTEGER AUTOINCREMENT,
    dept_name TEXT,
    PRIMARY KEY(dept_id)
);

INSERT INTO dept_backup
SELECT dept_id, dept_name FROM dept;

SELECT * FROM dept_backup;
"""
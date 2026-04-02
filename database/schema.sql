



CREATE TABLE IF NOT EXISTS levels (
    level_id INT PRIMARY KEY,
    level_name VARCHAR(50) NOT NULL
);


-- Admins Table
-
CREATE TABLE IF NOT EXISTS admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


-- Teachers Table

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    level_id INT NOT NULL,
    password VARCHAR(255) NOT NULL,
    CONSTRAINT fk_teacher_level
        FOREIGN KEY (level_id) REFERENCES levels(level_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);


-- Students Table

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT,
    level_id INT NOT NULL,
    password VARCHAR(255) NOT NULL,
    CONSTRAINT fk_student_level
        FOREIGN KEY (level_id) REFERENCES levels(level_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);


-- Lessons Table

CREATE TABLE IF NOT EXISTS lessons (
    lesson_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    teacher_id INT NOT NULL,
    level_id INT NOT NULL,
    date_uploaded DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_lesson_teacher
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_lesson_level
        FOREIGN KEY (level_id) REFERENCES levels(level_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);




-- Schedule Table

CREATE TABLE IF NOT EXISTS schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    level_id INT NOT NULL,
    day VARCHAR(20) NOT NULL,
    time VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    CONSTRAINT fk_schedule_level
        FOREIGN KEY (level_id) REFERENCES levels(level_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

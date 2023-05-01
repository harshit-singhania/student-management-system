CREATE DATABASE student_database;

USE student_database;

CREATE TABLE Admin (
  AID INT PRIMARY KEY,
  LoginName VARCHAR(50),
  Password VARCHAR(50),
  Name VARCHAR(100)
);

CREATE TABLE CourseMst (
  CID INT PRIMARY KEY,
  CName VARCHAR(100),
  Fees DECIMAL(10, 2),
  Duration INT
);

CREATE TABLE StudentMst (
  SID INT PRIMARY KEY,
  Name VARCHAR(100),
  Course VARCHAR(100),
  EducationDetail TEXT,
  PersonalDetails TEXT,
  FeesDetails TEXT
);

CREATE TABLE TeacherMst (
  TID INT PRIMARY KEY,
  TName VARCHAR(100),
  Course VARCHAR(100),
  Education TEXT
);

-- Add data to Admin table
INSERT INTO Admin VALUES
  (1, 'admin1', 'password1', 'John Doe'),
  (2, 'admin2', 'password2', 'Jane Smith'),
  (3, 'admin3', 'password3', 'Bob Johnson'),
  (4, 'admin4', 'password4', 'Sarah Lee'),
  (5, 'admin5', 'password5', 'David Chen');

-- Add data to CourseMst table
INSERT INTO CourseMst VALUES
  (1, 'Mathematics', 1500.00, 120),
  (2, 'English', 1000.00, 90),
  (3, 'Science', 2000.00, 150),
  (4, 'History', 1200.00, 80),
  (5, 'Computer Science', 2500.00, 180);

-- Add data to StudentMst table
INSERT INTO StudentMst VALUES
  (1, 'Alice Smith', 'English', 'High School Diploma', 'DOB: 01/01/2000, Address: 123 Main St., Phone: 123-456-7890', 'Paid in Full'),
  (2, 'Bob Johnson', 'Mathematics', 'Bachelors Degree', 'DOB: 02/02/2001, Address: 456 Elm St., Phone: 987-654-3210', 'Payment Plan'),
  (3, 'Charlie Brown', 'Science', 'Associates Degree', 'DOB: 03/03/2002, Address: 789 Oak St., Phone: 555-555-5555', 'Paid in Full'),
  (4, 'David Lee', 'Computer Science', 'Masters Degree', 'DOB: 04/04/2003, Address: 1010 Pine St., Phone: 111-111-1111', 'Payment Plan'),
  (5, 'Emily Wong', 'Art', 'High School Diploma', 'DOB: 05/05/2004, Address: 1212 Maple St., Phone: 222-222-2222', 'Paid in Full');

-- Add data to TeacherMst table
INSERT INTO TeacherMst VALUES
  (1, 'Mr. Johnson', 'Mathematics', 'Bachelor\'s Degree'),
  (2, 'Ms. Smith', 'English', 'Master\'s Degree'),
  (3, 'Dr. Lee', 'Science', 'PhD'),
  (4, 'Ms. Brown', 'History', 'Bachelor\'s Degree'),
  (5, 'Mr. Chen', 'Computer Science', 'Master\'s Degree');

select * from StudentMst;
select *  from TeacherMst;
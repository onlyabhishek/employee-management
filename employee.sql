-- Create a new database
CREATE DATABASE employee;

-- Use the 'employee' database
USE employee;

-- Create a table for Employee
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- Create a table for EmployeePhoneNumbers
CREATE TABLE EmployeePhoneNumbers (
    PhoneNumberID INT PRIMARY KEY,
    EmployeeID INT,
    PhoneNumber VARCHAR(15),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create a table for Document
CREATE TABLE Document (
    DocumentID INT PRIMARY KEY,
    DocumentName VARCHAR(100),
    UploadDate DATE,
    Deadline DATE,
    EmployeeID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create a table for Department
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50),
    Description TEXT,
    EmployeeID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create a table for Attendance
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY,
    EmployeeID INT,
    Status VARCHAR(10),
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create a table for LeaveRequest
CREATE TABLE LeaveRequest (
    ReviewID INT PRIMARY KEY,
    EmployeeID INT,
    ReviewDate DATE,
    Details TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Rename the 'LeaveRequest' table to 'PerformanceReview'
RENAME TABLE LeaveRequest TO PerformanceReview;

-- Create a table for Leave
CREATE TABLE Leave (
    LeaveID INT PRIMARY KEY,
    EmployeeID INT,
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(20),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create a table for LeaveRecords
CREATE TABLE LeaveRecords (
    LeaveID INT PRIMARY KEY,
    EmployeeID INT,
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(20),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create a table for Manager
CREATE TABLE Manager (
    ManagerID INT PRIMARY KEY,
    EmployeeID INT,
    Email VARCHAR(100),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Add an 'email' column to the 'Employee' table
ALTER TABLE Employee ADD email VARCHAR(50);

-- Insert data into the 'Employee' table
INSERT INTO Employee (EmployeeID, FirstName, LastName, Salary, email)
VALUES
    (1, 'Rajesh', 'Kumar', 60000.00, 'rajeshkumar@email.com'),
    (2, 'Priya', 'Sharma', 55000.00, 'priyasharma@email.com'),
    (3, 'Amit', 'Singh', 62000.00, 'amitsingh@email.com'),
    (4, 'Sneha', 'Patel', 58000.00, 'snehapatel@email.com'),
    (5, 'Arun', 'Gupta', 65000.00, 'arungupta@email.com'),
    (6, 'Neha', 'Shah', 54000.00, 'nehashah@email.com'),
    (7, 'Vikas', 'Verma', 63000.00, 'vikasverma@email.com'),
    (8, 'Meera', 'Yadav', 59000.00, 'meerayadav@email.com'),
    (9, 'Anil', 'Mishra', 61000.00, 'anilmishra@email.com'),
    (10, 'Pooja', 'Jain', 57000.00, 'poojajain@email.com');

-- Insert data into the 'Department' table
INSERT INTO Department (DepartmentID, EmployeeID, DepartmentName, Description)
VALUES
    (1, 1, 'HR', 'Human Resources'),
    (2, 2, 'IT', 'Information Technology'),
    (3, 3, 'Finance', 'Financial Management'),
    (4, 4, 'Marketing', 'Marketing Department'),
    (5, 5, 'Sales', 'Sales Department'),
    (6, 6, 'IT', 'Information Technology'),
    (7, 7, 'HR', 'Human Resources'),
    (8, 8, 'Finance', 'Financial Management'),
    (9, 9, 'Marketing', 'Marketing Department'),
    (10, 10, 'Sales', 'Sales Department');

-- Insert data into the 'LeaveRecords' table
INSERT INTO LeaveRecords (LeaveID, EmployeeID, StartDate, EndDate, Status)
VALUES
    (1, 1, '2023-07-01', '2023-07-05', 'Approved'),
    (2, 2, '2023-07-01', '2023-07-05', 'Approved'),
    (3, 3, '2023-07-01', '2023-07-05', 'Approved'),
    (4, 4, '2023-07-01', '2023-07-05', 'Approved'),
    (5, 5, '2023-07-01', '2023-07-05', 'Approved');



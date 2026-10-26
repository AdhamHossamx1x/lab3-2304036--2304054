-- Problem 1: COMPANY database (DML)
-- Run:  mysql -u root -p < problem1_DML.sql
USE company;

-- Step 1: employees WITHOUT a department yet (Dno = NULL is allowed)
INSERT INTO EMPLOYEE (ssn, fname, lname, bdate, address, gender, salary, Dno) VALUES
('2304036', 'Adham',    'Hossam',  '2004-11-18', 'Alexandria', 'M', 8000.00, NULL),
('2304054', 'Alaa',     'Abdullah','2005-05-05', 'Cairo',      'F', 7500.00, NULL),
('2304066', 'Abdullah', 'Elsayed', '2003-11-05', 'Giza',       'M', 6500.00, NULL),
('2304077', 'Basem',    'Hesham',  '2003-01-30', 'Alexandria', 'M', 5000.00, NULL);

-- Step 2: departments (managers are employees that already exist)
INSERT INTO DEPARTMENT (Dnumber, Dname, mgr_ssn, mgr_start_date) VALUES
(1, 'Research',  '2304036', '2024-01-01'),
(2, 'Software',  '2304054', '2024-06-01'),
(3, 'Marketing', '2304066', '2024-09-01');

-- Step 3: now give each employee a department
UPDATE EMPLOYEE SET Dno = 1 WHERE ssn = '2304036';
UPDATE EMPLOYEE SET Dno = 2 WHERE ssn = '2304054';
UPDATE EMPLOYEE SET Dno = 3 WHERE ssn = '2304066';
UPDATE EMPLOYEE SET Dno = 2 WHERE ssn = '2304077';

-- Step 4: projects
INSERT INTO PROJECT (Pnumber, Pname, Plocation, Dno) VALUES
(10, 'ProductX',   'Alexandria', 1),
(20, 'WebPortal',  'Cairo',      2),
(30, 'AdCampaign', 'Giza',       3);
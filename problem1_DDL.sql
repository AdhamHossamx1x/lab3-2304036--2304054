-- Problem 1: COMPANY database (DDL)
-- Run:  mysql -u root -p < problem1_DDL.sql

DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

-- EMPLOYEE first (its foreign key to DEPARTMENT is added later with ALTER TABLE,
-- because DEPARTMENT does not exist yet and DEPARTMENT also points back to EMPLOYEE)
CREATE TABLE EMPLOYEE (
    ssn      CHAR(9)        NOT NULL,
    fname    VARCHAR(30)    NOT NULL,
    lname    VARCHAR(30)    NOT NULL,
    bdate    DATE,
    address  VARCHAR(100),
    gender   CHAR(1),
    salary   DECIMAL(10,2),
    Dno      INT,
    PRIMARY KEY (ssn)
);

CREATE TABLE DEPARTMENT (
    Dnumber        INT          NOT NULL,
    Dname          VARCHAR(50)  NOT NULL,
    mgr_ssn        CHAR(9),
    mgr_start_date DATE,
    PRIMARY KEY (Dnumber),
    FOREIGN KEY (mgr_ssn) REFERENCES EMPLOYEE(ssn)
);

CREATE TABLE PROJECT (
    Pnumber   INT          NOT NULL,
    Pname     VARCHAR(50)  NOT NULL,
    Plocation VARCHAR(50),
    Dno       INT,
    PRIMARY KEY (Pnumber),
    FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber)
);

-- Now DEPARTMENT exists, so EMPLOYEE.Dno can point to it
ALTER TABLE EMPLOYEE ADD FOREIGN KEY (Dno)
    REFERENCES DEPARTMENT(Dnumber);

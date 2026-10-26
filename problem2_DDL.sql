-- Problem 2: library database (DDL)
-- Run:  mysql -u root -p < problem2_DDL.sql

DROP DATABASE IF EXISTS library;
CREATE DATABASE library;
USE library;

CREATE TABLE AUTHOR (
    author_id INT          NOT NULL AUTO_INCREMENT,
    name      VARCHAR(100) NOT NULL,
    country   VARCHAR(50),
    photo     VARCHAR(255),              -- bonus: photo file name
    PRIMARY KEY (author_id)
);

CREATE TABLE BOOK (
    book_id   INT           NOT NULL AUTO_INCREMENT,
    title     VARCHAR(150)  NOT NULL,
    price     DECIMAL(10,2),
    author_id INT           NOT NULL,
    cover     VARCHAR(255),              -- bonus: cover file name
    PRIMARY KEY (book_id),
    FOREIGN KEY (author_id) REFERENCES AUTHOR(author_id)
        ON DELETE CASCADE                -- deleting an author deletes his/her books
);

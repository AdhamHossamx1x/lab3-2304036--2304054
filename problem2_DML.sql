-- Problem 2: library database (seed data)
-- Run:  mysql -u root -p < problem2_DML.sql
USE library;

INSERT INTO AUTHOR (author_id, name, country) VALUES
(1, 'Naguib Mahfouz',  'Egypt'),
(2, 'Agatha Christie', 'United Kingdom'),
(3, 'Gabriel Garcia Marquez', 'Colombia'),
(4, 'Taha Hussein',    'Egypt');

INSERT INTO BOOK (book_id, title, price, author_id) VALUES
(1, 'Palace Walk',                    15.50, 1),
(2, 'Midaq Alley',                    12.00, 1),
(3, 'Murder on the Orient Express',   18.75, 2),
(4, 'And Then There Were None',       16.00, 2),
(5, 'One Hundred Years of Solitude',  20.00, 3),
(6, 'The Days',                       10.25, 4),
(7, 'Love in the Time of Cholera',    17.50, 3);

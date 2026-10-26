# Lab 3: Foreign Keys and Simple SQL

Introduction to Database Systems, Alexandria National University, Fall 2026.

## Files

| File | What it is |
|------|-----------|
| `problem1_DDL.sql` | Creates the `company` database and its 3 tables with primary and foreign keys |
| `problem1_DML.sql` | Inserts 4 employees, 3 departments, 3 projects |
| `problem1_Answers.txt` | SQL and output/error for Q1.1, Q1.2, Q1.3 |
| `problem2_DDL.sql` | Creates the `library` database (`AUTHOR`, `BOOK`, with `ON DELETE CASCADE`) |
| `problem2_DML.sql` | Seed data: 4 authors, 7 books |
| `website/` | The library website (Flask + MySQL) |

## Requirements

- MySQL Server running on your computer (user `root`)
- Python 3.9 or newer

## How to run: Problem 1

Open a terminal in this folder, then:

```
mysql -u root -p < problem1_DDL.sql
mysql -u root -p < problem1_DML.sql
mysql -u root -p company
```

The last command opens the MySQL client. Type the queries from `problem1_Answers.txt` there.

## How to run: Problem 2 (database)

```
mysql -u root -p < problem2_DDL.sql
mysql -u root -p < problem2_DML.sql
```

## How to run: the website

1. Do the Problem 2 database steps above first.
2. Open `website/app.py` and write your MySQL password in `DB_PASSWORD`
   (or set the environment variable `DB_PASSWORD`).
3. In a terminal:

```
cd website
pip install -r requirements.txt
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

## Website pages

- **F2.1** Home page shows the books table (with `author_id`) and the authors table.
- **F2.2** "Add book" and "Add author" buttons.
- **F2.3** "Edit" button in every row.
- **F2.4** "Remove" a book.
- **F2.5** "Remove" an author. This also deletes the author's books (`ON DELETE CASCADE`).
- **Bonus** A cover image for each book and a photo for each author (uploaded files are saved in `website/static/uploads/`).

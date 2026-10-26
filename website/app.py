"""Library website - Lab 3 (Flask + MySQL).

Run:  python app.py      then open http://127.0.0.1:5000
Change DB_PASSWORD below to your MySQL root password.
"""
import os
import uuid

import pymysql
from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

# ---------- settings (edit these) ----------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")   # <-- put your MySQL password here
DB_NAME = "library"
# -------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
ALLOWED = {"png", "jpg", "jpeg", "gif", "webp"}
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
app.secret_key = "lab3-secret"


def db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
                           database=DB_NAME,
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=True)


def run(sql, params=(), one=False, fetch=True):
    """Run one SQL statement and return rows (SELECT) or nothing."""
    conn = db()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            if not fetch:
                return None
            return cur.fetchone() if one else cur.fetchall()
    finally:
        conn.close()


def save_image(field):
    """Save the uploaded image (bonus) and return its new file name, or None."""
    f = request.files.get(field)
    if not f or f.filename == "":
        return None
    ext = f.filename.rsplit(".", 1)[-1].lower()
    if ext not in ALLOWED:
        flash("Image must be png / jpg / jpeg / gif / webp.")
        return None
    name = uuid.uuid4().hex + "_" + secure_filename(f.filename)
    f.save(os.path.join(UPLOAD_DIR, name))
    return name


# ---------- F2.1  show both tables ----------
@app.route("/")
def index():
    books = run("SELECT * FROM BOOK ORDER BY book_id")
    authors = run("SELECT * FROM AUTHOR ORDER BY author_id")
    return render_template("index.html", books=books, authors=authors)


# ---------- F2.2  add ----------
@app.route("/author/add", methods=["GET", "POST"])
def add_author():
    if request.method == "POST":
        run("INSERT INTO AUTHOR (name, country, photo) VALUES (%s, %s, %s)",
            (request.form["name"], request.form["country"], save_image("photo")),
            fetch=False)
        flash("Author added.")
        return redirect(url_for("index"))
    return render_template("author_form.html", author=None)


@app.route("/book/add", methods=["GET", "POST"])
def add_book():
    authors = run("SELECT author_id, name FROM AUTHOR ORDER BY name")
    if request.method == "POST":
        try:
            run("INSERT INTO BOOK (title, price, author_id, cover) "
                "VALUES (%s, %s, %s, %s)",
                (request.form["title"], request.form["price"],
                 request.form["author_id"], save_image("cover")), fetch=False)
            flash("Book added.")
            return redirect(url_for("index"))
        except pymysql.err.IntegrityError:
            flash("That author_id does not exist (foreign key error).")
    return render_template("book_form.html", book=None, authors=authors)


# ---------- F2.3  edit ----------
@app.route("/author/<int:author_id>/edit", methods=["GET", "POST"])
def edit_author(author_id):
    author = run("SELECT * FROM AUTHOR WHERE author_id = %s", (author_id,), one=True)
    if not author:
        return redirect(url_for("index"))
    if request.method == "POST":
        photo = save_image("photo") or author["photo"]
        run("UPDATE AUTHOR SET name = %s, country = %s, photo = %s "
            "WHERE author_id = %s",
            (request.form["name"], request.form["country"], photo, author_id),
            fetch=False)
        flash("Author updated.")
        return redirect(url_for("index"))
    return render_template("author_form.html", author=author)


@app.route("/book/<int:book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):
    book = run("SELECT * FROM BOOK WHERE book_id = %s", (book_id,), one=True)
    if not book:
        return redirect(url_for("index"))
    authors = run("SELECT author_id, name FROM AUTHOR ORDER BY name")
    if request.method == "POST":
        cover = save_image("cover") or book["cover"]
        try:
            run("UPDATE BOOK SET title = %s, price = %s, author_id = %s, cover = %s "
                "WHERE book_id = %s",
                (request.form["title"], request.form["price"],
                 request.form["author_id"], cover, book_id), fetch=False)
            flash("Book updated.")
            return redirect(url_for("index"))
        except pymysql.err.IntegrityError:
            flash("That author_id does not exist (foreign key error).")
    return render_template("book_form.html", book=book, authors=authors)


# ---------- F2.4 / F2.5  remove ----------
@app.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    run("DELETE FROM BOOK WHERE book_id = %s", (book_id,), fetch=False)
    flash("Book removed.")
    return redirect(url_for("index"))


@app.route("/author/<int:author_id>/delete", methods=["POST"])
def delete_author(author_id):
    # ON DELETE CASCADE in the database removes this author's books too
    run("DELETE FROM AUTHOR WHERE author_id = %s", (author_id,), fetch=False)
    flash("Author and all of his/her books removed.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

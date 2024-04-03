# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.


from flask import Flask, render_template, request
from models_02 import db, Book, Author
from faker import Faker
from random import randint

fake = Faker()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    for _ in range(1, 6):
        new_author = Author(first_name=fake.last_name(),
                            last_name=fake.last_name())
        db.session.add(new_author)
    db.session.commit()

    for i in range(25):
        new_book = Book(name=f'Книга_{i + 1}',
                        year_public=randint(1984, 2024),
                        quantity_copy=randint(1, 10),
                        id_author=randint(1, 5))
        db.session.add(new_book)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def get_books():
    """
    Сделал запрос на поиск книг по году издания на странице, если нет с таким годом - выводит сообщение
    Если в форму не водить год отобразит все книги
    :return:
    """
    books = Book.query.all()
    context = {'books': books}
    if request.method == 'POST':
        if year_public := request.form.get('year_public'):
            books = Book.query.filter(Book.year_public == year_public).all()
            context = {'books': books,
                       'year_public': year_public}
            return render_template('books.html', **context)
    return render_template('books.html', **context)


@app.route('/xx/', methods=['GET', 'POST'])
def get_xx():
    """
    Сделал запрос на поиск книг на странице по году издания, если нет с таким годом - выводит сообщение
    Если в форму не водить год отобразит все книги
    :return:
    """
    books = Book.query.filter(Book.year_public < 2000).all()
    context = {'books': books}
    if request.method == 'POST':
        if year_public := request.form.get('year_public'):
            books_century = []
            for book in books:
                if book.year_public == int(year_public):
                    books_century.append(book)
            books = books_century
            context = {'books': books,
                       'year_public': year_public}
            return render_template('books.html', **context)
    return render_template('books.html', **context)


@app.route('/xxi/', methods=['GET', 'POST'])
def get_xxi():
    """
    Сделал запрос на поиск книг по году издания, если нет с таким годом - выводит сообщение
    Если в форму не водить год отобразит все книги
    :return:
    """
    books = Book.query.filter(Book.year_public > 2000).all()
    context = {'books': books}
    if request.method == 'POST':
        if year_public := request.form.get('year_public'):
            books_century = []
            for book in books:
                if book.year_public == int(year_public):
                    books_century.append(book)
            books = books_century
            context = {'books': books,
                       'year_public': year_public}
            return render_template('books.html', **context)
    return render_template('books.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year_public = db.Column(db.Integer, nullable=False)
    quantity_copy = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'{self.name}. Автор книги : {self.author}. Год издания: {self.year_public}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    book = db.relationship('Book', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'



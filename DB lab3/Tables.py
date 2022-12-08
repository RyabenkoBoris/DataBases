from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    book_numbers = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship("Author", backref=backref('author'))


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    amount = Column(Integer)
    publication_date = Column(Date)
    series_id = Column(Integer, ForeignKey('series.id'))
    series = relationship("Series", backref=backref('series'))


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    book = relationship("Book", secondary='book_genre')


class BookGenre(Base):
    __tablename__ = 'book_genre'
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genre.id'), primary_key=True)


from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base
from guternberg_api import configuration as conf

Base = declarative_base()
engine = create_engine(conf.DB_CONNECTION_URL, echo=True)

class Book(Base):
    __tablename__ = 'books_book'

    id = Column(Integer, primary_key=True, nullable=False)
    download_count = Column(Integer, default=None)
    gutenberg_id = Column(Integer, nullable=False)
    media_type = Column(String(16), nullable=False)
    title = Column(Text, default=None)

class Format(Base):
    __tablename__ = 'books_format'

    id = Column(Integer, primary_key=True, nullable=False)
    mime_type = Column(String(32), nullable=False)
    url = Column(Text, nullable=False)
    book_id = Column(Integer, nullable=False)

class Author(Base):
    __tablename__ = 'books_author'

    id = Column(Integer, primary_key=True, nullable=False)
    birth_year = Column(Integer, default=None)
    death_year = Column(Integer, default=None)
    name = Column(String(128), nullable=False)

class BookAndAuthorMapper(Base):
    __tablename__ = 'books_book_authors'

    id = Column(Integer, primary_key=True, nullable=False)
    book_id = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)

class Bookshelf(Base):
    __tablename__ = 'books_bookshelf'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)

class BookAndBookshelfMapper(Base):
    __tablename__ = 'books_book_bookshelves'

    id = Column(Integer, primary_key=True, nullable=False)
    book_id = Column(Integer, nullable=False)
    bookshelf_id = Column(Integer, nullable=False)

class Language(Base):
    __tablename__ = 'books_language'

    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String(4), nullable=False)

class BookAndLanguageMapper(Base):
    __tablename__ = 'books_book_languages'

    id = Column(Integer, primary_key=True, nullable=False)
    book_id = Column(Integer, nullable=False)
    language_id = Column(Integer, nullable=False)

class Subject(Base):
    __tablename__ = 'books_subject'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)

class BookAndSubjectMapper(Base):
    __tablename__ = 'books_book_subjects'

    id = Column(Integer, primary_key=True, nullable=False)
    book_id = Column(Integer, nullable=False)
    subject_id = Column(Integer, nullable=False)
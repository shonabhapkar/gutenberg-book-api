from guternberg_api.HbmDal import *
from sqlalchemy.orm import sessionmaker
from guternberg_api.logger import logger
from guternberg_api import configuration as config


class DBHelper:

    def extract_book_id_by_gutenberg_id(self, ptup_gutenberg_id):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()
            llst_result = lobj_session.query(
                        Book.id, Book.download_count
                    ).filter(
                        Book.gutenberg_id.in_(ptup_gutenberg_id),
                    ).order_by(Book.download_count).all()

            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_gutenberg_id': ptup_gutenberg_id})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_language(self, ptup_language):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            llst_result = lobj_session.query(
                        Book.id, Book.download_count
                    ).filter(
                        Language.code.in_(ptup_language),
                        Book.id == BookAndLanguageMapper.book_id,
                        Language.id == BookAndLanguageMapper.language_id,
                    ).order_by(Book.download_count).limit(config.BOOKS_BATCH_COUNT).all()

            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_language': ptup_language})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_mime_type(self, ptup_mime_type):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            llst_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Format.mime_type.in_(ptup_mime_type),
                Book.id == Format.book_id,
            ).order_by(Book.download_count).limit(config.BOOKS_BATCH_COUNT).all()

            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_mime_type': ptup_mime_type})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_author(self, ptup_author):
        llst_result = []
        lobj_session = None
        try:
            lstr_regex = "|".join(ptup_author)
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            llst_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Book.id == BookAndAuthorMapper.book_id,
                Author.id == BookAndAuthorMapper.author_id,
            ) .filter(
                Author.name.op('regexp')(lstr_regex)
            ).order_by(Book.download_count).limit(config.BOOKS_BATCH_COUNT).all()

            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_author': ptup_author})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_title(self, ptup_title):
        llst_result = []
        lobj_session = None
        try:
            lstr_regex = "|".join(ptup_title)
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            llst_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Book.title.op('regexp')(lstr_regex)
            ).order_by(Book.download_count).limit(config.BOOKS_BATCH_COUNT).all()

            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_title': ptup_title})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_topic(self, ptup_topic):
        llst_result = []
        lobj_session = None
        try:
            lstr_regex = "|".join(ptup_topic)
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            lstr_bookshelf_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                 Bookshelf.name.op('regexp')(lstr_regex),
                 Book.id == BookAndBookshelfMapper.book_id,
                 Bookshelf.id == BookAndBookshelfMapper.bookshelf_id,
            )

            lstr_book_subject_result = lobj_session.query(
                        Book.id, Book.download_count
                ).filter(
                        Subject.name.op('regexp')(lstr_regex),
                        Book.id == BookAndSubjectMapper.book_id,
                        Subject.id == BookAndSubjectMapper.subject_id,
                )

            llst_result = lstr_bookshelf_result.union(
                        lstr_book_subject_result
                ).order_by(Book.download_count).limit(config.BOOKS_BATCH_COUNT).all()

            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_topic': ptup_topic})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_title_using_book_id(self, pint_bookid):
        lstr_title = ""
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            lstr_title = lobj_session.query(
                Book.title
            ).filter(
                Book.id == pint_bookid,
            ).one()[0]


        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return lstr_title


    def extract_author_info_using_book_id(self, pint_bookid):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            llst_author_result = lobj_session.query(
                Author
            ).filter(
                Book.id == BookAndAuthorMapper.book_id,
                Author.id == BookAndAuthorMapper.author_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            for lobj_row in llst_author_result:
                ldict_row_result = {}
                ldict_row_result["name"] = lobj_row.name
                ldict_row_result["birth_year"] = lobj_row.birth_year
                ldict_row_result["death_year"] = lobj_row.death_year
                llst_result.append(ldict_row_result)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_subject_using_book_id(self, pint_bookid):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()
            llst_subjects_result = lobj_session.query(
                Subject
            ).filter(
                Book.id == BookAndSubjectMapper.book_id,
                Subject.id == BookAndSubjectMapper.subject_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            for lobj_row in llst_subjects_result:
                llst_result.append(lobj_row.name)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_language_using_book_id(self, pint_bookid):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()
            llst_language_result = lobj_session.query(
                Language
            ).filter(
                Book.id == BookAndLanguageMapper.book_id,
                Language.id == BookAndLanguageMapper.language_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            for lobj_row in llst_language_result:
                llst_result.append(lobj_row.code)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_bookshelf_using_book_id(self, pint_bookid):
        llst_result = []
        lobj_session = None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()
            llst_bookshelf_result = lobj_session.query(
                Bookshelf
            ).filter(
                Book.id == BookAndBookshelfMapper.book_id,
                Bookshelf.id == BookAndBookshelfMapper.bookshelf_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            for lobj_row in llst_bookshelf_result:
                llst_result.append(lobj_row.name)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_download_link_using_book_id(self, pint_bookid):
        llst_result = []
        lobj_session= None
        try:
            Session = sessionmaker(bind=engine)
            lobj_session = Session()
            llst_format_result = lobj_session.query(
                Format
            ).filter(
                Book.id == Format.book_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            for lobj_row in llst_format_result:
                ldict_row_result = {}
                ldict_row_result["mime_type"] = lobj_row.mime_type
                ldict_row_result["url"] = lobj_row.url
                llst_result.append(ldict_row_result)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result

    def get_books_info_by_book_id(self, plst_book_id):
        llst_books = []
        try:
            lobj_db_helper = DBHelper()

            for lint_book_id in plst_book_id:
                ldict_book_info = {}

                ldict_book_info["title"] = \
                    lobj_db_helper.extract_title_using_book_id(lint_book_id)
                ldict_book_info["author_info"] = \
                    lobj_db_helper.extract_author_info_using_book_id(lint_book_id)
                ldict_book_info["subject"] = \
                    lobj_db_helper.extract_subject_using_book_id(lint_book_id)
                ldict_book_info["language"] = \
                    lobj_db_helper.extract_language_using_book_id(lint_book_id)
                ldict_book_info["bookself"] = \
                    lobj_db_helper.extract_bookshelf_using_book_id(lint_book_id)
                ldict_book_info["download_link"] = \
                    lobj_db_helper.extract_download_link_using_book_id(lint_book_id)

                llst_books.append(ldict_book_info)

        except Exception as e:
            logger.error(str(e), extra={'plst_book_id': plst_book_id})
            raise
        finally:
            return llst_books



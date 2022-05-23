from guternberg_api.HbmDal import *
from sqlalchemy.orm import sessionmaker
from guternberg_api.logger import logger


class DBHelper:
    """
    This class uses HbmDal Class and performs db operations
    """

    def extract_book_id_by_gutenberg_id(self, ptup_gutenberg_id):
        """
        This method takes gutenberg_id tuple as input and extract book_ids (sorted by download counts) from db
        by gutenberg_id criteria

        :param ptup_gutenberg_id: It is tuple of gutenberg_ids
        :return llst_result: It is a list of book_id sorted by download counts
        """

        lobj_session = None

        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract tuple of Book_id and download_count (sorted by download counts) from db by gutenberg_id criteria
            llst_result = lobj_session.query(
                        Book.id, Book.download_count
                    ).filter(
                        Book.gutenberg_id.in_(ptup_gutenberg_id),
                    ).order_by(Book.download_count).all()

            # get book_id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_gutenberg_id': ptup_gutenberg_id})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_language(self, ptup_language):
        """
        This method takes language tuple as input and extract book_id (sorted by download counts) from db
        by language criteria. Language criteria is case sensitive full match

        :param ptup_language: It is tuple of language
        :return llst_result: It is a list of book_id sorted by download counts
        """
        llst_result = []
        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract tuple of Book_id and download_count (sorted by download counts) from db by language criteria
            # Language criteria is case sensitive full match
            llst_result = lobj_session.query(
                        Book.id, Book.download_count
                    ).filter(
                        Language.code.in_(ptup_language),
                        Book.id == BookAndLanguageMapper.book_id,
                        Language.id == BookAndLanguageMapper.language_id,
                    ).order_by(Book.download_count).all()

            # get book_id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_language': ptup_language})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_mime_type(self, ptup_mime_type):
        """
        This method takes mime_type tuple as input and extract book_ids (sorted by download counts) from db
        by mime_type criteria. mime_type criteria is case sensitive full match

        :param ptup_mime_type: It is tuple of mime_type
        :return llst_result: It is a list of book_id sorted by download counts
        """

        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract tuple of Book_id and download_count (sorted by download counts) from db by mime_type criteria
            # mime_type criteria is case sensitive full match
            llst_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Format.mime_type.in_(ptup_mime_type),
                Book.id == Format.book_id,
            ).order_by(Book.download_count).all()

            # get book_id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_mime_type': ptup_mime_type})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_topic(self, ptup_topic):
        """
        This method takes mime_type tuple as input and extract book_ids (sorted by download counts) from db
        by topic criteria. Topic is filter on either ‘subject’ or ‘bookshelf’ or both.
        topic criteria is case-insensitive partial match

        :param ptup_topic: It is tuple of topic
        :return llst_result: It is a list of book_id sorted by download counts
        """

        lobj_session = None
        try:
            # create topic regex for case-insensitive partial match
            lstr_regex = "|".join(ptup_topic)

            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # create qurey to extract list of Book objets from db by bookshelf criteria
            # bookshelf criteria is case-insensitive partial match
            lstr_bookshelf_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Bookshelf.name.op('regexp')(lstr_regex),
                Book.id == BookAndBookshelfMapper.book_id,
                Bookshelf.id == BookAndBookshelfMapper.bookshelf_id,
            )

            # create qurey to extract list of Book objets from db by subject criteria
            # subject criteria is case-insensitive partial match
            lstr_book_subject_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Subject.name.op('regexp')(lstr_regex),
                Book.id == BookAndSubjectMapper.book_id,
                Subject.id == BookAndSubjectMapper.subject_id,
            )

            # extract tuple of Book_id and download_count (sorted by download counts) from db
            # by topic criteria (taking union of subject and bookshelf queries)
            llst_result = lstr_bookshelf_result.union(
                lstr_book_subject_result
            ).order_by(Book.download_count).all()

            # get book_id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_topic': ptup_topic})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_author(self, ptup_author):
        """
        This method takes mime_type tuple as input and extract book_ids (sorted by download counts) from db
        by author criteria. mime_type criteria is case-insensitive partial match

        :param ptup_author: It is tuple of author
        :return llst_result: It is a list of book_id sorted by download counts
        """

        lobj_session = None
        try:
            # create author regex for case-insensitive partial match
            lstr_regex = "|".join(ptup_author)

            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract tuple of Book_id and download_count (sorted by download counts) from db by author criteria
            # author criteria is case-insensitive partial match
            llst_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Book.id == BookAndAuthorMapper.book_id,
                Author.id == BookAndAuthorMapper.author_id,
            ) .filter(
                Author.name.op('regexp')(lstr_regex)
            ).order_by(Book.download_count).all()

            # get book_id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_author': ptup_author})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_book_id_by_title(self, ptup_title):
        """
        This method takes title tuple as input and extract book_ids (sorted by download counts) from db
        by author criteria. mime_type criteria is case-insensitive partial match

        :param ptup_author: It is tuple of author
        :return llst_result: It is a list of book_id sorted by download counts
        """
        lobj_session = None
        try:
            # create title regex for case-insensitive partial match
            lstr_regex = "|".join(ptup_title)

            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract tuple of Book_id and download_count (sorted by download counts) from db by title criteria
            # title criteria is case-insensitive partial match
            llst_result = lobj_session.query(
                Book.id, Book.download_count
            ).filter(
                Book.title.op('regexp')(lstr_regex)
            ).order_by(Book.download_count).all()

            # get book_id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_title': ptup_title})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_title_using_book_id(self, pint_bookid):
        """
        This method takes book_id as input and extract title from db

        :param pint_bookid: It is book id
        :return lstr_title: It is title
        """
        lstr_title = ""
        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract tile from db by book id criteria
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
        """
        This method takes book_id as input and extract author_info from db

        :param pint_bookid: It is book id
        :return llst_result: It is list of author
        """

        llst_result = []
        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract list of Author objects from db by book id criteria
            llst_author_result = lobj_session.query(
                Author
            ).filter(
                Book.id == BookAndAuthorMapper.book_id,
                Author.id == BookAndAuthorMapper.author_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            # create list of author info
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


    def extract_language_using_book_id(self, pint_bookid):
        """
        This method takes book_id as input and extract languages from db

        :param pint_bookid: It is book id
        :return llst_result: It is list of language
        """

        llst_result = []
        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract list of Language objects from db by book id criteria
            llst_language_result = lobj_session.query(
                Language
            ).filter(
                Book.id == BookAndLanguageMapper.book_id,
                Language.id == BookAndLanguageMapper.language_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            # create list of subject
            for lobj_row in llst_language_result:
                llst_result.append(lobj_row.code)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_subject_using_book_id(self, pint_bookid):
        """
        This method takes book_id as input and extract subject from db

        :param pint_bookid: It is book id
        :return llst_result: It is list of subject
        """

        llst_result = []
        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract list of Subject objects from db by book id criteria
            llst_subjects_result = lobj_session.query(
                Subject
            ).filter(
                Book.id == BookAndSubjectMapper.book_id,
                Subject.id == BookAndSubjectMapper.subject_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            # create list of subject
            for lobj_row in llst_subjects_result:
                llst_result.append(lobj_row.name)

        except Exception as e:
            logger.error(str(e), extra={'pint_bookid': pint_bookid},
                         exc_info=True)
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result


    def extract_bookshelf_using_book_id(self, pint_bookid):
        """
        This method takes book_id as input and extract bookshelf name from db

        :param pint_bookid: It is book id
        :return llst_result: It is list of bookshelf name
        """

        llst_result = []
        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract list of Bookshelf objects from db by book id criteria
            llst_bookshelf_result = lobj_session.query(
                Bookshelf
            ).filter(
                Book.id == BookAndBookshelfMapper.book_id,
                Bookshelf.id == BookAndBookshelfMapper.bookshelf_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            # create list of bookshelf
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
        """
        This method takes book_id as input and extract download_link info from db

        :param pint_bookid: It is book id
        :return llst_result: It is list of download_link info
        """

        llst_result = []
        lobj_session= None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            # extract list of Format objects from db by book id criteria
            llst_format_result = lobj_session.query(
                Format
            ).filter(
                Book.id == Format.book_id,
            ).filter(
                Book.id == pint_bookid,
            ).all()

            # create list of download link info
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


    def sort_book_id_by_download_count(self, ptup_book_id):
        """
        This method takes book_id tuple as input and sort book_id by download_count

        :param ptup_book_id: It is book id tuple
        :return llst_result: It is list of Books id sorted by download count
        """

        lobj_session = None
        try:
            # create session
            Session = sessionmaker(bind=engine)
            lobj_session = Session()

            #  sort book_id by download_count
            llst_result = lobj_session.query(
                        Book.id, Book.download_count
                    ).filter(
                        Book.id.in_(ptup_book_id),
                    ).order_by(Book.download_count).all()

            # create list of book id
            llst_result = [lint_id for lint_id, _ in llst_result]

        except Exception as e:
            logger.error(str(e), extra={'ptup_book_id': ptup_book_id})
            raise
        finally:
            if lobj_session:
                lobj_session.close()
        return llst_result



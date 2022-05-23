from guternberg_api.DBHelper import DBHelper
from guternberg_api.logger import logger


class APIHelper:
    """
    This class uses DBHelper Class and performs db operations
    """


    def extract_book_id_by_multiple_criteria(self, ptup_g_id, ptup_lang, ptup_mime_type,
                                             ptup_topic, ptup_author, ptup_title):
        """
        This method extract book_ids (sorted by download counts) from db
        by multiple provided criteria.

        :param ptup_g_id: It is tuple of gutenberg_id
        :param ptup_lang: It is tuple of lang
        :param ptup_mime_type: It is tuple of mime_type
        :param ptup_topic: It is tuple of topic
        :param ptup_author: It is tuple of author
        :param ptup_title: It is tuple of title
        :return llst_result: It is a list of book_id sorted by download counts
        """
        llst_book_id = []
        try:
            lobj_db_helper = DBHelper()

            if ptup_g_id:
                # extract list of book ids by gutenberg_id criteria
                llst_book_id.append(lobj_db_helper.extract_book_id_by_gutenberg_id(ptup_g_id))
            if ptup_lang:
                # extract list of book ids by language criteria
                llst_book_id.append(lobj_db_helper.extract_book_id_by_language(ptup_lang))
            if ptup_mime_type:
                # extract list of book ids by mime_type criteria
                llst_book_id.append(lobj_db_helper.extract_book_id_by_mime_type(ptup_mime_type))
            if ptup_topic:
                # extract list of book ids by topic criteria
                llst_book_id.append(lobj_db_helper.extract_book_id_by_topic(ptup_topic))
            if ptup_author:
                # extract list of book ids by author criteria
                llst_book_id.append(lobj_db_helper.extract_book_id_by_author(ptup_author))
            if ptup_title:
                # extract list of book ids by title criteria
                llst_book_id.append(lobj_db_helper.extract_book_id_by_title(ptup_title))

            # find the common book ids returned by all criteria
            ltup_book_id = tuple(set.intersection(*map(set, llst_book_id)))

            # sort the book ids by download count
            llst_book_id = lobj_db_helper.sort_book_id_by_download_count(ltup_book_id)

        except Exception as e:
            logger.error(str(e), extra={'ptup_title': ptup_title})
            raise

        return llst_book_id


    def get_books_info_by_book_id(self, plst_book_id):
        """
        This method takes book_id as input and extract Books info from db

        :param pint_bookid: It is book id
        :return llst_books: It is list of Books info
        """

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
from guternberg_api.DBHelper import DBHelper
from flask import Flask, request
from flask_restful import Resource, Api
from guternberg_api.ResponseGenerator import ResponseGenerator
from guternberg_api.logger import logger
from guternberg_api import configuration as config

app = Flask(__name__)
api = Api(app)


class BookInfoExtractorByGutenbergId(Resource):
    def get(self):

        try:
            try:
                lstr_g_id = request.args.get('g_id')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response(
                    "'g_id' is missing in request params")

            # separate the input by ","
            ltup_g_id = tuple(lstr_g_id.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = lobj_db_helper.extract_book_id_by_gutenberg_id(ltup_g_id)
            lint_total_no_of_books_found = len(llst_book_id)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(
                llst_book_id[:config.BOOKS_BATCH_COUNT])

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(lint_total_no_of_books_found,
                                                                       llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByLanguage(Resource):
    def get(self):

        try:
            try:
                lstr_language = request.args.get('lang')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response(
                    "'language' is missing in request params")

            # separate the input by ","
            ltup_lang = tuple(lstr_language.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = DBHelper().extract_book_id_by_language(ltup_lang)
            lint_total_no_of_books_found = len(llst_book_id)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(
                llst_book_id[:config.BOOKS_BATCH_COUNT])

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(lint_total_no_of_books_found,
                                                                       llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByMimeType(Resource):
    def get(self):

        try:
            try:
                lstr_mime_type = request.args.get('mime_type')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response(
                    "'mime_type' is missing in request params")

            # separate the input by ","
            ltup_mime_type = tuple(lstr_mime_type.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = DBHelper().extract_book_id_by_mime_type(ltup_mime_type)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(llst_book_id)

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByTopic(Resource):
    def get(self):

        try:
            try:
                lstr_topic = request.args.get('topic')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response(
                    "'topic' is missing in request params")

            # separate the input by ","
            ltup_topic = tuple(lstr_topic.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = DBHelper().extract_book_id_by_topic(ltup_topic)
            lint_total_no_of_books_found = len(llst_book_id)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(
                llst_book_id[:config.BOOKS_BATCH_COUNT])

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(lint_total_no_of_books_found,
                                                                       llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByAuthor(Resource):
    def get(self):

        try:
            try:
                lstr_author = request.args.get('author')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response(
                    "'author' is missing in request params")

            # separate the input by ","
            ltup_author = tuple(lstr_author.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = DBHelper().extract_book_id_by_author(ltup_author)
            lint_total_no_of_books_found = len(llst_book_id)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(
                llst_book_id[:config.BOOKS_BATCH_COUNT])

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(lint_total_no_of_books_found,
                                                                       llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByTitle(Resource):
    def get(self):

        try:
            try:
                lstr_title = request.args.get('title')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response(
                    "'title' is missing in request params")

            # separate the input by ","
            ltup_title = tuple(lstr_title.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = DBHelper().extract_book_id_by_title(ltup_title)
            lint_total_no_of_books_found = len(llst_book_id)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(
                llst_book_id[:config.BOOKS_BATCH_COUNT])

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(lint_total_no_of_books_found,
                                                                       llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


class BookInfoExtractor(Resource):
    def get(self):

        try:
            lstr_g_id = request.args.get('g_id', default='')
            lstr_language = request.args.get('lang', default='')
            lstr_mime_type = request.args.get('mime_type', default='')
            lstr_topic = request.args.get('topic', default='')
            lstr_author = request.args.get('author', default='')
            lstr_title = request.args.get('title', default='')

            if not lstr_g_id and not lstr_language and not lstr_mime_type and \
                    not lstr_topic and not lstr_author and not lstr_title:

                return ResponseGenerator().get_bad_request_response(
                    "request params are missing")

            # separate the input by ","
            ltup_g_id = tuple(lstr_g_id.split(","))
            ltup_lang = tuple(lstr_language.split(","))
            ltup_mime_type = tuple(lstr_mime_type.split(","))
            ltup_topic = tuple(lstr_topic.split(","))
            ltup_author = tuple(lstr_author.split(","))
            ltup_title = tuple(lstr_title.split(","))

            # extract list of book id
            lobj_db_helper = DBHelper()
            llst_book_id = DBHelper().extract_book(ltup_g_id, ltup_lang, ltup_mime_type,
                                                   ltup_topic, ltup_author, ltup_title)
            lint_total_no_of_books_found = len(llst_book_id)

            # extract books info
            llst_books = lobj_db_helper.get_books_info_by_book_id(
                llst_book_id[:config.BOOKS_BATCH_COUNT])

            # create books_info json response
            return ResponseGenerator().create_books_info_json_response(lint_total_no_of_books_found,
                                                                       llst_books)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return ResponseGenerator().get_error_response()


api.add_resource(BookInfoExtractorByGutenbergId, '/guternberg_api/get_books_by_g_id')
api.add_resource(BookInfoExtractorByLanguage, '/guternberg_api/get_books_by_lang')
api.add_resource(BookInfoExtractorByMimeType, '/guternberg_api/get_books_by_mime_type')
api.add_resource(BookInfoExtractorByTopic, '/guternberg_api/get_books_by_topic')
api.add_resource(BookInfoExtractorByAuthor, '/guternberg_api/get_books_by_author')
api.add_resource(BookInfoExtractorByTitle, '/guternberg_api/get_books_by_title')
api.add_resource(BookInfoExtractor, '/guternberg_api/get_books')

if __name__ == '__main__':
    app.run(debug=True)

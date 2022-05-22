from guternberg_api.DBHelper import DBHelper
from flask import Flask, request
from flask_restful import Resource, Api
from guternberg_api.ResponseGenerator import ResponseGenerator, APIResponseCodes, APIResponse

app = Flask(__name__)
api = Api(app)


class BookInfoExtractorByGutenbergId(Resource):
    def get(self):

        try:
            try:
                lstr_g_id = request.args.get('g_id')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_g_id = tuple(lstr_g_id.split(","))
            llst_book_id = DBHelper().extract_book_id_by_gutenberg_id(ltup_g_id)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByLanguage(Resource):
    def get(self):

        try:
            try:
                lstr_language = request.args.get('lang')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_lang = tuple(lstr_language.split(","))
            llst_book_id = DBHelper().extract_book_id_by_language(ltup_lang)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByMimeType(Resource):
    def get(self):

        try:
            try:
                lstr_mime_type = request.args.get('mime_type')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_mime_type = tuple(lstr_mime_type.split(","))
            llst_book_id = DBHelper().extract_book_id_by_mime_type(ltup_mime_type)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByTopic(Resource):
    def get(self):

        try:
            try:
                lstr_topic = request.args.get('topic')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_topic = tuple(lstr_topic.split(","))
            llst_book_id = DBHelper().extract_book_id_by_topic(ltup_topic)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByAuthor(Resource):
    def get(self):

        try:
            try:
                lstr_author = request.args.get('author')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_author = tuple(lstr_author.split(","))
            llst_book_id = DBHelper().extract_book_id_by_author(ltup_author)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_error_response()


class BookInfoExtractorByTitle(Resource):
    def get(self):

        try:
            try:
                lstr_title = request.args.get('title')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_title = tuple(lstr_title.split(","))
            llst_book_id = DBHelper().extract_book_id_by_title(ltup_title)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_error_response()


class BookInfoExtractor(Resource):
    def get(self):

        try:
            try:
                lstr_g_id = request.args.get('g_id', default='')
                lstr_language = request.args.get('lang', default='')
                lstr_mime_type = request.args.get('mime_type', default='')
                lstr_topic = request.args.get('topic', default='')
                lstr_author = request.args.get('author', default='')
                lstr_title = request.args.get('title', default='')

            except Exception as e:
                return ResponseGenerator().get_bad_request_response()

            ltup_g_id = tuple(lstr_g_id.split(","))
            ltup_lang = tuple(lstr_language.split(","))
            ltup_mime_type = tuple(lstr_mime_type.split(","))
            ltup_topic = tuple(lstr_topic.split(","))
            ltup_author = tuple(lstr_author.split(","))
            ltup_title = tuple(lstr_title.split(","))

            llst_book_id = DBHelper().extract_book(ltup_g_id, ltup_lang, ltup_mime_type,
                                                   ltup_topic, ltup_author, ltup_title)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
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

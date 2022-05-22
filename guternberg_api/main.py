from guternberg_api.DBHelper import DBHelper
from flask import Flask, request
from flask_restful import Resource, Api
from guternberg_api.ResponseGenerator import ResponseGenerator, APIResponseCodes

app = Flask(__name__)
# creating an API object
api = Api(app)


class BookInfoExtractorByGutenbergId(Resource):
    def get(self):

        try:
            try:
                lstr_language = request.args.get('guternberg_id')

            except Exception as e:
                return ResponseGenerator().set_response(APIResponseCodes.bad_request, {}, "language input is missing")

            ltup_gutenberg_id = tuple(lstr_language.split(","))

            lobj_db_helper = DBHelper()
            llst_book_id = lobj_db_helper.extract_book_id_by_gutenberg_id(
                ltup_gutenberg_id)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_default_response(llst_book_id)


api.add_resource(BookInfoExtractorByGutenbergId, '/guternberg_api/get_books_by_guternberg_id')

if __name__ == '__main__':
    app.run(debug=True)

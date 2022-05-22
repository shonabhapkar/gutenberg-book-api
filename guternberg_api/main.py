from guternberg_api.DBHelper import DBHelper
from flask import Flask
from flask_restful import Resource, Api
from guternberg_api.ResponseGenerator import ResponseGenerator

app = Flask(__name__)
# creating an API object
api = Api(app)


class BookInfoExtractorByGutenbergId(Resource):
    def get(self, pstr_language):

        try:
            ltup_gutenberg_id = tuple(pstr_language.split(","))

            lobj_db_helper = DBHelper()
            llst_book_id = lobj_db_helper.extract_book_id_by_gutenberg_id(
                ltup_gutenberg_id)

            return ResponseGenerator().get_response(llst_book_id)

        except Exception as e:
            return ResponseGenerator().get_default_response(llst_book_id)
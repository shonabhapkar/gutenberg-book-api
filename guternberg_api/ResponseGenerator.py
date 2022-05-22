from guternberg_api.DBHelper import DBHelper


class APIResponse:
    message: str
    code: int
    response: {}

    def __rep__(self):
        return {"code": self.code,
                "response": self.response,
                "message": self.message}

class APIResponseCodes:
    created = 201
    ok = 200
    no_content = 204
    bad_request = 400
    not_found = 404

class ResponseGenerator:

    def get_response(self, plst_book_id):
        try:
            llst_books = []
            lobj_db_helper = DBHelper()

            for lint_book_id in plst_book_id:
                ldict_book_info = {}
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

            if llst_books:
                ldict_result = {"total_no_of_books": len(plst_book_id),
                                "books": llst_books}

                APIResponse.code = APIResponseCodes.ok
                APIResponse.response = ldict_result
                APIResponse.message = "Books extracted Successfully"

                return APIResponse.__rep__()
            else:
                APIResponse.code = APIResponseCodes.no_content
                APIResponse.response = {}
                APIResponse.message = "No Book found"

                return APIResponse.__rep__()
        except Exception as e:
            # logger.error(str(e), exc_info=True)
            return self.get_default_response()


    def get_default_response(self):
        APIResponse.code = APIResponseCodes.ok
        APIResponse.response = {}
        APIResponse.message = "Books extracted Successfully"

        return APIResponse.__rep__()
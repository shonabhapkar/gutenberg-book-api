from guternberg_api.DBHelper import DBHelper
from guternberg_api.logger import logger

class APIResponse:
    def __init__(self, code, response, message):
        self.message = message
        self.code = code
        self.response = response

    def get_response(self):
        return {"code": self.code,
                "response": self.response,
                "message": self.message}


class APIResponseCodes:
    created = 201
    ok = 200
    no_content = 204
    bad_request = 400
    not_found = 404
    server_error = 500

class ResponseGenerator:

    def create_books_info_json_response(self, plst_books):
        try:
            if plst_books:
                ldict_result = {"total_no_of_books": len(plst_books),
                                "books": plst_books}

                lobj_response_api = APIResponse(APIResponseCodes.ok, ldict_result,
                                                "Books extracted Successfully")
                return lobj_response_api.get_response()
            else:
                lobj_response_api = APIResponse(APIResponseCodes.no_content, {},
                                                "No Book found")
                return lobj_response_api.get_response()

        except Exception as e:
            logger.error(str(e), extra={'plst_books': plst_books}, exc_info=True)
            return self.get_error_response()

    def get_error_response(self):
        lobj_response_api = APIResponse(APIResponseCodes.server_error, {},
                                        "Server Error")
        return lobj_response_api.get_response()

    def get_bad_request_response(self, pstr_message):
        lobj_response_api = APIResponse(APIResponseCodes.bad_request, {}, pstr_message)
        return lobj_response_api.get_response()
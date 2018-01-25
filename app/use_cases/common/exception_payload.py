from flask import jsonify


class ExceptionPayload(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

    @staticmethod
    def generate_payload_res(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

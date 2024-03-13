from flask_restx import Resource

from .namespaces import anagram_ns


@anagram_ns.route('/', methods=['POST'])
class AnagramAnswer(Resource):
    @anagram_ns.response(200, 'Cars successfully retrieved.')
    @anagram_ns.doc('get_cars')
    def post(self):
        """List all cars"""
        return "Miam"

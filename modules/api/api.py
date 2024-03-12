from flask_restx import Api

from modules.anagrame.api import anagram_ns

from .blueprint import api_bp

api = Api(api_bp, title='Flask API', version='1.0', description='A simple Flask API', doc='/doc/')

api.add_namespace(anagram_ns, path='/anagram')

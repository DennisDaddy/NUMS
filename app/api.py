from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from app.models import *

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    """This is a class for root endpoint"""
    def get(self):
        """This is a method for getting root endpoint using GET request"""
        return jsonify({'message': 'Welcome to Stackoverflow-lite'})

class QuestionList(Resource):
    """This is a class for questions without IDs"""
    def get(self):
        """This is a method for getting a list of questions using GET request"""
        pass
    
    def post(self):
        """This is a method for creating a question using POST request"""
        title = request.get_json()['title']
        content = request.get_json()['content']

        if len(title) ==0:
            return jsonify({'message': 'Fill in the title'})
        if len(content) ==0:
            return jsonify({'message': 'Fill in the content'})
        cur.execute("INSERT INTO questions (title, content) VALUES('"+title+"','"+content+"');")
        conn.commit()
        return jsonify({'message': 'Question successfully created'})


class Question(Resource):
    pass
    
api.add_resource(Home, '/')
api.add_resource(QuestionList, '/api/v1/questions', endpoint='questions')
api.add_resource(Question, '/api/v1/questions/<int:id>', endpoint='question')
if __name__ == '__main__':
    app.run(debug=True)
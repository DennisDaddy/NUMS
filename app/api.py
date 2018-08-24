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
        """This is a method for retrieving a list of questions using GET request"""
        my_list = []
        try:
            cur.execute("SELECT * FROM questions")
            rows = cur.fetchall()
            for row in rows:
                my_list.append(row[0])
                my_list.append(row[1])
                my_list.append(row[2])
        except:
            return jsonify({'message': 'Cannot retrieve entries'})
        return jsonify(my_list)
    
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
        return jsonify({'message': 'Question successfully created!'})


class Question(Resource):
    """This is a class for questions with IDs"""

    def get(self, id):
        """This is a method for retrieving question using GET request"""
        cur.execute("SELECT * FROM questions WHERE ID= %s", (id,))
        result = cur.fetchone()
        if result is None:
            return jsonify({'message': 'Question not found!'})
        return jsonify(result)

    def put(self, id):
        """This is a method for modifying a question using PUT request"""
        cur.execute("SELECT * FROM questions WHERE ID= %s", (id,))
        question = cur.fetchone()
        
        title = request.get_json()['title']
        content = request.get_json()['content']       

        if question is not None:
            cur.execute("UPDATE questions SET title=%s, content=%s WHERE id=%s", (title, content, id))            
        else:
            return jsonify({'message': 'Not complete no entry!'})
        conn.commit()
        return jsonify({'message': 'Entry successfuly Updated'})

        
        


    
api.add_resource(Home, '/')
api.add_resource(QuestionList, '/api/v1/questions', endpoint='questions')
api.add_resource(Question, '/api/v1/questions/<int:id>', endpoint='question')
if __name__ == '__main__':
    app.run(debug=True)
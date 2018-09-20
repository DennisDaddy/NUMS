"""Import flask modules"""
import sys
from flask import Flask, jsonify, request, make_response
# from flask_cors import CORS
from flask_restful import Resource, Api
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
#     get_jwt_identity
# )


from app.models import *

app = Flask(__name__)
# CORS(app)
api = Api(app)
app.config['JWT_SECRET_KEY'] = '5c750c0e72ce5394dfe7720fa26d0327d616ff9ff869be19'
# jwt = JWTManager(app)


class Home(Resource):
    """This is a class for root endpoint"""
    def get(self):
        """This is a method for getting root endpoint using GET request"""
        return jsonify({'message': 'Welcome to Stackoverflow-lite'})

class QuestionList(Resource):
    """This is a class for questions without IDs"""

    # @jwt_required
    def get(self):
        """This is a method for retrieving a list of questions using GET request"""
        cur.execute("SELECT * FROM questions")
        questions = cur.fetchall()
        if questions is None:
            return jsonify({"messge": "No questions found!"})
        else:
            return jsonify(questions)
        conn.commit()

    # @jwt_required
    def post(self):
        """This is a method for creating a question using POST request"""
        title = request.get_json()['title']
        content = request.get_json()['content']

        if len(title) == 0:
            return jsonify({'message': 'Fill in the title'})
        if len(title) > 50:
            return jsonify({'message': 'Failed! title cannot be greater than 50 characters'})

        if len(content) == 0:
            return jsonify({'message': 'Fill in the content'})

        if len(content) > 200:
            return jsonify({'message': 'Failed! content cannot be greater than 200 characters'})

        cur.execute("INSERT INTO questions (title, content) VALUES('"+title+"','"+content+"');")
        conn.commit()
        return jsonify({'message': 'Question successfully created!'})


class Question(Resource):
    """This is a class for questions with IDs"""

    # @jwt_required
    def get(self, id):
        """This is a method for retrieving question using GET request"""
        cur.execute("SELECT * FROM questions WHERE ID= %s", (id,))
        result = cur.fetchone()
        if result is None:
            return jsonify({'message': 'Question not found!'})
        return jsonify(result)

    # @jwt_required
    def put(self, id):
        """This is a method for modifying a question using PUT request"""
        cur.execute("SELECT * FROM questions WHERE ID= %s", (id,))
        question = cur.fetchone()

        title = request.get_json()['title']
        content = request.get_json()['content']

        if question is not None:
            cur.execute("UPDATE questions SET title=%s, content=%s WHERE id=%s",\
            (title, content, id))
        else:
            return jsonify({'message': 'Not complete no entry!'})
        conn.commit()
        return jsonify({'message': 'Question successfuly Updated'})

    # @jwt_required
    def delete(self, id):
        """This is a method for deleting a question using DELETE request"""
        try:
            cur.execute("DELETE FROM questions WHERE ID = %s", (id,))
            conn.commit()
        except:
            return jsonify({'message': 'Cant retrieve the question!'})
        finally:
            conn.close()
        return jsonify({'message': 'Question successfully deleted!'})


class  AnswerList(Resource):
    """This is a class for answers without IDs"""

    # @jwt_required
    def get(self):
        """This is a method for retrieving an answers using GET request """
        cur.execute("SELECT * FROM answers")
        answers = cur.fetchall()
        if answers is None:
            return jsonify({'message': 'No answers found'})
        else:
            return jsonify(answers)
        conn.commit()

    # @jwt_required
    def post(self):
        """This is a method for creating an answer using POST request"""
        body = request.get_json()['body']

        if len(body) == 0:
            return jsonify({'message': 'Fill in the body'})
        cur.execute("INSERT INTO answers (body) VALUES('"+body+"');")
        conn.commit()
        return jsonify({'message': 'Answer successfully created!'})

class Answer(Resource):
    """This is a class for answers with IDs"""

    # @jwt_required
    def get(self, id):
        """This is a method for getting an answer using GET request"""
        cur.execute("SELECT * FROM answers WHERE ID= %s", (id,))
        result = cur.fetchone()
        if result is None:
            return jsonify({'message': 'Answer not found!'})
        return jsonify(result)

    # @jwt_required
    def put(self, id):
        """This is a method for modifying an answer using PUT request"""
        cur.execute("SELECT * FROM answers WHERE ID= %s", (id,))
        answer = cur.fetchone()

        body = request.get_json()['body']

        if answer is not None:
            cur.execute("UPDATE answers SET body=%s WHERE id=%s", (body, id))
        else:
            return jsonify({'message': 'Not complete no answer!'})
        conn.commit()
        return jsonify({'message': 'Answer successfuly Updated'})
    # @jwt_required
    def delete(self, id):
        """This is a method for deleting an answer for a question using DELETE request"""
        try:
            cur.execute("DELETE FROM answers WHERE ID = %s", (id,))
            conn.commit()
        except:
            return jsonify({'message': 'Cant retrieve answer!'})
        finally:
            conn.close()
        return jsonify({'message': 'Answer successfully deleted!'})


class CommentList(Resource):
    """This is a class for retrieving comments without IDs"""
    # @jwt_required
    def post(self):
        """This is a method for creating a comment using POST request"""

        body = request.get_json()['body']
        if len(body) == 0:
            return jsonify({'message': 'Fill in the comment body'})
        cur.execute("INSERT INTO comments (body) VALUES('"+body+"');")
        conn.commit()
        return jsonify({'message': 'Comment successfully created!'})

class Comment(Resource):
    """This is a class for comments with IDs"""
    # @jwt_required
    def get(self, id):
        """This is a method for getting a comment information using GET request"""

        cur.execute("SELECT * FROM comments WHERE ID= %s", (id,))
        result = cur.fetchone()
        if result is None:
            return jsonify({'message': 'Comment not found!'})
        return jsonify(result)
    # @jwt_required
    def put(self, id):
        """This is a method for modifying a comment using PUT request"""

        cur.execute("SELECT * FROM comments WHERE ID= %s", (id,))
        comment = cur.fetchone()
        body = request.get_json()['body']

        if comment is not None:
            cur.execute("UPDATE comments SET body=%s WHERE id=%s", (body, id))
        else:
            return jsonify({'message': 'Not complete, no comment!'})
        conn.commit()
        return jsonify({'message': 'Comment successfuly Updated'})
    # @jwt_required
    def delete(self, id):
        """This is a method for deleting a comment using DELETE request"""
        try:
            cur.execute("DELETE FROM comments WHERE ID = %s", (id,))
            conn.commit()
        except:
            return jsonify({'message': 'Cant retrieve the comment!'})
        finally:
            conn.close()
        return jsonify({'message': 'Comment successfully deleted'})


class UserRegistration(Resource):
    """This is a class for registering new users"""


    def post(self):
        """This a method for registering a user using POST request """
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        password_confirmation = request.get_json()['password_confirmation']

        if not username or len(username.strip()) == 0:
            return jsonify({"message": "Username cannot be blank!"})
        elif not email:
            return jsonify({"message": "Email cannot be blank!"})
        elif not password:
            return jsonify({"message": "Password cannot be blank!"})
        elif password != password_confirmation:
            return jsonify({"message": "Password does not match!"})
        elif len(password) < 5:
            return jsonify({"message": "Password cannot be less than 5 characters!"})

        cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"'")
        user = cur.fetchone()
        if user is None:
            cur.execute("INSERT INTO users (username, email, password, password_confirmation)\
            VALUES('"+username+"', '"+email+"', '"+password+"', '"+password_confirmation+"');")
        else:
            return jsonify({'message': 'User already exists'})
        conn.commit()
        return jsonify({'message': 'You are successfully registered!'})

class UserLogin(Resource):
    """This is a class for logging in a user"""

    def post(self):
        """This method checks if a user exists in database, checks if username and password matches
        the one in the database then logs in the user using POST request"""
        username = request.get_json()['username']
        password = request.get_json()['password']

        cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"'\
        AND password LIKE '"+password+"'")
        user = cur.fetchone()
        if not user:
            return jsonify({'message': 'Invalid username/password combination, try again'})
        # return jsonify({'message': 'Login successful!'})
        # access_token = create_access_token(identity=username)
        # return jsonify(access_token=access_token)
    conn.commit()

class UserInfo(Resource):
    """This is a class for retrieving user information"""
    # @jwt_required
    def get(self, user_id):
        """This is a method for retrieving user information"""
        cur.execute("SELECT * FROM users WHERE ID = %s", (user_id,))
        info = cur.fetchone()
        if info is None:
            return jsonify({'messsage': 'That user is not Available'})
        return jsonify(info)


api.add_resource(Home, '/api/v1')
api.add_resource(UserRegistration, '/api/v1/auth/register')
api.add_resource(UserLogin, '/api/v1/auth/login')
api.add_resource(UserInfo, '/api/v1/account/<int:user_id>')
api.add_resource(QuestionList, '/api/v1/questions', endpoint='questions')
api.add_resource(Question, '/api/v1/questions/<int:id>', endpoint='question')
api.add_resource(AnswerList, '/api/v1/answers', endpoint='answers')
api.add_resource(Answer, '/api/v1/answers/<int:id>', endpoint='answer')

api.add_resource(CommentList, '/api/v1/comments', endpoint='comments')
api.add_resource(Comment, '/api/v1/comments/<int:id>', endpoint='comment')



if __name__ == '__main__':
    app.run(debug=True)

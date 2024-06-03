from flask_login import UserMixin
import json
import uuid

class User(UserMixin):
    def __init__(self, username, email, password, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        with open('db.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['id'] == user_id:
                    return User(**user)

    @classmethod
    def find_by_email(cls, email):
        with open('db.json', 'r') as file:
            users = json.load(file)
            user = next((x for x in users if x['email'] == email), None)
            if user:
                return cls(**user)

    @classmethod
    def find_by_username(cls, username):
        with open('db.json', 'r') as file:
            users = json.load(file)
            user = next((x for x in users if x['username'] == username), None)
            if user:
                return cls(**user)
    
    def save_to_db(self):
        with open('db.json', 'r') as file:
            users = json.load(file)
            users.append({'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password})

        with open('db.json', 'w') as file:
            json.dump(users, file)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

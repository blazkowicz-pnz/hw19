from setup_db import db
from dao.model.user import User


class AuthDao:
    def get_by_username(self, username):
        return db.session.query(User).filter(User.username == username).first()


        # return {
        #     "username": "ivan",
        #     "password": "A5Si7eMyyaE+uC6bJGMWBMMd+Xi04vD70sVJlE+deaU=",
        #     "role": "admin"
        # }
import hmac

from dao.user import UserDao
import hashlib, base64
from config import Config

class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = self.get_hash_from_password(user_data.get("password"))

        return self.dao.create(user_data)

    def update(self, user_data):
        user_data["password"] = self.get_hash_from_password(user_data.get("password"))
        uid = user_data.get("id")
        user = self.get_one(uid)
        user.username = user_data.get("username")
        user.role = user_data.get("role")
        user.password = user_data.get("password")
        return self.dao.update(user)


    def delete(self, uid):
        return self.dao.delete(uid)


    def get_hash_from_password(self, password): # В методе по дз несколько иначе реализован
        return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            Config.SECRET_HERE,
            Config.PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    # На всякий случай сравнение
    def compare_pass(self, pass_hash, other_pass):
        decode_digest = base64.b64decode(pass_hash)
        hash_digest = hashlib.pbkdf2_hmac("sha256",
                                          other_pass.encode(),
                                          Config.SECRET_HERE,
                                          Config.PWD_HASH_ITERATIONS)
        return hmac.compare_digest(decode_digest, hash_digest)


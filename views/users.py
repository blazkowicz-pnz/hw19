from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service
from dao.model.user import UserSchema

ns_user = Namespace("users")


@ns_user.route("/")
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

    def post(self):
        req_data = request.json
        user = user_service.create(req_data)
        return "", 201, {"location": f"/users/{user.id}"}


@ns_user.route("/<int:uid>")
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200


    def put(self, uid):
        req_data = request.json
        req_data["id"] = uid
        user_service.update(req_data)
        return "", 204

    def patch(self, uid):
        req_data = request.json
        req_data["id"] = uid
        user_service.update(req_data)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204

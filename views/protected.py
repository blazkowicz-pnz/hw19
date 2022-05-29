from flask_restx import Resource, Namespace

from utils import auth_required, admin_access_required

ns_protected = Namespace("protected")

@ns_protected.route("/users")
class UsersView(Resource):
    @auth_required
    def get(self):
        return {}, 200


@ns_protected.route("/admin")
class AdminView(Resource):
    @admin_access_required
    def get(self):
        return {}, 200
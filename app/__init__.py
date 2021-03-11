from flask import Flask, jsonify
from flask_graphql import GraphQLView
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object((set_environment_config()))

    db.init_app(app)

    from app.models.User import User
    from app.models.VerificationCode import VerificationCode

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.route("/ping")
    def pong():
        return jsonify({"msg": "pong"})

    from .schema import schema

    app.add_url_rule(
        "/",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=False,
        ),
    )

    # app.add_url_rule(
    #     "/graphql",
    #     view_func=GraphQLView.as_view(
    #         "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
    #     ),
    # )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app


def set_environment_config():
    return "config.DefaultConfig"

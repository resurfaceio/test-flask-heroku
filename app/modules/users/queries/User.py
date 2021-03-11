from flask_jwt_extended import get_jwt_identity, jwt_required
from graphene import Field, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app.models.User import User as UserModel


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("password",)


class User(ObjectType):
    user = Field(
        UserType,
    )

    @jwt_required
    def resolve_user(self, info):
        id = get_jwt_identity()
        user_ = UserModel.query.filter_by(id=id).scalar()
        if user_:
            return user_
        else:
            raise GraphQLError("User is not found.")

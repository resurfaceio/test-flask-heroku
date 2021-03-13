from graphene import ObjectType

from .User import User


class UserQuery(User, ObjectType):
    pass

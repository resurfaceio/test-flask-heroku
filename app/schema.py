from graphene import ObjectType, Schema, String

from app.modules.news.mutations import NewsMutation
from app.modules.news.queries import NewsQuery
from app.modules.users.mutations import UserMutation
from app.modules.users.queries import UserQuery


class RootQuery(UserQuery, NewsQuery, ObjectType):
    pass


class RootMutation(UserMutation, NewsMutation, ObjectType):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)

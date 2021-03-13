from graphene import AbstractType

from .RegisterUser import RegisterUser


class UserMutation(AbstractType):
    create_user = RegisterUser.Field()

from graphene import ObjectType

from .News import News, NewsType


class NewsQuery(News, ObjectType):
    pass

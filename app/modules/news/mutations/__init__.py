from graphene import AbstractType

from .AddNews import AddNews


class NewsMutation(AbstractType):
    add_news = AddNews.Field()

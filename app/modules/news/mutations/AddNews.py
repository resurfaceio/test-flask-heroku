import graphene
from flask_jwt_extended import get_jwt_identity, jwt_required
from graphene import Boolean, Mutation, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app.models.News import News as NewsModel
from app.modules.news.queries import NewsType


class AddNews(Mutation):
    class Arguments:
        title = String(description="Self Descriptive")
        body = String(description="Self Descriptive")

    news = graphene.Field(NewsType)

    def mutate(self, info, **kwargs):

        news = NewsModel(**kwargs)
        try:
            news.save()
        except Exception as e:
            raise GraphQLError("Error creating news object.", e)
        else:
            return AddNews(news=news)

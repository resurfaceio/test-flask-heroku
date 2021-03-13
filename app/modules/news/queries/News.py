import graphene
from flask_jwt_extended import get_jwt_identity, jwt_required
from graphene import Field, List, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app.models.News import News as NewsModel


class NewsType(SQLAlchemyObjectType):
    class Meta:
        model = NewsModel


class News(ObjectType):
    all_news = List(NewsType)
    news_by_id = Field(NewsType, id=graphene.String())

    def resolve_all_news(self, info):
        return NewsModel.query.all()

    def resolve_news_by_id(self, info, id):
        news_ = NewsModel.query.filter_by(id=id).scalar()
        if news_:
            return news_
        else:
            raise GraphQLError("News not found.")

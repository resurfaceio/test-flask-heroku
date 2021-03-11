from graphene import Boolean, Mutation, String
from graphql import GraphQLError

from app.models.User import User as UserModel


class RegisterUser(Mutation):
    ok = Boolean(description="Request status")
    message = String(description="Request message")

    class Input:
        email = String(description="Self Descriptive")
        password = String(description="Self Descriptive")

    def mutate(self, info, **kwargs):
        user = UserModel(**kwargs)
        try:
            user.save()

        except Exception as e:
            raise GraphQLError("Error creating User object.", e)
        else:
            ok = True
            message = "User have been created successfully"
            return RegisterUser(ok=ok, message=message)

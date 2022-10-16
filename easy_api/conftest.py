import pytest
from factory.faker import faker

from easy_api.users.models import User
from easy_api.users.tests.factories import UserFactory

FAKE = faker.Faker()


@pytest.fixture
def user(db) -> User:
    yield UserFactory()


# @pytest.fixture
# def user_factory() -> [User]:
#     def generate_users(count: int):
#         return [UserFactory() for i in range(count)]
#
#     yield generate_users

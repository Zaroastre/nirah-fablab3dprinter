from api import CrudApi, AuthenticationApi;
from entity import Credential, User;

class AbstractDao:
    def __init__(self) -> None:
        pass;

class CrudDao(AbstractDao, CrudApi):
    def __init__(self) -> None:
        AbstractDao.__init__(self);
        CrudApi.__init__(self);

    def create(self, entity):
        return entity;

    def read(self, identifier):
        return CrudApi.read(identifier);

    def update(self, identifier, entity):
        return CrudApi.update(identifier, entity);

    def delete(self, identifier, entity):
        return CrudApi.delete(identifier, entity);

class AuthenticationDao(AbstractDao, AuthenticationApi):
    def __init__(self) -> None:
        AbstractDao.__init__(self);
        AuthenticationApi.__init__(self);

    def login(self, user: Credential) -> User:
        return AuthenticationApi.login(user);

    def logout(self, user: Credential) -> User:
        return AuthenticationApi.logout(user);

    def register(self, user: Credential) -> User:
        return AuthenticationApi.register(user);

    def unregister(self, user: Credential) -> User:
        return AuthenticationApi.unregister(user);

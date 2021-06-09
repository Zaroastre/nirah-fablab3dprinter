from .api import CrudApi, AuthenticationApi;

class AbstractDao:
    def __init__(self) -> None:
        pass;

class CrudDao(AbstractDao, CrudApi):
    def __init__(self) -> None:
        AbstractDao.__init__(self);
        CrudApi.__init__(self);
    
    def create(self, entity):
        return CrudApi.create(entity);
    
    def read(self, identifier):
        return CrudApi.read(identifier);

    def update(self, identifier, entity):
        return CrudApi.update(identifier, entity);
    
    def delete(self, identifier, entity):
        return CrudApi.delete(identifier, entity);

class AuthenticationDao(CrudDao, AuthenticationApi):
    def __init__(self) -> None:
        CrudDao.__init__(self);
        AuthenticationApi.__init__(self);

    def login(self, user: User) -> User:
        return AuthenticationApi.login(user);
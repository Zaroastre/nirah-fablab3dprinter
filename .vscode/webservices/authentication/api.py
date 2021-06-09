from .entity import User;

class CrudApi:
    def create(self, entity):
        raise NotImplementedError;
    def read(self, identifier):
        raise NotImplementedError;
    def update(self, identifier, entity):
        raise NotImplementedError;
    def delete(self, identifier, entity):
        raise NotImplementedError;

class AuthenticationApi:
    def register(self, user: User) -> User:
        raise NotImplementedError;
    
    def unregister(self, user: User) -> User:
        raise NotImplementedError;
    
    def login(self, user: User) -> User:
        raise NotImplementedError;
    
    def logout(self, user: User) -> User:
        raise NotImplementedError;

    def verify(self, token: str) -> User:
        raise NotImplementedError;
        
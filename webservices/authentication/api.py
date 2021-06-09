from entity import Credential, User;

class CrudApi:
    def create(self, entity: Credential) -> User:
        raise NotImplementedError;
    def read(self, identifier: int) -> User:
        raise NotImplementedError;
    def update(self, identifier: int, entity: Credential) -> User:
        raise NotImplementedError;
    def delete(self, identifier, entity: Credential) -> User:
        raise NotImplementedError;

class AuthenticationApi:
    def register(self, user: Credential) -> User:
        raise NotImplementedError;

    def unregister(self, user: Credential) -> User:
        raise NotImplementedError;

    def login(self, user: Credential) -> User:
        raise NotImplementedError;

    def logout(self, user: Credential) -> User:
        raise NotImplementedError;

    def verify(self, token: str) -> User:
        raise NotImplementedError;

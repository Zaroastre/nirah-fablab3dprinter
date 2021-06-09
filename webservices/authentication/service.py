from api import CrudApi, AuthenticationApi;
from repository import AbstractRepository, CrudRepository, AuthenticationRepository;
from entity import Credential, User;

class AbstractService:
    def __init__(self, repository: AbstractRepository) -> None:
        self.__repository: AbstractRepository = repository;

class CrudService(AbstractService, CrudApi):
    def __init__(self, repository: CrudRepository) -> None:
        AbstractService.__init__(self, repository=repository);
        CrudApi.__init__(self);
        self.__repository: CrudDao = repository;
    def create(self, entity: Credential) -> User:
        return self.__repository.create(entity);

    def read(self, identifier: int) -> User:
        return self.__repository.read(identifier);

    def update(self, identifier: int, entity: Credential) -> User:
        return self.__repository.update(identifier, entity);

    def delete(self, identifier: int, entity: Credential) -> User:
        return self.__repository.delete(identifier, entity);

class AuthenticationService(AbstractService, AuthenticationApi):
    def __init__(self, repository: AuthenticationRepository) -> None:
        CrudService.__init__(self, repository=repository);
        AuthenticationApi.__init__(self);
        self.___repository: AuthenticationRepository = repository;

    def register(self, user: Credential) -> User:
        return self.__repository.register(user);

    def unregister(self, user: Credential) -> User:
        return self.__repository.unregister(user);

    def login(self, user: Credential) -> User:
        return self.__repository.login(user);

    def logout(self, user: Credential) -> User:
        return self.__repository.logout(user);

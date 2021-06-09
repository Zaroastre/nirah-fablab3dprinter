from api import CrudApi, AuthenticationApi;
from dao import AbstractDao, CrudDao, AuthenticationDao;
from entity import Credential, User;

class AbstractRepository:
    def __init__(self, dao: AbstractDao) -> None:
        self.__dao: AbstractDao = dao;

class CrudRepository(AbstractRepository, CrudApi):
    def __init__(self, dao: CrudDao) -> None:
        AbstractRepository.__init__(self, dao=dao);
        CrudApi.__init__(self);
        self.__dao: CrudDao = dao;

    def create(self, entity: Credential) -> User:
        return self.__dao.create(entity);

    def read(self, identifier: int) -> User:
        return self.__dao.read(identifier);

    def update(self, identifier: int, entity: Credential) -> User:
        return self.__dao.update(identifier, entity);

    def delete(self, identifier: int, entity: Credential) -> User:
        return self.__dao.delete(identifier, entity);

class AuthenticationRepository(AbstractRepository, AuthenticationApi):
    def __init__(self, dao: AuthenticationDao) -> None:
        AbstractRepository.__init__(self, dao=dao);
        AuthenticationApi.__init__(self);
        self.__dao: AuthenticationDao = dao;

    def register(self, user: Credential) -> User:
        return self.__dao.register(user);

    def unregister(self, user: Credential) -> User:
        return self.__dao.unregister(user);

    def login(self, user: Credential) -> User:
        return self.__dao.login(user);

    def logout(self, user: Credential) -> User:
        return self.__dao.logout(user);

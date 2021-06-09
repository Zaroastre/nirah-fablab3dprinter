from .api import CrudApi, AuthenticationApi;
from .dao import AbstractDao, CrudDao, AuthenticationDao;
from .entity import User;

class AbstractRepository:
    def __init__(self, dao: AbstractDao) -> None:
        self.__dao: AbstractDao = dao;

class CrudRepository(AbstractRepository, CrudApi):
    def __init__(self, dao: CrudDao) -> None:
        AbstractRepository.__init__(self, dao=dao);
        CrudApi.__init__(self);
        self.__dao: CrudDao = dao;
    
    def create(self, entity):
        return self.__dao.create(entity);

    def read(self, identifier):
        return self.__dao.read(identifier);
    
    def update(self, identifier, entity):
        return self.__dao.update(identifier, entity)

    def delete(self, identifier, entity):
        return self.__dao.delete(identifier, entity)

class AuthenticationRepository(CrudRepository, AuthenticationApi):
    def __init__(self, dao: AuthenticationDao) -> None:
        CrudRepository.__init__(self, dao=dao);
        AuthenticationApi.__init__(self);
        self.__dao: AuthenticationDao = dao;
    
    def register(self, user: User):
        return super().register(user);
    
    def unregister(self, user: User):
        return super().unregister(user);

    def login(self, user: User):
        return super().login(user);
    
    def logout(self, user: User):
        return super().logout(user);
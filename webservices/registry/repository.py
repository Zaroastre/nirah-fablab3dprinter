from api import CrudApi, RegistryApi;
from dao import AbstractDao, CrudDao, RegistryDao;
from entity import WebService;

class AbstractRepository:
    def __init__(self, dao: AbstractDao) -> None:
        self.__dao: AbstractDao = dao;

class CrudRepository(AbstractRepository, CrudApi):
    def __init__(self, dao: CrudDao) -> None:
        AbstractRepository.__init__(self, dao=dao);
        CrudApi.__init__(self);
        self.__dao: CrudDao = dao;

    def create(self, entity: WebService) -> WebService:
        return self.__dao.create(entity);

    def read(self, identifier: int) -> WebService:
        return self.__dao.read(identifier);

    def update(self, identifier: int, entity: WebService) -> WebService:
        return self.__dao.update(identifier, entity);

    def delete(self, identifier: int, entity: WebService) -> WebService:
        return self.__dao.delete(identifier, entity);

class RegistryRepository(AbstractRepository, RegistryApi):
    def __init__(self, dao: RegistryDao) -> None:
        AbstractRepository.__init__(self, dao=dao);
        RegistryApi.__init__(self);
        self.__dao: RegistryDao = dao;

    def register(self, user: WebService) -> WebService:
        return self.__dao.register(user);

    def unregister(self, user: WebService) -> WebService:
        return self.__dao.unregister(user);

    def login(self, user: WebService) -> WebService:
        return self.__dao.login(user);

    def logout(self, user: WebService) -> WebService:
        return self.__dao.logout(user);

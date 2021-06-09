from .api import CrudApi, AuthenticationApi;
from .repository import AbstractRepository, CrudDao, AuthenticationDao;

class AbstractService:
    def __init__(self, dao: AbstractRepository) -> None:
        self.__dao: AbstractRepository = dao;

class CrudService(AbstractService, CrudApi):
    def __init__(self, dao: CrudDao) -> None:
        AbstractService.__init__(self, dao=dao);
        CrudApi.__init__(self);
        self.__dao: CrudDao = dao;

class AuthenticationService(CrudService, AuthenticationApi):
    def __init__(self, dao: AuthenticationDao) -> None:
        CrudService.__init__(self, dao=dao);
        AuthenticationApi.__init__(self);
        self.___dao: AuthenticationDao = dao;

from api import CrudApi, AuthenticationApi;
from dao import AuthenticationDao;
from repository import AuthenticationRepository;
from service import AbstractService, AuthenticationService, CrudService;
from entity import Credential, User;

class AbstractController:
    def __init__(self, service: AbstractService):
        self.__service: AbstractService = service;

class CrudController(AbstractController, CrudApi):
    def __init__(self, service: CrudService):
        AbstractController.__init__(self, service=service);
        CrudApi.__init__(self);
        self.__service: CrudService = service;

    def create(self, entity: User):
        self.__service.create(entity=entity);

    def read(self, identifier: int):
        self.__service.read(identifier);

    def update(self, identifier: int, entity: User):
        self.__service.update(identifier, entity);

    def delete(self, identifier: int, entity: User):
        self.__service.delete(identifier, entity);

class AuthenticationController(AbstractController, AuthenticationApi):
    def __init__(self, service: AuthenticationService):
        AbstractController.__init__(self, service=service);
        AuthenticationApi.__init__(self);
        self.__service: AuthenticationService = service;

    def register(self, entity: Credential) -> User:
        self.__service.register(entity=entity);

    def unregister(self, entity: Credential) -> User:
        self.__service.unregister(entity=entity);

    def login(self, entity: Credential) -> User:
        self.__service.login(entity=entity);

    def logout(self, entity: Credential) -> User:
        self.__service.logout(entity=entity);


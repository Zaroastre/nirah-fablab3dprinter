from api import CrudApi, RegistryApi;
from dao import RegistryDao;
from repository import RegistryRepository;
from service import AbstractService, RegistryService, CrudService;
from entity import WebService;

class AbstractController:
    def __init__(self, service: AbstractService):
        self.__service: AbstractService = service;

class CrudController(AbstractController, CrudApi):
    def __init__(self, service: CrudService):
        AbstractController.__init__(self, service=service);
        CrudApi.__init__(self);
        self.__service: CrudService = service;

    def create(self, entity: WebService):
        self.__service.create(entity=entity);

    def read(self, identifier: int):
        self.__service.read(identifier);

    def update(self, identifier: int, entity: WebService):
        self.__service.update(identifier, entity);

    def delete(self, identifier: int, entity: WebService):
        self.__service.delete(identifier, entity);

class RegistryController(AbstractController, RegistryApi):
    def __init__(self, service: RegistryService):
        AbstractController.__init__(self, service=service);
        RegistryApi.__init__(self);
        self.__service: RegistryService = service;

    def register(self, entity: WebService) -> WebService:
        self.__service.register(entity=entity);

    def unregister(self, entity: WebService) -> WebService:
        self.__service.unregister(entity=entity);

    def login(self, entity: WebService) -> WebService:
        self.__service.login(entity=entity);

    def logout(self, entity: WebService) -> WebService:
        self.__service.logout(entity=entity);


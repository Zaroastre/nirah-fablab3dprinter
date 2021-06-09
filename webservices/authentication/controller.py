from .api import CrudApi, AuthenticationApi;
from .dao import AuthenticationDao;
from .repository import AuthenticationRepository;
from .service import AbstractService, AuthenticationService, CrudService;

class AbstractController:
    def __init__(self, service: AbstractService) -> None:
        self.__service: AbstractService = service;



class CrudController(AbstractController, CrudApi, AuthenticationApi):
    def __init__(self, service: CrudService) -> None:
        super().__init__();
        self.__service: CrudService = service;
    
    def create(self, entity): 
        self.__service.create(entity=entity);

    def read(self, identifier):
        self.__service.read(identifier);

    def update(self, identifier, entity):
        self.__service.update(identifier, entity);

    def delete(self, identifier, entity):
        self.__service.delete(identifier, entity);


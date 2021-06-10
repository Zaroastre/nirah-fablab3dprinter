from api import CrudApi, RegistryApi;
from repository import AbstractRepository, CrudRepository, RegistryRepository;
from entity import WebService;

class AbstractService:
    def __init__(self, repository: AbstractRepository) -> None:
        self.__repository: AbstractRepository = repository;

class CrudService(AbstractService, CrudApi):
    def __init__(self, repository: CrudRepository) -> None:
        AbstractService.__init__(self, repository=repository);
        CrudApi.__init__(self);
        self.__repository: CrudDao = repository;
    def create(self, entity: WebService) -> WebService:
        return self.__repository.create(entity);

    def read(self, identifier: int) -> WebService:
        return self.__repository.read(identifier);

    def update(self, identifier: int, entity: WebService) -> WebService:
        return self.__repository.update(identifier, entity);

    def delete(self, identifier: int, entity: WebService) -> WebService:
        return self.__repository.delete(identifier, entity);

class RegistryService(AbstractService, RegistryApi):
    def __init__(self, repository: RegistryRepository) -> None:
        CrudService.__init__(self, repository=repository);
        RegistryApi.__init__(self);
        self.___repository: RegistryRepository = repository;

    def register(self, user: WebService) -> WebService:
        return self.__repository.register(user);

    def unregister(self, user: WebService) -> WebService:
        return self.__repository.unregister(user);

    def login(self, user: WebService) -> WebService:
        return self.__repository.login(user);

    def logout(self, user: WebService) -> WebService:
        return self.__repository.logout(user);

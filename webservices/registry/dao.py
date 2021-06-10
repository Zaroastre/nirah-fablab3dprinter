from api import CrudApi, RegistryApi;
from entity import WebService;

class AbstractDao:
    def __init__(self) -> None:
        pass;

class CrudDao(AbstractDao, CrudApi):
    def __init__(self) -> None:
        AbstractDao.__init__(self);
        CrudApi.__init__(self);

    def create(self, entity):
        return entity;

    def read(self, identifier):
        return CrudApi.read(identifier);

    def update(self, identifier, entity):
        return CrudApi.update(identifier, entity);

    def delete(self, identifier, entity):
        return CrudApi.delete(identifier, entity);

class RegistryDao(AbstractDao, RegistryApi):
    def __init__(self) -> None:
        AbstractDao.__init__(self);
        RegistryApi.__init__(self);

    def login(self, user: WebService) -> WebService:
        return RegistryApi.login(user);

    def logout(self, user: WebService) -> WebService:
        return RegistryApi.logout(user);

    def register(self, user: WebService) -> WebService:
        return RegistryApi.register(user);

    def unregister(self, user: WebService) -> WebService:
        return RegistryApi.unregister(user);

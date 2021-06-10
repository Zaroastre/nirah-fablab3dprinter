from entity import WebService;

class CrudApi:
    def create(self, entity: WebService) -> WebService:
        raise NotImplementedError;
    def read(self, identifier: str) -> WebService:
        raise NotImplementedError;
    def update(self, identifier: str, entity: WebService) -> WebService:
        raise NotImplementedError;
    def delete(self, identifier: str) -> WebService:
        raise NotImplementedError;

class RegistryApi(CrudApi):
    def __init__(self):
        CrudApi.__init__(self);

    def register(self, entity: WebService) -> WebService:
        return super().create(entity);

    def unregister(self, identifier: str) -> bool:
        return super().delete(identifier);

    def hearthbeat(self, entity: WebService) -> bool:
        raise NotImplementedError;

    def list_all(self) -> list:
        raise NotImplementedError;

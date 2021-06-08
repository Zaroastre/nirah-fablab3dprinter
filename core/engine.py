from threading import Thread;

class Service(Thread):
    def __init__(self):
        self.name: str = None;
        self.version: str = None;
        self.status: str = None;

    def run(self):
        raise Exception("Not yet implemented.");

    def terminate(self):
        raise Exception("Not yet implemented.");

    def restart(self):
        raise Exception("Not yet implemented.");


class ServiceRegistry(Thread):
    def __init__(self):
        self.services: list = [];
    
    def register(self, service: Service):
        if (not service in self.services):
            self.services.append(service);
            return True;
        return False;
    
    def unregister(self, service: Service):
        if (service in self.services):
            self.services.remove(service);
            return True;
        return False;
    
    def run(self):
        raise Exception("Not yet implemented.");
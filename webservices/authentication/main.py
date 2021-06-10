#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from controller import CrudController;
from service import CrudService;
from repository import CrudRepository;
from dao import CrudDao;
from entity import User;
from web import HttpWebService;
from configuration import ApplicationConfiguration;

def main():
    CONFIGURATION: dict = ApplicationConfiguration.load();
    print("Hello from: {}".format(CONFIGURATION.get("ARTIFACT_ID")));

    http_web_service: HttpWebService = HttpWebService();
    is_registered: bool = http_web_service.register(registry=CONFIGURATION.get("REGISTRY"));
    if (is_registered):
        http_web_service.start();
        http_web_service.join();
        is_unregistered: bool = http_web_service.unregister(registry=CONFIGURATION.get("REGISTRY"));
        if (is_unregistered):
            pass;
    else:
        print("{} is not registered to the registry.".format(CONFIGURATION.get("ARTIFACT_ID")));

if __name__ == '__main__':
    main()

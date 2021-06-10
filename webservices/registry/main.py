#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from controller import CrudController;
from service import CrudService;
from repository import CrudRepository;
from dao import CrudDao;
from web import HttpWebService;
from configuration import ApplicationConfiguration;

def main():
    CONFIGURATION: dict = ApplicationConfiguration.load();
    print("Hello from: {}".format(CONFIGURATION.get("ARTIFACT_ID")));

    http_web_service: HttpWebService = HttpWebService(bind_port=int(CONFIGURATION.get("HTTP_PORT")));
    http_web_service.start();
    http_web_service.join();

if __name__ == '__main__':
    main()

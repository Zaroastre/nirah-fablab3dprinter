#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from controller import CrudController;
from service import CrudService;
from repository import CrudRepository;
from dao import CrudDao;
from entity import User;
from web import HttpWebService;

def main():
    print("Hello from: {}".format(__file__.replace('\\', '/').split('/')[-2]));
    http_web_service: HttpWebService = HttpWebService();
    http_web_service.start();

if __name__ == '__main__':
    main()

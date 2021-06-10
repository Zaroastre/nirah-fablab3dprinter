#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread;
from os import listdir;
from queue import Queue;
from os import system, chdir;
from time import sleep;

class Application(Thread):
    def __init__(self, executable: str) -> None:
        Thread.__init__(self);
        self.__executable: str = executable;

    def run(self):
        system("python {}".format(self.__executable));


def main():
    # Detected web services.
    WEB_SERVICE_FOLDER_PATH: str = "webservices";
    REGISTRY_FOLDER: str = "registry";
    EXECUTABLE: str = "main.py";
    APPLICATIONS: list = [];
    WEB_SERVICES_FOLDERS: list = listdir(path=WEB_SERVICE_FOLDER_PATH);
    if (REGISTRY_FOLDER in WEB_SERVICES_FOLDERS):
        WEB_SERVICES_FOLDERS.remove(REGISTRY_FOLDER);
    REGISTRY_WEB_SERVICE: Application = Application(executable="{}/{}/{}".format(WEB_SERVICE_FOLDER_PATH, REGISTRY_FOLDER, EXECUTABLE));
    APPLICATIONS.append(REGISTRY_WEB_SERVICE);
    REGISTRY_WEB_SERVICE.start();

    sleep(1)

    for WEB_SERVICE_FOLDER in WEB_SERVICES_FOLDERS:
        MICRO_WEB_SERVICE: Application = Application(executable="{}/{}/{}".format(WEB_SERVICE_FOLDER_PATH, WEB_SERVICE_FOLDER, EXECUTABLE));
        APPLICATIONS.append(MICRO_WEB_SERVICE);
        MICRO_WEB_SERVICE.start();

    # Wait while all web services are running.
    QUEUE = Queue(maxsize=len(APPLICATIONS));
    QUEUE.join();

if __name__ == '__main__':
    main()

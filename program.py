#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread;
from os import listdir;
from queue import Queue;
from os import system, chdir;

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
    APPLICATIONS.append(Application(executable="{}/{}/{}".format(WEB_SERVICE_FOLDER_PATH, REGISTRY_FOLDER, EXECUTABLE)));
    for WEB_SERVICE_FOLDER in WEB_SERVICES_FOLDERS:
        APPLICATIONS.append(Application(executable="{}/{}/{}".format(WEB_SERVICE_FOLDER_PATH, WEB_SERVICE_FOLDER, EXECUTABLE)));

    # Star web services.
    for APPLICATION in APPLICATIONS:
        APPLICATION.start();

    # Wait while all web services are running.
    QUEUE = Queue(maxsize=len(APPLICATIONS));
    QUEUE.join();

if __name__ == '__main__':
    main()

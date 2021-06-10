from bottle import Bottle, run, request, response
from json import loads as json_loads
from threading import Thread;
from truckpad.bottle.cors import CorsPlugin, enable_cors
from json import loads, dumps;
from os import system;
from entity import WebService, Version;
from configuration import ApplicationConfiguration;
import requests;

class HttpWebService(Thread):

    HTTP_SERVER: Bottle = Bottle();
    CONFIGURATION: dict = ApplicationConfiguration.load();

    def __init__(self, bind_address: str = "0.0.0.0", bind_port: int = 9601):
        Thread.__init__(self);
        self.__bind_address: str = bind_address;
        self.__bind_port: str = bind_port;

    @enable_cors
    @HTTP_SERVER.post("{}/applications/<identifier>".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def register(identifier):
        print(identifier);
        response.status = 204;
        return;

    @enable_cors
    @HTTP_SERVER.delete("{}/applications/<identifier>".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def unregister(identifier):
        response.status = 200;
        return None;

    @enable_cors
    @HTTP_SERVER.get("/version")
    def get_version():
        response.status = 200
        response.content_type = "application/json"
        return dumps(Version.parse(HttpWebService.CONFIGURATION.get("VERSION")).__dict__);


    def run(self):
        HttpWebService.HTTP_SERVER.install(CorsPlugin(origins=['*']));
        run(HttpWebService.HTTP_SERVER, host=self.__bind_address, port=self.__bind_port);

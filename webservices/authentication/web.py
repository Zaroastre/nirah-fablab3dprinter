from bottle import Bottle, run, request, response
from json import loads as json_loads
from threading import Thread;
from truckpad.bottle.cors import CorsPlugin, enable_cors
from json import loads, dumps;
from os import system;
from entity import User, Version, WebService;
from configuration import ApplicationConfiguration;
import requests;

class HttpWebService(Thread):

    HTTP_SERVER: Bottle = Bottle();
    CONFIGURATION: dict = ApplicationConfiguration.load();

    def __init__(self, bind_address: str = "127.0.0.1", bind_port: int = 9601):
        Thread.__init__(self);
        self.__bind_address: str = bind_address;
        self.__bind_port: str = bind_port;
        self.__properties: WebService = WebService();
        self.__properties.group_id = HttpWebService.CONFIGURATION.get("GROUP_ID");
        self.__properties.project_id = HttpWebService.CONFIGURATION.get("PROJECT_ID");
        self.__properties.artifact_id = HttpWebService.CONFIGURATION.get("ARTIFACT_ID");
        self.__properties.version = Version.parse(HttpWebService.CONFIGURATION.get("VERSION")).full;
        self.__properties.port = int(HttpWebService.CONFIGURATION.get("HTTP_PORT"));

    def register(self, registry) -> bool:
        version_response = None;
        is_registered: bool = False;
        try:
            version_response = requests.get("http://{}/version".format(registry));
        except Exception as error:
            print(error);
            pass
        if (version_response != None):
            if (version_response.status_code == 200):
                registry_version = version_response.json().get("full");
                registration_response = None;
                try:
                    registration_response = requests.post("http://{}/api/{}/applications/{}".format(registry, registry_version, HttpWebService.CONFIGURATION.get("ARTIFACT_ID")), json=self.__properties.__dict__);
                except Exception as error:
                    print(error);
                    pass
                if (registration_response != None):
                    if (registration_response.status_code == 204):
                        is_registered = True;
        return is_registered;

    def unregister(self, registry) -> bool:
        version_response = None;
        is_unregistered: bool = False;
        try:
            version_response = requests.get("http://{}/version".format(registry));
        except Exception as error:
            # print(error);
            pass
        if (version_response != None):
            if (version_response.status_code == 200):
                registry_version = version_response.json().get("full");
                registration_response = None;
                try:
                    registration_response = requests.delete("http://{}/api/{}/applications/{}".format(registry, registry_version, HttpWebService.CONFIGURATION.get("ARTIFACT_ID")), json={});
                except Exception as error:
                    # print(error);
                    pass
                if (registration_response != None):
                    if (registration_response.status_code == 204):
                        is_unregistered = True;
        return is_unregistered;

    @enable_cors
    @HTTP_SERVER.get("{}/test".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def test():
        response.status = 200
        response.content_type = "application/json"
        return dumps(User().__dict__);

    def run(self):
        HttpWebService.HTTP_SERVER.install(CorsPlugin(origins=['*']));
        run(HttpWebService.HTTP_SERVER, host=self.__bind_address, port=self.__bind_port);


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
    REGISTERED_SERVICES: dict = {};

    def __init__(self, bind_address: str = "0.0.0.0", bind_port: int = 9600):
        Thread.__init__(self);
        self.__bind_address: str = bind_address;
        self.__bind_port: str = bind_port;

    @enable_cors
    @HTTP_SERVER.post("{}/applications/<identifier>".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def register(identifier):
        if (not identifier in HttpWebService.REGISTERED_SERVICES.keys()):
            HttpWebService.REGISTERED_SERVICES[identifier] = WebService.parse(request.json);
            HttpWebService.REGISTERED_SERVICES.get(identifier).host = request.headers.get("Host").split(':')[0];
        response.status = 204;
        return;

    @enable_cors
    @HTTP_SERVER.delete("{}/applications/<identifier>".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def unregister(identifier):
        if (identifier in HttpWebService.REGISTERED_SERVICES.keys()):
            HttpWebService.REGISTERED_SERVICES.pop(identifier);
            response.status = 204;
        else:
            response.status = 404;
        return;

    @enable_cors
    @HTTP_SERVER.get("{}/applications".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def list_all():
        response.status = 200;
        content = {};
        for key in HttpWebService.REGISTERED_SERVICES.keys():
            content[key]=HttpWebService.REGISTERED_SERVICES.get(key).__dict__;
        return dumps(content);

    @enable_cors
    @HTTP_SERVER.get("/version")
    def get_version():
        response.status = 200
        response.content_type = "application/json"
        return dumps(Version.parse(HttpWebService.CONFIGURATION.get("VERSION")).__dict__);
    

    @enable_cors
    @HTTP_SERVER.get("/<service_id>/api/<service_version>/<url:path>")
    def forward_get(service_id, service_version, url):
        if (service_id in HttpWebService.REGISTERED_SERVICES.keys()):
            service: WebService = HttpWebService.REGISTERED_SERVICES.get(service_id)
            if (service.version == service_version):
                response.status = 200;
                try:
                    forward_response = requests.get(url="http://{}:{}/api/{}/{}".format(service.host, service.port, service.version, url), params=request.params, headers=request.headers);
                    for header_name in  forward_response.headers.keys():
                        response.set_header(header_name, forward_response.headers.get(header_name));
                    response.status = forward_response.status_code;
                    return forward_response.content;
                except Exception as error:
                    print(error)
                    response.status = 503;
                    return str(error);
            else:
                response.status = 404;
                return "API version not found.";
        else:
            response.status = 404;
            return "Service not found.";

    @enable_cors
    @HTTP_SERVER.post("/<service_id>/api/<service_version>/<url:path>")
    def forward_post(service_id, service_version, url):
        if (service_id in HttpWebService.REGISTERED_SERVICES.keys()):
            service: WebService = HttpWebService.REGISTERED_SERVICES.get(service_id)
            if (service.get("version") == service_version):
                response.status = 200;
                try:
                    forward_response = requests.post(url="http://{}:{}/api/{}/{}".format(service.host, service.port, service.get("version"), url), params=request.params, headers=request.headers, data=request.body);
                    response.headers = forward_response.headers;
                    response.status = forward_response.status_code;
                    return forward_response.content;
                except Exception as error:
                    response.status = 503;
                    return error;
            else:
                response.status = 404;
                return "API version not found.";
        else:
            response.status = 404;
            return "Service not found.";

    @enable_cors
    @HTTP_SERVER.put("/<service_id>/api/<service_version>/<url:path>")
    def forward_put(service_id, service_version, url):
        if (service_id in HttpWebService.REGISTERED_SERVICES.keys()):
            service: WebService = HttpWebService.REGISTERED_SERVICES.get(service_id)
            if (service.get("version") == service_version):
                response.status = 200;
                try:
                    forward_response = requests.put(url="http://{}:{}/api/{}/{}".format(service.host, service.port, service.get("version"), url), params=request.params, headers=request.headers, data=request.body);
                    response.headers = forward_response.headers;
                    response.status = forward_response.status_code;
                    return forward_response.content;
                except Exception as error:
                    response.status = 503;
                    return error;
            else:
                response.status = 404;
                return "API version not found.";
        else:
            response.status = 404;
            return "Service not found.";

    @enable_cors
    @HTTP_SERVER.delete("/<service_id>/api/<service_version>/<url:path>")
    def forward_delete(service_id, service_version, url):
        if (service_id in HttpWebService.REGISTERED_SERVICES.keys()):
            service: WebService = HttpWebService.REGISTERED_SERVICES.get(service_id)
            if (service.get("version") == service_version):
                response.status = 200;
                try:
                    forward_response = requests.delete(url="http://{}:{}/api/{}/{}".format(service.host, service.port, service.get("version"), url), params=request.params, headers=request.headers, data=request.body);
                    response.headers = forward_response.headers;
                    response.status = forward_response.status_code;
                    return forward_response.content;
                except Exception as error:
                    response.status = 503;
                    return error;
            else:
                response.status = 404;
                return "API version not found.";
        else:
            response.status = 404;
            return "Service not found.";

    def run(self):
        HttpWebService.HTTP_SERVER.install(CorsPlugin(origins=['*']));
        run(HttpWebService.HTTP_SERVER, host=self.__bind_address, port=self.__bind_port);

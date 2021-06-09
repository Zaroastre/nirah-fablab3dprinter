from bottle import Bottle, run, request, response
from json import loads as json_loads
from threading import Thread;
from truckpad.bottle.cors import CorsPlugin, enable_cors
from json import loads, dumps;
from os import system;
from entity import User;

class HttpWebService(Thread):

    HTTP_SERVER: Bottle = Bottle();
    CONFIGURATION: dict = loads(open("{}{}".format(__file__.replace(__file__.split('/')[-1], ''), "manifest.json"), "r").read());

    def __init__(self):
        Thread.__init__(self);

    @enable_cors
    @HTTP_SERVER.get("{}/test".format(CONFIGURATION.get("BASE_API").replace("{%VERSION%}", CONFIGURATION.get("VERSION"))))
    def test():
        response.status = 200
        response.content_type = "application/json"
        return dumps(User().__dict__);

    def run(self):
        HttpWebService.HTTP_SERVER.install(CorsPlugin(origins=['*']));
        run(HttpWebService.HTTP_SERVER, host="0.0.0.0", port=int(HttpWebService.CONFIGURATION.get("HTTP_PORT")));


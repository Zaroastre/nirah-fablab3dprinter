from threading import Thread;

from bottle import Bottle, run, request, response
from json import loads as json_loads
from truckpad.bottle.cors import CorsPlugin, enable_cors


class Server(Thread):
    HTTP_SERVER: Bottle = Bottle();
    
    def __init__(self):
        Thread.__init__(self);

    @enable_cors
    @HTTP_SERVER.get("/api/v0")
    def test():
        response.status = 404
        return "Test done!"

    def run(self):
        Server.HTTP_SERVER.install(CorsPlugin(origins=['*']));
        run(Server.HTTP_SERVER, host="0.0.0.0", port=9600);
    
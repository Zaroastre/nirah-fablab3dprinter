#!/usr/bin/env python3

from core.engine import ServiceRegistry
from server import Server

def main():

    SERVICE_REGISTRY: ServiceRegistry = ServiceRegistry();
    
    server = Server();
    server.start();


if __name__ == '__main__':
    main()
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print("Hello from: {}".format(__file__.replace('\\', '/').split('/')[-2]))

if __name__ == '__main__':
    main()
    
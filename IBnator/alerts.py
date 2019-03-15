#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
import sys
from util import pretty_json, read_json

# TODO: API to download this JSON file.
# TODO: Add other tags.

class AlertWrapper(object):

    def __init__(self):
        self.json_files = ['alert.json']

    def parse_alerts(self):
        '''
        Parse the alert files for osquery malware.
        '''
        for input_file in self.json_files:
            data = read_json(input_file)

            for item in data:
                try:
                    tag = item['tags']

                    if 'osquery' in tag:
                        self.parse_osquery(item)

                    elif 'duo' in tag:
                        self.parse_duo(item)

                except KeyError as err:
                    print 'Key {0} not found.'.format(err)

    def parse_osquery(self, item):
        '''
        Parse content from osquery alert
        '''
        try:
            hostIdentifier = item['content']['hostIdentifier']
            name = item['content']['name']
            username = item['content']['decorations']['username']
            print "Malware {0} found on host {1} from {2}".format(name, hostIdentifier, username)

        except KeyError as err:
            print 'Key {0} not found. Dumping JSON data...'.format(err)
            pretty_json(data)

    def parse_duo(self, item):
        '''
        Parse content from duo alerts
        '''
        try:
            pretty_json(item)

        except KeyError as err:
            print 'Key {0} not found. Dumping JSON data...'.format(err)
            pretty_json(data)


if __name__ == '__main__':
    aw = AlertWrapper()
    aw.parse_alerts()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyring
import getpass
import sys
import json


def get_key(key):
    '''
    Get API key.
    '''
    token = keyring.get_password(key, key)
    if not token:
        token = getpass.getpass("Please enter {0}: ".format(key))

    return token


def pretty_json(self, data):
    '''
    STDOUT JSON in a pretty format
    '''
    return json.dumps(data, indent=4, sort_keys=True)


def read_json(input_file):
    '''
    Loads data from JSON files.
    '''
    try:
        with open(input_file, 'r') as json_data:
            return json.load(json_data)

    except IOError:
        print "Input file '{0}' does not exist.".format(input_file)
        sys.exit(1)
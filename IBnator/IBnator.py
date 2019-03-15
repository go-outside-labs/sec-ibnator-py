#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import argparse
from duo_locked_out import Check_Duo_Account
from slack_wrapper import SlackWrapper
from alerts import AlertWrapper


LOG_LEVEL = logging.DEBUG


def setup_log(config):
    '''
        Set the logging config.
    '''
    logging.basicConfig(filename=os.path.abspath(config['LOG_FILE']), \
                        format='%(asctime)s %(message)s', \
                        level=LOG_LEVEL)


def get_arguments():
    '''
        Return selected option in form of an Argparser object.
    '''
    parser = argparse.ArgumentParser(description='IBnator is the security analysts')
    parser.add_argument('-d', '--duo_lockout', action='store_true', help='Uses duo Admin API to determine which users are locked out.')
    parser.add_argument('-p', '--ping_locked_users', action='store_true', help='Slack-Ping users that are locked out from Duo.')
    parser.add_argument('-a', '--alerts', action='store_true', help='Reads 411 alerts.')

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def run(args):
    '''
        DO IT.
    '''

    if args.duo_lockout:
        try:
            cda = Check_Duo_Account()
            cda.main()
        except KeyboardInterrupt:
            logging.warning("\n[!] Program killed.")

    elif args.ping_locked_users:
        cda = Check_Duo_Account()
        sw = SlackWrapper()
        cda.main()
        for user in cda.locked_users:
            sw.message_user(user)

    elif args.alerts:
        aw = AlertWrapper()
        aw.read_411_alerts()


def main():

    run(get_arguments())


if __name__ == '__main__':

    main()



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import duo_client

from util import get_key


class Check_Duo_Account(object):

    def __init__(self):
        self.ikey = get_key("duoadminapi_ikey")
        self.skey = get_key("duoadminapi_skey")
        self.host = "xxxxxx.duosecurity.com"
        self.locked_users = []

    def admin_check_users(self):
        '''
        Makes call to Duo Admin API
        '''
        try:
            admin_api = duo_client.Admin(self.ikey, self.skey, self.host)
            users = admin_api.get_users()
            for user in users:
                if user['status'] == 'locked out':
                    if user['username']:
                        print "[*] User: %s Status: %s" % (user['username'], user['status'])
                        self.locked_users.append(user['username'])
                    else:
                        print "[*] User: %s Status: %s" % (user['email'], user['status'])
            else:
                print "[*] No accounts locked out."

        except Exception, err:
            print "[!] Error Getting Status of Duo Security account: {0}".format(err)

    def main(self):
        '''
        DO IT.
        '''
        self.admin_check_users()


if __name__ == '__main__':
    try:
        cda = Check_Duo_Account()
        cda.main()
    except KeyboardInterrupt:
        print "\n[!] Program killed."


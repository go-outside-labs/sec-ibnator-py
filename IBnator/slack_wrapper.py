#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackclient import SlackClient
import logging


class SlackWrapper(object):

    def __init__(self):
        self.username = "Bot"
        self.message = [{
            "title": "Hi, I have a question for you!",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "yes",
                    "text": "I'm locked out.",
                    "type": "button",
                    "value": "yes"
                },
                {
                    "name": "no",
                    "text": "I can connect fine.",
                    "type": "button",
                    "value": "no"
                }
            ]}]
        self.channel = "#security-announce"
        self.sc = SlackClient(self.get_key("slack_token"))

    def get_key(self, key):
        '''
        Get API key.
        '''
        token = keyring.get_password(key, key)
        if not token:
            token = getpass.getpass("Please enter {0}: ".format(key))

        return token

    def message_channel(self):
        '''
        Send a Slack DM to the specified user.
        '''
        message_type = "chat.postMessage"
        send_message(message_type, message)

    def message_channel(self, channel=None, message=None):
        '''
        Send a message in a channel.
        '''
        self.channel = self.channel or channel
        self.message = self.message or message
        print '[*] Sending message to channel {0}.'.format(self.channel)

        message_type = 'chat.postMessage'

        response = self.sc.api_call(
            message_type,
            channel=self.channel,
            attachments=self.message,
            username=self.username)

        print response

    def message_user(self, user, channel=None, message=None):
        '''
        Send a DM message to a user.
        '''
        logging.info('[*] Trying to contact {0}.'.format(user))

        self.channel = self.channel or channel
        self.message = self.message or message

        message_type = 'chat.postEphemeral'
        response = self.sc.api_call(
            message_type,
            channel="@bt3",
            attachments=self.message,
            username=self.username,
            as_user=False,
            user="@bt3")

        print response


if __name__ == '__main__':

    sw = SlackWrapper()
    #sw.message_channel()
    sw.message_user('bt3')
    users = sw.sc.api_call("users.list")
    for user in users['members']:
        if 'first_name' in user['profile'] and user['profile']['first_name'] == 'Buffy':
            print user['profile']
            print user['profile']['id']
            print




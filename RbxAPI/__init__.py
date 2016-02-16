# -*- coding: utf-8 -*-
"""
Project: RbxAPI
File: party.py
Author: Diana
Creation Date: 6/8/2014

Used for my TOP SECRET PARTY CHAT PROGRAM
IF YOU'RE VIEWING THIS YOU SHOULD NOT BE AND YOU SHOULD TELL ME NOW

Copyright (C) 2016  Diana Land
Read LICENSE for more information
"""
import json

from RbxAPI import general

basePartyURL = 'http://www.roblox.com/chat/party.ashx'


def getMembers():
    """
    Get Party Members.

    :return:
    """
    s = general.getSession()
    r = s.get(basePartyURL + '?reqtype=get')
    text = general.Convert(r.text)
    try:
        users = []
        for user in text['Members']:
            users.append(user['UserName'])
        return users
    except KeyError:
        pass


def getGUID():
    """
    Get Party GUID

    :return:
    """
    s = general.getSession()
    r = s.get(basePartyURL + '?reqtype=get')
    try:
        text = general.Convert(r.text)
    except Exception:
        print(text['Error'])
        raise
    try:
        return text['PartyGuid']
    except KeyError:
        pass


def invite(User):
    """
    Invite user User to the party

    :param User: User to invite
    :type User: str
    :return: Error or False
    :rtype: str | bool
    """
    s = general.getSession()
    result = s.get(basePartyURL + '?reqtype=inviteUser&userName=' + User)
    text = general.Convert(result.text)
    if text['Error']:
        return text['Error']


def createAndInvite(User):
    """
    Create a party and invite user User

    :param User: User to invite.
    :type User: str
    :return: Nothing, or error.
    :rtype: str | list | None
    """
    s = general.getSession()
    result = s.get(basePartyURL + '?reqtype=createAndInvite&userName=' + User)
    text = general.Convert(result.text)
    if 'Error' in text:
        return text['Error']


def kick(User):
    """
    Kick a user User from the party.

    :param User: User to kick.
    :type User: str
    :return:
    """
    s = general.getSession()
    ID = s.get('http://api.roblox.com/users/get-by-username?username=' + User)
    ID = json.loads(ID.text)['Id']
    text = s.get(basePartyURL + '?reqtype=removeUser&userid=' + str(ID))
    text = json.loads(text.text)
    if 'Error' in text:
        return text['Error']


def message(Msg):
    """
    Message Msg to party

    :param Msg: Message to send
    :type Msg: str
    :return: Error or nothing
    :rtype: None | str
    """
    s = general.getSession()
    send = 'http://www.roblox.com/chat/send.ashx?partyGuid=' + getGUID()
    r = s.post(send, data={'message': Msg},
               headers={'X-CSRF-TOKEN': general.GetToken(), 'X-Requested-With': 'XMLHttpRequest'})
    text = general.Convert(r.text)
    if 'Error' in text:
        return text['Error']


def getLastMessage():
    """
    Get last message.

    :return: list of messages
    :rtype: list[str]
    """
    s = general.getSession()
    r = s.get('http://www.roblox.com/chat/get.ashx?reqType=getallchatswithdata&openChatTabs=&activechatids=&getpartysta'
              'tus=true&timeZoneOffset=240')
    try:
        text = general.Convert(r.text)
    except Exception:
        raise
    try:
        # print(text['PartyStatus']['Conversation'])
        ms = len(text['PartyStatus']['Conversation'])
        if ms != 0:
            return text['PartyStatus']['Conversation'][ms - 1]['SenderUserName'], \
                   text['PartyStatus']['Conversation'][ms - 1]['Message']
            # messages = []
            # for item in text['PartyStatus']['Conversation']:
            #     messages.append(item['SenderUserName'] + ": " + item["Message"])
            # return messages
    except KeyError:
        pass


def getMessages():
    """
    Get messages.

    :return: list of messages
    :rtype: list[str]
    """
    s = general.getSession()
    r = s.get('http://www.roblox.com/chat/get.ashx?reqType=getallchatswithdata&openChatTabs=&activechatids=&getpartysta'
              'tus=true&timeZoneOffset=240')
    try:
        text = general.Convert(r.text)
    except Exception:
        raise
    try:
        ms = len(text['PartyStatus']['Conversation'])
        if ms != 0:
            messages = []
            for item in text['PartyStatus']['Conversation']:
                messages.append({item['SenderUserName']: ": " + item["Message"]})
            return messages
    except KeyError:
        pass


def getLeader():
    """
    Get leader of Party.

    :return: Party Leader Username
    :rtype: str
    """
    s = general.getSession()
    r = s.get(basePartyURL + '?reqtype=get')
    try:
        text = general.Convert(r.text)
    except Exception:
        print(text['Error'])
        raise
    try:
        return text["CreatorName"]
    except KeyError:
        pass


def setup():
    """
    Setup the program.

    """
    pass


if __name__ == '__main__':
    setup()
    getMessages()

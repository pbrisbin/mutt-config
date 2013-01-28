#!/usr/bin/python2
#
# Very stripped-down, simplified, feature-less version of gcontacts.py
# by Jim Karsten.
#
# $ GMAIL_USER='x@gmail.com' GMAIL_PASS='x' ./gmail2mutt.py > aliases
#
###

import os
import sys
import re

import gdata.contacts
import gdata.contacts.service

class Addressbook:
    def __init__(self, contacts):
        """
        An Addressbook is initialized from a gdata contacts feed of
        entries. They are maintained internally as a dictionary of
        Name->[Email] containing only valid entries.
        """
        self.addresses = {}

        for contact in contacts:
            name   = contact.title.text
            emails = contact.email

            if name and emails:
                curr = self.addresses.get(name, [])
                new  = map(lambda e: e.address, emails)

                self.addresses[name] = curr + new

    def dump(self, formatter):
        """
        Dump our names and emails using the provided formatter which is
        a function of two arguments: name and array of email addresses.
        The array is guaranteed to be 1+ elements.
        """
        names = self.addresses.keys()
        names.sort()

        for name in names:
            formatter(name, self.addresses[name])


def query_contacts(email, password, limit = 999999):
    client = gdata.contacts.service.ContactsService()
    client.email = email
    client.password = password

    client.ProgrammaticLogin()

    query = gdata.contacts.service.ContactsQuery()
    query.max_results = limit

    return client.GetContactsFeed(query.ToUri()).entry


def alias_formatter(name, emails):
    # TODO: for now we just print the first email of each contact,
    # eventually we should make incrementing suffixes for contacts with
    # more than one email
    print "alias {key} {name} <{email}>".format(
            key  = re.sub(r'\s+', '_', name.lower()),
            name = name, email = emails[0]
            )


if __name__ == '__main__':
    email    = os.environ.get('GMAIL_USER')
    password = os.environ.get('GMAIL_PASS')

    if not (email and password):
        sys.stderr.write("GMAIL_USER or GMAIL_PASS not set\n")
        exit(1);

    contacts = query_contacts(email, password)

    Addressbook(contacts).dump(alias_formatter)

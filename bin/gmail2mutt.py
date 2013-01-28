#!/usr/bin/python2
#
# Very stripped-down, simplified, feature-less version of gcontacts.py
# by Jim Karsten.
#
# $ GMAIL_USER='x@gmail.com' GMAIL_PASS='x' ./gmail2mutt.py > aliases
#
###

__author__  = "Patrick Brisbin <pbrisbin@gmail.com>"
__version__ = "0.1"

import os
import re
import sys

import gdata.contacts
import gdata.contacts.service

if __name__ == '__main__':
    client = gdata.contacts.service.ContactsService()

    try:
        client.email    = os.environ['GMAIL_USER']
        client.password = os.environ['GMAIL_PASS']
    except:
        sys.stderr.write("GMAIL_USER or GMAIL_PASS unset\n")
        exit(1)

    client.ProgrammaticLogin()

    query = gdata.contacts.service.ContactsQuery()
    query.max_results = 999999

    # interpolated print used to not confuse vim when editing this file
    print "# {vim}: ft={ft}".format(vim = "vim", ft = "mutt")

    for entry in client.GetContactsFeed(query.ToUri()).entry:
        name = entry.title.text or None

        if name and entry.email:
            print "alias {key} {name} <{email}>".format(
                    key   = re.sub(r'\s+', '_', name.lower()),
                    name  = name,
                    email = entry.email[0].address
                    )

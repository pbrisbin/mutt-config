# Mutt

This is my `~/.mutt`.

## Offlineimap

Two Gmail accounts are kept in sync with directories under `~/Mail` via 
Offlineimap. See the config in `./examples`.

Newer Offlineimap is very strict in that any name translation used going 
from Remote -> Local must be correctly reversed by the name translation 
going from Local -> Remote. If the translations don't accurately reverse 
each other, Offlineimap will duplicate folders or error.

My translation logic is consolidated in `./nametrans.py`.

The translations found in `mapping` are tried first. Otherwise, a 
catchall, regex-based translation is made. The catchall will translate 
between `Proper case` (remote) and `snake_case` (local). This requires 
your remote labels and local directories follow this (completely 
arbitrary) convention.

If you've got labels that cannot be properly translated by this simple 
rule, you must either exclude them from the sync (see the `exclude` 
function), or simply add them to `mapping`.

## Mailrun

I don't trust Offlineimap as a daemon, so I just manually sync every 3 
minutes via [f]cron.

~~~
*/3 * * * * /home/you/.mutt/bin/mailrun
~~~

`mailrun` gives offlineimap 60 seconds to complete before forcibly 
killing that process. In my experience if it's not done in 30, it's 
hung. You may want to adjust these numbers depending on the size and 
number of your mailboxes.

Either way, you should run your first sync manually since it will take 
*a while*.

## Msmtprc

Msmtprc is used to send emails from either account via the commandline 
or Mutt. See the config in `./examples`.

## Mail query

Mail query is a little C app I wrote which reads your existing mail for 
addresses and presents them in a format such that mutt can use them for 
tab completion. Given a small enough mailbox, it's usably fast.

It is available in its own [repo][].

[repo]: https://github.com/pbrisbin/mail-query

## Gmail2mutt

This simple script fetches your Gmail contacts using `python-gdata` and 
outputs them in mutt alias format.

~~~
$ bin/gmail2mutt.py > aliases
~~~

It uses the environment variables `GMAIL_USER` and `GMAIL_PASS`.

## Mutt

Mutt accesses the mailboxes under the two synced folders in `~/Mail` and 
uses `folder-hook`s to adjust the appropriate settings (`from`, 
`sendmail`, etc) depending on what folder you're in.

Be sure to review all settings and `man muttrc` for anything you don't 
understand.

# Mutt

This is my `~/.mutt`. Requires [mutt-kz][].

[mutt-kz]: https://aur.archlinux.org/packages.php?ID=57156

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
*/3 * * * * /home/you/.mutt/mailrun
~~~

If `mailrun` finds an `offlineimap` currently running, it `kill`s it. In 
my experience, it's hung. That said, you should run your first sync 
manually since it will take *a while*.

## Msmtprc

Msmtprc is used to send emails from either account via the commandline 
or Mutt. See the config in `./examples`.

## Mail query

Mail query is a little C app I wrote which reads your existing mail for 
addresses and presents them in a format such that mutt can use them for 
tab completion. Given a small enough mailbox, it's usably fast.

It is available in its own [repo][].

[repo]: https://github.com/pbrisbin/mail-query

## Notmuch

Notmuch support is fully integrated in mutt-kz. Search with `,s`.

## Mutt

Mutt accesses the mailboxes under the two synced folders in `~/Mail` and 
uses `folder-hook`s to adjust the appropriate settings (`from`, 
`sendmail`, etc) depending on what folder you're in.

Be sure to review all settings and `man muttrc` for anything you don't 
understand.

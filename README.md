# Mutt

This is my `~/.mutt`.

## Offlineimap and Msmtp

Two Gmail accounts are kept in sync with directories under `~/Mail` via 
Offlineimap. Msmtprc is used to send emails from either account via the 
commandline or Mutt.

You can find the relevant configs for both of these tools in my 
[dotfiles][] repo.

[dotfiles]: https://github.com/pbrisbin/dotfiles

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

## Mail query

Mail query is a little C app I wrote which reads your existing mail for 
addresses and presents them in a format such that mutt can use them for 
tab completion. Given a small enough mailbox, it's usably fast.

It is available in its own [repo][].

[repo]: https://github.com/pbrisbin/mail-query

## Mutt

Mutt accesses the mailboxes under the two synced folders in `~/Mail` and 
uses `folder-hook`s to adjust the appropriate settings (`from`, 
`sendmail`, etc) depending on what folder you're in.

Be sure to review all settings and `man muttrc` for anything you don't 
understand.

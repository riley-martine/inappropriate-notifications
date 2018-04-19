Inappropriate Notifications
===========================
.. image:: https://badge.fury.io/py/inappropriate-notifications.svg
    :target: https://badge.fury.io/py/inappropriate-notifications

Ever want to get inappropriate notifications on your computer while
you're presenting? Well now you can!

Based off of the homepage of https://muzzleapp.com/. Check out their
website to see an example of what this does.

This program uses notifications from
https://muzzleapp.com/notifications/notifications.json, as well as those
we came up with ourself.

User names and images downloaded from https://randomuser.me.

Requirements
------------

Linux
~~~~~

python3.6+ libnotify

Windows
~~~~~~~

python3.6+ win10toast (installed automatically)

Installation
------------
``pip install inappropriate-notifications``

Alternative installation
~~~~~~~~~~~~~~~~~~~~~~~~
``git clone https://github.com/riley-martine/inappropriate-notifications.git``

``cd inappropriate-notifications``

``python3.6 setup.py install``


Usage
-----
Display help: ``inappropriate-notifications -h``

Display one inappropriate notification: ``inappropriate-notifications --once``

Display notifications about 2 seconds apart: ``inappropriate-notifications -t 2``

Display 20 notifications about 5 seconds apart: ``inappropriate-notifications -c 20 -t 5``




Caveats (To fix / to do)
------------------------

-  Only tested on Ubuntu and Windows 10 (MacOS and Windows 7 on roadmap)
-  Relies on libnotify on Linux
-  Icons are for Mac apps and need to be replaced with the ones you use
-  No fields on notifications (reply, dismiss) where applicable
-  Does not pull names/images from people you know when applicable
-  Only suited to work env -- students don't need messages about getting
   fired
-  No tests
-  No version command line argument
-  ctrl-c when running command line should fail nicer
-  Right-to-left names mess up first line
